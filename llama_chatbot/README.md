# llama_rasp

The model of gpt2_chatbot was changed from gpt2 to llama. The model is tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf. The model of gpt2_chatbot was changed from gpt2 to llama. The model is TinyLlama-1.1B-Chat-v1.0-GGUF. I used the following site for reference. Downloading the model and installing llama_cpp_python made it easy to run.

Reference: https://qiita.com/kazuhitoyokoi/items/66e8c9e1b447a2850ba7

DL link: https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

I tried the llama-2-7b quantization model but could not generate sentences on raspberry pi. (llama-2-7b.Q2_K.gguf, llama-2-7b.Q4_0.gguf, llama-2-7b.Q8_0.gguf)

https://huggingface.co/TheBloke/Llama-2-7B-GGUF/tree/main

# Execution Result
I asked the same question as I did for gpt2_chatbot.
![Llama Chatbot_page-0001](https://github.com/user-attachments/assets/4971e025-caab-47d4-ad19-e96060358f1e)
