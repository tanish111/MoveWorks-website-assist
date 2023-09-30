from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"  # You can choose a different variant if needed
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
context = "ceo is bhavin"
question = "who is ceo?"

input_text = f"{context} [SEP] {question}"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
response_ids = model.generate(input_ids, max_length=50, num_return_sequences=1)
response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
print("Answer:", response)


