import warnings
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# FutureWarningを無視する
warnings.simplefilter('ignore', FutureWarning)

# ローカルディスクからモデルとトークナイザーをロード
tokenizer = GPT2Tokenizer.from_pretrained('./gpt2_model')
model = GPT2LMHeadModel.from_pretrained('./gpt2_model')

# パディングトークンIDを設定
if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

# テキスト生成の例
input_text = "how are you?"
inputs = tokenizer(input_text, return_tensors='pt')

# Attention maskを設定
attention_mask = (inputs['input_ids'] != tokenizer.pad_token_id).to(torch.long)

# 文章を生成
outputs = model.generate(
    inputs['input_ids'],
    attention_mask=attention_mask,
    max_length=150,
    pad_token_id=tokenizer.eos_token_id,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    repetition_penalty=1.5,
    do_sample=True
)

# 生成されたテキストを表示
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)

# 文が終了するまでの後処理（例: ピリオドでカット）
end_index = generated_text.find('.')
if end_index != -1:
    generated_text = generated_text[:end_index+1]
print(generated_text)
