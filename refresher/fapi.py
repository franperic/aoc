from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    price: float
    description: str | None = None


@app.get("/")
def hello_world():
    return {"message": "I am up and running!"}


@app.post("/items/{item_id}")
def get_item(item_id: int, item: Item):
    return {item_id: f"Here is your item {item_id}", item.id: item}
