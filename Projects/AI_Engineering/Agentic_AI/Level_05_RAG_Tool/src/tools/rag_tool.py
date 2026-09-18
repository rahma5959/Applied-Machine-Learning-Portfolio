from pathlib import Path
from langchain_core.tools import tool
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


def load_document():
    file_path = Path(__file__).resolve().parents[2] / "Data" / "documents" / "ai_basics.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content


def split_document(content):
    chunks = content.split("\n")
    
    return [chunk.strip() for chunk in chunks if chunk.strip()]




# Load document
content = load_document()

# Split document
chunks = split_document(content)

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
chunk_embeddings = embedding_model.encode(chunks)

@tool
def retrieve_context(question:str) -> str:
    """Retrieve the most relevant information from the knowledge documents."""

    #question embedding
    question_embedding= embedding_model.encode(question)

    #Similarity
    similarities = cos_sim(question_embedding, chunk_embeddings)

    #find the most relevent chunk 
    most_relevant_index=similarities[0].argmax().item()
    print("Most relevant index:", most_relevant_index)

    #retrieve the most relevant chunk
    most_relevant_chunk=chunks[most_relevant_index]
    
    return most_relevant_chunk

# Test
question = "What is machine learning?"
context = retrieve_context.invoke({
    "question": question
})

print("Question:", question)
print("\nRetrieved context:")
print(context)
