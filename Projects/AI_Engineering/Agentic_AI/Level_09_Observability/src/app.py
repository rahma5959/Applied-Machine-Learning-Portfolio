from fastapi import FastAPI
import uuid
import time
import logging
from prometheus_fastapi_instrumentator import Instrumentator

app=FastAPI()

Instrumentator().instrument(app).expose(app)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a"
)

logger=logging.getLogger(__name__)

@app.get("/")
def home():

    start_time=time.time()
    logger.info("Home endpoint called")

    response= {
        "message": "AI Agent Observability API is running"
    }

    execution_time=time.time()-start_time

    logger.info(
        f"Home endpoint completed in {execution_time:.4f} seconds"
    )

    return response

@app.get("/error")
def test_error():
    logger.info("Error test endpoint started")

    try:
        result=10/0
        return{"result":result}
    
    except Exception as error:
        logger.error(f"An error occurred: {error}")
        return{
            "error": "An internal error occurred"
        }

   

@app.middleware("http")
async def log_requests(request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()

    logger.info(
        f"Request started | id={request_id} "
        f"| method={request.method} | path={request.url.path}"
    )

    try:
        response = await call_next(request)

        execution_time = time.time() - start_time

        logger.info(
            f"Request completed | id={request_id} "
            f"| status={response.status_code} "
            f"| time={execution_time:.4f}s"
        )

        return response

    except Exception:
        execution_time = time.time() - start_time

        logger.exception(
            f"Request failed | id={request_id} "
            f"| time={execution_time:.4f}s"
        )

        raise
