# gpt2_rasp
On a Raspberry Pi, I developed a gpt2 web application locally. The following website served as the basis for the web application's development.
https://blog.piandpython.net/make-a-gpt-2-chatbot-with-raspberry-pi-flask-and-gunicorn/#gunicorn

Using dl.py, the gpt2 model was saved in the gpt2_model directory. (The size of pytorch_model.bin prevented it from being submitted to github.)
Tokenizer and model are the contents of the gpt2_model folder that are defined in app.py. The templates folder contains html files.
## First state
1. Enter a message in the text box.
2. When the send button is pressed, gpt2 generates the text.

![GPT-2 Chatbot_page-0001](https://github.com/user-attachments/assets/c29c0051-79cc-40b7-b47a-25fb66bb20f1)
## post-question
I asked the following three questions. "hello", "how are you?", "what is sushi?" For the sake of execution time, the generated text's length was set to 50 characters.

![result_page-0001](https://github.com/user-attachments/assets/b5c12dca-7c3c-4ec6-a395-ef4c5ce07cb8)
