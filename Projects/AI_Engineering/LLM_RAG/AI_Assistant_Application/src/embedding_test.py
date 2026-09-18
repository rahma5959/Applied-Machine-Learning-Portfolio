from sentence_transformers import SentenceTransformer

#load embedding model
model= SentenceTransformer("all-MiniLM-L6-v2")

# Text to encode 
text = "Artificial intelligence is a field of computer science."


# Create the embedding
embedding = model.encode(text)
print("Embedding created successfully!")
print("Embedding size:", len(embedding))
print("First values:", embedding[:5])