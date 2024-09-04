from flask import Flask, render_template, request
from llama_cpp import Llama

app = Flask(__name__)

# Specify the path of the Llama model
model_path = "./llama_model/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"

# Initialize the Llama model
llm = Llama(model_path=model_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')

    # Generate response
    output = llm(user_text, max_tokens=50)

    # Extract the generated text
    ai_response = output['choices'][0]['text'].strip()

    # Log the AI response
    print("User Input:", user_text)
    print("AI Response:", ai_response)

    return str(ai_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
