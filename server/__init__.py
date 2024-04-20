from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import openai
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from IPython.display import *
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.prompt import PromptTemplate
from langchain.chat_models import ChatOpenAI

import os
import shutil
import numpy as np
import pandas as pd

import spacy
import nltk
from nltk.stem.porter import PorterStemmer
from collections import Counter


from flask import Flask

import sqlite3
import re

def create_course_database():

  connection = sqlite3.connect('whereiseveryone.db')
  course_data = pd.read_csv('server/CScourses.csv')
  # Write the data to a sqlite table
  course_data.to_sql('course', connection, if_exists='replace', index=False)

create_course_database()


def course_matching(sentence):
 
  patterns = ('computer science \d\d\d', 'cs \d\d\d', 'cs\d\d\d', 'COMP_SCI \d\d\d')
  courses = re.compile("(%s|%s|%s|%s)" % patterns).findall(sentence) #["COMP_SCI 322", "cs 211", ...]

  # Create a cursor object
  connection = sqlite3.connect('whereiseveryone.db')
  cur = connection.cursor()

  for i in range(len(courses)):
    course_num = courses[i][-3:]
    rows = cur.execute(f"SELECT `course name`, `course title` FROM course WHERE `course name` LIKE '%{course_num}%'")
    res = rows.fetchone()
    if res != None:
      sentence = re.sub(courses[i], ": ".join(res), sentence)

  connection.close()
 
  return sentence


stemmer = PorterStemmer()

# OPENAI_API_KEY = ##############################
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

event_loader = TextLoader("server/updated_faculty_and_events_data.txt")
event_document = event_loader.load()

embeddings = HuggingFaceEmbeddings()
text_splitter = CharacterTextSplitter(chunk_size=750, chunk_overlap=0)
documents = text_splitter.split_documents(event_document)
vectorstore = Chroma.from_documents(documents, embeddings)

memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True, k=5)

template = (
                "If the question make sense on its own, don't consider the information in chat history and only search answer for the question. "
                "If the question does not make sense on its own, given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language."
                "Answer the question accurately. If you don't know the answer, do not make up one. "

                "You are a lovely receptionist who answer questions about CS department. You make everyone feel welcome. Your name is Pam."

                "Chat History: {chat_history}"
                "follow up question: {question}"
            )
prompt = PromptTemplate.from_template(template)
llm = ChatOpenAI() #OpenAI(temperature=.3, max_tokens=75)

#question_generator_chain = LLMChain(llm=OpenAI(temperature=.3, max_tokens=75), prompt=prompt)
qa = ConversationalRetrievalChain.from_llm(
    #combine_docs_chain=combine_docs_chain,
    llm=llm,
    retriever=vectorstore.as_retriever(),
    condense_question_prompt=prompt,
    verbose=False,
    memory= memory,
)




application = Flask(__name__)
application.secret_key = "hi"

from server import routes
print("done")
