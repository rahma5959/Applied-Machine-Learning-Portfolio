
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim
from document_loader import load_documents, split_document
from transformers import pipeline


# Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# Load the documents
file_path = "../Data/documents/ai_basics.txt"
content = load_documents(file_path)

# Split the document into chunks
chunks = split_document(content)

# Create embeddings for all chunks
chunk_embeddings = embedding_model.encode(chunks)


# Load the LLM
generator = pipeline("text-generation", model="gpt2")


def answer_question(question):
    """Retrieve the most relevant chunk and generate an answer."""

    # Create an embedding for the question
    question_embedding = embedding_model.encode(question)

    # Calculate similarity between the question and chunks
    similarities = cos_sim(question_embedding, chunk_embeddings)

    # Find the most relevant chunk
    most_relevant_chunk_index = similarities[0].argmax().item()

    # Retrieve the relevant context
    context = chunks[most_relevant_chunk_index]

    # Create the prompt
    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    # Generate the answer
    result = generator(
        prompt,
        max_new_tokens=50,
        num_return_sequences=1
    )
    # Get only the generated text after "Answer:"
    generated_text = result[0]["generated_text"]
    answer = generated_text.split("Answer:", 1)[-1].strip()
    return answer

if __name__ == "__main__":
    question = "What is machine learning?"

    answer = answer_question(question)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)

