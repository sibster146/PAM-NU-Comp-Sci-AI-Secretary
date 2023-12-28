import speech_recognition as sr
import paramiko
from urllib.parse import quote
from gtts import gTTS 
import os 
from GreeterDemo import speak

# # def play_audio(mytext):
# #     language = 'en'
# #     myobj = gTTS(text=mytext, lang=language, slow=False) 
# #     # Saving the converted audio in a mp3 file named 
# #     # welcome  
# #     myobj.save("welcome.mp3") 
# #     # Playing the converted file 
# #     os.system("welcome.mp3") 



def execute_remote_query(query):
    # URL-encode the query string
    encoded_query = quote(query)

    # Define the SSH parameters
    hostname = '3.21.236.74'
    port = 22
    username = 'ec2-user'
    private_key_path = 'test2.pem'

    # Initialize the SSH client
    client = paramiko.SSHClient()

    # Automatically add the server's host key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    client.connect(hostname, port, username, key_filename=private_key_path)

    # Construct the command with the URL-encoded query parameter
    command = f'curl 127.0.0.1:8000/query_func/{encoded_query}'

    # Execute the command
    stdin, stdout, stderr = client.exec_command(command)
   # print(stdout.read().decode('utf-8'))
    return stdout
    print("its done here")
    lines = []
    # Process the output
    for line in stdout:
        lines.append(line.strip('\n'))
    # Close the connection
    print("its done parsing")
    client.close()

    return "".join(lines)





# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech_from_mic(recognizer, source):

    
    # Check that recognizer and source arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    # Start recording from the microphone
    recognizer.adjust_for_ambient_noise(source)
    recognizer.energy_threshold = 9000
    audio = recognizer.listen(source)

    # Recognize speech using Google Web Speech API
    try:
        return recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        return "API unavailable"
    except sr.UnknownValueError:
        # Speech was unintelligible
        return None

# Continuously listen to the microphone and print what is heard
try:
    with sr.Microphone() as source:
        while True:
            print("Listening...")
            speech = recognize_speech_from_mic(recognizer, source)
            if not speech:
                continue
            print("You said: " + speech)
            response = execute_remote_query(speech)
            print("got response")
            answer = response.read().decode('utf-8')
            speak(answer)
            #play_audio(str(answer))

except KeyboardInterrupt:
    print("\nProgram stopped manually.")

#speak("hi")



  
