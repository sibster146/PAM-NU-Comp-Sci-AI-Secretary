import requests
import time
import uuid
import re

# Our communication API endpoints 

append = "https://api.the-singularity-show.com/api/append/"
ready = "https://api.the-singularity-show.com/api/ready/"
done = "https://api.the-singularity-show.com/api/done/"
ready = "https://api.the-singularity-show.com/api/ready/"
clearqueue = "https://api.the-singularity-show.com/api/clearqueue/"

header = {"Content-Type": "application/json"}


# Tools to manage the asynchronous control of actions. Used to make sure actions do not 
# start until speaking is finished. It is based on the idea that every speech action is 
# given an ID and subsequent actions can be designed to wait until a speech action is complete 

# Every action is given a unique ID that is used to track whether the action is finished
# generateID generates a unique ID for tracking synchronous actions
  
def generateID():
	return uuid.uuid4().hex

# The web pages track whether or not a speech action has completed but the core system has to do
# so as well. waitUntilOver pauses action until the actionID associated with an earlier action
# is complete
	
def	waitUntilOver(actionID):
	done = False
	while not done:
		time.sleep(.1)
		response=requests.post(ready, headers=header, json={"id": actionID})
		if response.json()["content"] == True:
			print("Done")
			done = True
			

# splitIntoSentences does what it seems to. It splits a paragraph (as a string) into a list
# of strings, each of which isa sentence.

def splitIntoSentences(text):
	return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s', text)

# paragraphSpeak breaks the paragraph into sentences and sends them individually to the named page
# It speeds the voice up by 10%. We break the sentences up so the text to speech system can use shorter
# texts
 
def paragraphSpeak(text, speaker, trigger = "Free Trigger"):
	sentences = splitIntoSentences(text)
	content = []   
	for sentence in sentences:
		print(sentence)
		id = generateID()
		utterance = f'<prosody rate="+10%"> {sentence} </prosody>'
		content.append({"text": utterance, "trigger": "Free Trigger", "id": id})
	content[0]["trigger"]=trigger
	data = {"content": content, "file": speaker}
	requests.post(append, headers=header, json=data)		
	return id


# Along with the functions associated with saying things, there are other actions that
# We can request the Avatars to take.

# Send image takes an image and the name of a DVI and sends it to the target
# The image pair is the URL for the image and the name of the DIV

def sendImage(image_pair, target, trigger = "Free Trigger"):
	content = {"image": image_pair}
	data ={"content": [content], "file": target}
	waitUntilOver(trigger)
	response = requests.post(append, headers=header, json=data)
	return "Free Trigger"


# purge sends a signal to the avatar page to halt speaking and remove all actions that are in its queue

def purge(speaker):
	print(f"Purging {speaker}")
	data = {"file": speaker, "content": [{"action": "PURGE"}]}
	requests.post(append, headers=header, json=data) 
	
# reset triggers clears the trigger list and then adds "Free Trigger for any commands that do not require triggers

def resetTriggers():
	print(f"Clearing Trigger queue")
	requests.post(clearqueue, headers=header, json={})
	requests.post(done, headers=header, json={"id": "Free Trigger"})


