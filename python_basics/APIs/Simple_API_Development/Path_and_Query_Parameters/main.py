from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = Query(None, max_length=50)):
    return {"item_id": item_id, "q": q}
