Pam is a LLM designed to answer questions about the Northwestern CS department.

SET UP
The modules "server" and "application.py" contain the LLM, which was built as a Flask server application. "Client.py" contains an always listening scripts that will listen to speech,
convert it to text, and send the text to the server. The LLM will find the response to the question and return it to the client. I recommend deploying the Flask application as a web 
server on an EC2 instance with NGINX.

Presentation: https://vimeo.com/908564340?share=copy
