from flask import Flask, render_template, request
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

app = Flask(__name__)

model_path = "./Llama-68M-Chat-v1"

tokenizer = LlamaTokenizer.from_pretrained(model_path, padding_side='left')
model = LlamaForCausalLM.from_pretrained(model_path)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')

    # Llama-68M-Chat-v1, line 41 of README.md for reference.
    system_message = "You are a helpful assistant who provides concise responses."
    # Recommended Prompt Format
    prompt = f"<|im_start|>system\n{system_message}<|im_end|>\n"
    prompt += f"<|im_start|>user\n{user_text}<|im_end|>\n"
    prompt += "<|im_start|>assistant\n"

    input_ids = tokenizer.encode(prompt, return_tensors='pt', add_special_tokens=True).to(device)

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_length=200,
            # Recommended Inference Parameters
            penalty_alpha=0.5,
            top_k=4,
            pad_token_id=tokenizer.eos_token_id,
            attention_mask=torch.ones(input_ids.shape).to(device)
        )

    full_response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Only the assistant part is extracted and special tokens are removed
    ai_response_start = full_response.find("<|im_start|>assistant")
    ai_response = full_response[ai_response_start + len("<|im_start|>assistant"):].strip()

    # Remove unnecessary “<|im_end|>”.
    ai_response = ai_response.replace("<|im_end|>", "").strip()

    return str(ai_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, use_reloader=False)
