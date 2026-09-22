from tools.database_tool import get_documents

def test_document():
    result = get_documents.invoke({})
    assert len(result) > 0