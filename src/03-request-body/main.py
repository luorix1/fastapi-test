# sending info to the API will usually involve "pydantic"
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel): # declare a model that inherits from BaseModel (will become a JSON object or Python dict)
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/") # our first POST operation
async def create_item(item: Item): # declare it the same way as path or query parameter (specify type as the correct model)
    item_dict = item.dict()
    if item.tax: # you can directly access all attributes of the model object if it is passed as a parameter to the function
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}") # our first PUT operation
async def create_item(item_id: int, item: Item, q: Union[str, None] = None): # you can declare body, path, query parameters at once (path: declared in path, query: declared as a singular type, body: declared as a Pydantic model)
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result