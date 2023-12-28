from server import application, qa, memory, stemmer, course_matching
# import spacy
@application.route("/")
def home():
    return "No Home Page. This is web service"



@application.route('/query_func/<string:query>')
def query_func(query):
    """
    print(query)
    nlp = spacy.load("en_core_web_sm")
    def contains_pronoun(query):

	
        doc = nlp(query)
        not_count = ['who','i']
        count = 0
        for token in doc:
            # Check if the token is a pronoun
            if token.pos_ == "PRON" and token.text.lower() not in not_count:
                return True

#    stemmer = PorterStemmer()

    def get_lemmas_and_stems(sentence, nlp, stemmer):
        # Parse the sentence using the loaded model
        doc = nlp(sentence)
        # Extract lemmas and stems for each token in the sentence
        lemmas = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
        stems = [stemmer.stem(token.text.lower()) for token in doc if token.is_alpha and not token.is_stop]
        return lemmas, stems

    def have_same_topic(sentence1, sentence2, nlp, stemmer):
        # Get lemmas and stems from both sentences
        lemmas1, stems1 = get_lemmas_and_stems(sentence1, nlp, stemmer)
        lemmas2, stems2 = get_lemmas_and_stems(sentence2, nlp, stemmer)

        # Count lemmas and stems in both sentences
        lemma_freq1 = Counter(lemmas1)
        lemma_freq2 = Counter(lemmas2)
        stem_freq1 = Counter(stems1)
        stem_freq2 = Counter(stems2)

        # Find common elements
        common_lemmas = lemma_freq1 & lemma_freq2
        common_stems = stem_freq1 & stem_freq2

        #print(common_lemmas, common_stems)

        # Decide if they share the same topic based on common lemmas and stems
        return len(common_lemmas) > 0 or len(common_stems) > 0

    def is_follow_up(memory, query):
        prev_text = ' '.join([m.content for m in memory.chat_memory.messages])
        return contains_pronoun(query) or have_same_topic(prev_text, query, nlp, stemmer)
    """
    def ask_query(query):
       #  if not is_follow_up(memory, query):
       #    memory.clear()

        # print(memory)

        query = course_matching(query)

        # qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0, max_tokens=75), vectorstore.as_retriever(), memory= memory)
        result = qa({"question":query})
        response = result["answer"]
        return response

    return ask_query(query)
        
