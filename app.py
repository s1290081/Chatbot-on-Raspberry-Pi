from flask import Flask, render_template, request
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Specify the path of the model downloaded locally
model_path = "./gpt2_model"

# Load models and tokenizers with left padding
tokenizer = AutoTokenizer.from_pretrained(model_path, padding_side='left')
model = AutoModelForCausalLM.from_pretrained(model_path)

# Set the padding token to the EOS token
tokenizer.pad_token = tokenizer.eos_token

# Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    input_ids = tokenizer.encode(user_text, return_tensors='pt', add_special_tokens=True).to(device)

    # Generate response
    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=len(input_ids[0]) + 50,  # Reduced max_length for faster response
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,  # Enable sampling
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id,
            attention_mask=torch.ones(input_ids.shape).to(device)  # Add attention mask
        )

    full_response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Remove user text and return only AI responses
    ai_response = full_response[len(user_text):].strip()

    return str(ai_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
