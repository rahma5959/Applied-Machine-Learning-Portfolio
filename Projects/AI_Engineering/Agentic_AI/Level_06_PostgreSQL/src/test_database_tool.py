import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools import database_tool 

result=database_tool.get_document.invoke({})
print(result)

