from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "microsoft/phi-2"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",             # Use GPU if available
    torch_dtype=torch.float16      # Optional: use float32 if on CPU
)

# Define the prompt
prompt = "What is an apple?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# Generate output
outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
