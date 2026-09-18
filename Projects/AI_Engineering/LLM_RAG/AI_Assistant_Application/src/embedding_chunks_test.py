
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from document_loader import load_documents, split_document
from transformers import pipeline

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load documents
file_path = "../Data/documents/ai_basics.txt"
content = load_documents(file_path)

# Split into chunks
chunks = split_document(content)

# Create embeddings for all chunks
embeddings = model.encode(chunks)

print("Embeddings created successfully!")
print(f"Number of chunks: {len(chunks)}")
print(f"Embedding dimension: {embeddings.shape[1]}")

# Define user question
question = "What is machine learning?"

# Create embedding for user question
question_embedding = model.encode(question)

print("Question embedding created successfully!")
print(f"Question: {question}")
print("Question embedding dimension:", len(question_embedding))

# Calculate similarity between the question and each chunk
similarities = cos_sim(question_embedding, embeddings)

print("Similarities:", similarities)

for i, score in enumerate(similarities[0]):
    print(f"Chunk {i + 1}: {score.item():.4f}")

# Find the most relevant chunk
most_relevant_chunk_index = similarities[0].argmax().item()

print(f"Most relevant chunk index: {most_relevant_chunk_index}")
print(f"Most relevant chunk: {chunks[most_relevant_chunk_index]}")

# Create a prompt using the retrieved context
context = chunks[most_relevant_chunk_index]

prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

print("\nPrompt sent to the LLM:")
print(prompt)

# Load the LLM
generator = pipeline("text-generation", model="gpt2")

# Generate an answer
result = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=1
)

# Display the answer
print("\nAnswer from the LLM:")
print(result[0]["generated_text"])

