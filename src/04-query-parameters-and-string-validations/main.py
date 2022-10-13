from typing import Union

# query parameters can be constrained using Query
# min_length, max_length, regex, etc.
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Union[str, None] = Query(
        default=None, min_length=3, max_length=50, regex="^fixedquery$"
    )
): # set default value using Query to enforce certain constraints (in this case, length <= 50)
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# if you want a query parameter to be required while using Query, don't set a default value in Query (best option)
# i.e. Query(min_length=3) will constrain the length but the parameter is required

# you can also use explicit declaration that the parameter is required
# i.e. Query(default=...) will make the query parameter required

# you can also use Required from Pydantic
# i.e. Query(default=Required)

# EDGE CASE
# if you want a required query parameter to be able to accept None as well, write as follows
# i.e. q: Union[str, None] = Query(default=...)

# you can define query parameters explicitly with Query() -> get a list of values!
# defaults work the same way as before (provide a default list)

# can add more metadata (title, description, alias)
# alias allows you to rename query parameter so it shows up differently in the URL

# deprecated=True shows the parameter as being deprecated
# include_in_schema=False remove the parameter from the documentation