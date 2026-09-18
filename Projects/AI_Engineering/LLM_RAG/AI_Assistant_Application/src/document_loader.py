from pathlib import Path

def load_documents(file_path):
    """Load a text document and return its content."""
    path = Path(file_path)
    with open(path,'r',encoding='utf-8') as f:
        content= f.read()

    return content


def split_document(document):
    """Split a document into chunks."""
    chunks = document.split("\n")
    return chunks

if __name__=="__main__":

    file_path = "../Data/documents/ai_basics.txt"
    document=load_documents(file_path)
    print("Document loaded successfully!\n") 
    print(document)

    chunks=split_document(document)
    print("Document split into chunks successfully!\n") 
    print(chunks)
