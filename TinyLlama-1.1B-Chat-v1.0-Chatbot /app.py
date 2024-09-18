from flask import Flask, render_template, request
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re

app = Flask(__name__)

model_path = "./TinyLlama-1.1B-Chat-v1.0" 

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')

    messages = [
        {"role": "system", "content": "You are a friendly chatbot who always responds in the style of a pirate"},
        {"role": "user", "content": user_text}
    ]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_new_tokens=200
        )

    full_response = tokenizer.decode(output[0], skip_special_tokens=True)

    ai_response = full_response.split("<|assistant|>")[-1].strip()

    sentences = re.split(r'(?<=[.!?])\s+', ai_response)
    complete_sentences = [sent for sent in sentences if sent.strip().endswith(('.', '!', '?'))]
    
    ai_response = ' '.join(complete_sentences)

    return str(ai_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
