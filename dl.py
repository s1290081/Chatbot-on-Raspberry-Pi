from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save models and tokenizers
model.save_pretrained("./gpt2_model")
tokenizer.save_pretrained("./gpt2_model")
