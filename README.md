**PROJECT NAME**

PAM- the AI Receptionist for the Northwestern Computer Science department

**PROJECT DESCRIPTION**

Pam is a LLM designed to answer questions about the Northwestern CS department. She can answer questions about professors, computer science research, events, and courses. 

**APPLICATION OVERVIEW**

Client Side- client.py, ClassCode.py, GreeterDemo.py, http://the-singularity-show.com/pages/CS338/greeter.html (for the avatar)

Server Side- application.py, server/

**RUN**

There are two components to the application. The client side and the server side. 

The server is written in a Flask framework. Running the server locally will take up a lot of CPU power, so it is recommended to run on a t2 large EC2 instance. Install application.py and server onto the EC2 instance. You will need an OPENAI api key. Once you obtain that, insert it into the server/__init__.py module on line 64.

Bote the EC2 instance's IP address. For the client to communicate with the server, we are going to SSH into the EC2 instance. Ensure that the EC2 instance that is being used has the permissions to allow SSH. To SSH, the IP address, port, username, and private key path (for pem files). Clone client.py, ClassCode.py, and GreeterDemo.py into a directory on you local device. Ensure that local directory also has the necessary key file to be able to the SSH into the EC2 instance. Insert the IP address, port, username, and private key path (for pem files) into client.py. You will also need to launch the avatar on http://the-singularity-show.com/pages/CS338/greeter.html. The avatar will respond to the questions you ask on this site. 

To run the server, cd into the repository with application.py and server/ and run python application.py. Install the dependencies as necessary.
To run the client, cd into the repository with client.py, ClassCode.py, GreeterDemo.py and run python client.py, and open the avatar url on a separate window. Install dependecies as necessary.
Once the server and client are running, you should be able to speak into your local device and hear the answer from the avatar a few seconds later.

**MODULE DETAILS**

SERVER SIDE

application.py- imports the application class that is initialized in server, then run the application class.

server/__init__.py- Reads in the document from server/updated_faculty_and_events_data.txt. Instantiates HuggingFaceEmbeddings, a vector store, a memory window buffer, a prompt template, a llm instance, and a conversational retrieval chain. All of these instances come from the langchain or OPENAI libraries. The data from updated_faculty_and_events_data.txt is embedded and stored in the vector store. The conversational retrieval chain is the interface where queries will be sent to and responses will come from. It is instantiated with the vector store, llm, prompt template, and memory window buffer. Also, in this module, we read in server/CScourses.csv and generate a database about CS courses in server/whereiseveryone.db. At the end of the module, we instantiate the flask application instance. When launching the application, this module will automatically read in all the data and create all the necessary instances and interfaces to recieve queries and generate responses.

routes.py- Contains the endpoint that takes in the client's query. query_func(query) takes the query, calls the conversational retrieval chain (qa) with it, gets a response from the (qa), and returns the response back to the client.

CScourses.csv- contains information about CS courses

updated_faculty_and_events_data(1).txt- contains information about professors and events

whereiseveryone.db- database about cs courses

CLIENT SIDE

ClassCode.py- module was written by Kristian Hammond to communicate with the avatar available at url http://the-singularity-show.com/pages/CS338/greeter.html. paragraphSpeak() sends text to the avatar to speak. purge() purges all the texts in the avatar queue.

GreeterDemo.py- module was written by Kristian Hammond to communicate with the avatar available at url http://the-singularity-show.com/pages/CS338/greeter.html. speak() calls ClassCode.purge() to clear the text queue for the avatar and calls paragraphSpeak().

client.py- 














Presentation: https://vimeo.com/908564340?share=copy
