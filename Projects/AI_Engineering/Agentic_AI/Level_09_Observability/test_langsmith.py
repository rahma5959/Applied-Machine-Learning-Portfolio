
import os
from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

api_key = os.getenv("LANGSMITH_API_KEY")

if not api_key:
    raise ValueError("LANGSMITH_API_KEY is missing from .env")

client = Client(api_key=api_key)

try:
    projects = list(client.list_projects(limit=1))
    print("LangSmith connection successful!")
    print(f"Projects retrieved: {len(projects)}")
except Exception:
    print("LangSmith connection failed. Check your API key and network.")
    raise
