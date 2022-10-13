"""The first step for FastAPI."""

from enum import Enum
from typing import Dict

from fastapi import FastAPI


class ModelName(str, Enum):
    """Model naems."""

    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"


app = FastAPI()


@app.get("/")  # request to the URL "/" using a GET operation
async def root() -> Dict[str, str]:  # this runs asynchronously
    """Return a simple JSON response."""
    return {"message": "Hello FastAPI!"}  # return the content


@app.get("/items/{item_id}")
async def read_item(item_id: str) -> Dict[str, str]:
    """Read the item and return it."""
    return {"item_id": item_id}


@app.get("/items/foo")  # order matters. this doesn't run
async def read_item_foo() -> Dict[str, str]:
    """Return foo."""
    return {"item_id": "the item name is foo"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) -> Dict[str, str]:
    """Get model name."""
    if model_name == ModelName.ALEXNET:
        message = "Deep Learning FTW!"
    elif model_name == ModelName.LENET:
        message = "LeCNN all the images"
    else:
        message = "Have some residuals"
    return {"model_name": model_name, "message": message}


# :path tells it that the parameter should match any path.
# You could need the parameter to contain /home/john/file.txt,
# with a leading slash (/).
# In that case, the URL would be: /files//home/john/file.txt,
# with a double slash (//) between files and home.
@app.get("/files/{file_path:path}")
async def read_file(file_path: str) -> Dict[str, str]:
    """Pass file path."""
    return {"file_path": file_path}