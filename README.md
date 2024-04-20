PROJECT NAME

PAM- the AI Receptionist for the Northwestern Computer Science department

PROJECT DESCRIPTION

Pam is a LLM designed to answer questions about the Northwestern CS department. She can answer questions about professors, computer science research, events, and courses. 

INSTALLATION

Git clone the repository into your local repository. Install the dependencies in requirements.txt. You will need a OPENAI api key. Once you obtain that, insert it into the __init__.py module online line 64. 

RUN

There are two components to the application. The client and the server. The server is written in a Flask framework. Running the server locally will take up a lot of CPU power, so it is recommended to run on a t2 large EC2 instance. Install application.py and server onto the EC2 instance. Also, note the EC2 instance's IP address. For the client to communicate with the server, we are going to SSH into the EC2 instance. Ensure that the EC2 instance that is being used has the permissions to allow SSH. TO SSH, the IP address, port, username, and private key path (for pem files). These fields will be used in client.py. To run the server, you will need an OPENAI api key. Once you obtain that, insert it into the server/__init__.py module on line 64. 


Presentation: https://vimeo.com/908564340?share=copy
