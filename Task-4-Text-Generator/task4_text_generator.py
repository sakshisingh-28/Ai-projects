from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = "The future of artificial intelligence is"
result = generator(prompt, max_length=100, num_return_sequences=1)

print("Generated Text:\n", result[0]['generated_text'])
