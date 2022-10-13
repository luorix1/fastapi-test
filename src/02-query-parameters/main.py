from typing import Union

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/") # http://127.0.0.1:8000/items/?skip=0&limit=10 would yield skip=0, limit=10 (default type is string)
async def read_item(skip: int = 0, limit: int = 10): # defining query parameters as a certain type will convert to the specified type
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}") # by specifying a default value of None, you can make query parameters optional (if not set, it is required)
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False): # you can also make parameters boolean
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}") # you can declare path and query parameters at the same time
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item