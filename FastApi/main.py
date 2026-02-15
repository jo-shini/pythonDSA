from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []


class Item(BaseModel):
    name: str
    description: str


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI"}


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    # return {"ok": True, "item": item}
    print(items)
    return item


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        # print(len(items))
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.put("/items/{items_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    item[item_id] = item
    return item


@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items.pop(item_id)
    return deleted_item


@app.get("/getallItems",)
async def get_all_item():
    if len(items) < 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return items
