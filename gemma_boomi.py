# This is the main script callable from either terminal or the local boomi atom. the format will be: python script-path "llm prompt"

import sys
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def generate_text(prompt, model_name="google/gemma-2b-it", max_new_tokens=50):
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Encode input and generate output
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    input_ids = input_ids.to(model.device)
    outputs = model.generate(input_ids, max_new_tokens=max_new_tokens)
    
    # Decode and return output
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gemma_script.py 'Your prompt here'")
        sys.exit(1)

    prompt = sys.argv[1]
    generated_text = generate_text(prompt)
    print(generated_text)
