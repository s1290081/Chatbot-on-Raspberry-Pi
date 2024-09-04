# llama_rasp

The model of gpt2_chatbot was changed from gpt2 to llama. The model is TinyLlama-1.1B-Chat-v1.0-GGUF. I used the following site for reference. Downloading the model and installing llama_cpp_python made it easy to run.

Reference: https://qiita.com/kazuhitoyokoi/items/66e8c9e1b447a2850ba7

link: [https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/main](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/tree/main)

I tried the llama-2-7b quantization model but could not generate sentences on raspberry pi. (llama-2-7b.Q2_K.gguf, llama-2-7b.Q4_0.gguf, llama-2-7b.Q8_0.gguf)

https://huggingface.co/TheBloke/Llama-2-7B-GGUF/tree/main

# Execution Result
I asked the same question as I did for gpt2_chatbot. I used 2-bit and 4-bit quantization models to compare results. 5-bit and 6-bit models could not be run. Then there were times when a question would not generate a sentence.
## Q2_K
![Llama ChatbotQ2_K_page-0001](https://github.com/user-attachments/assets/94a004b3-b7cf-4829-ac4c-12da2e71518f)
## Q4_K_M
![Llama Chatbot_page-0001](https://github.com/user-attachments/assets/4971e025-caab-47d4-ad19-e96060358f1e)
