
from transformers import pipeline

# Load the GPT-2 language model
generator = pipeline("text-generation", model="gpt2")

# Define the prompt
prompt = "Artificial intelligence is"

print(f"Prompt: {prompt}")

# Generate text
result = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=1
)

print(f"Result: {result[0]['generated_text']}")

