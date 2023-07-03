from typing import Union
from fastapi import FastAPI
import uvicorn
from uce.ia.openiatest import Document, inference

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return {
        'inference': response[0],
        'usage': response[1]
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
