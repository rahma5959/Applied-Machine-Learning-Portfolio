from transformers import pipeline

generator = pipeline(
"text-generation",
model="gpt2"
)

def generate_response(prompt):
    result = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=1
    )

    return result[0]["generated_text"]

