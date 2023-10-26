"""
    1. Używając requests/httpx/aiohttp pobierz dane z dowolnej strony ASYNCHRONICZNIE i wyswietl dla "/"
    2. Stwórz globalny słownik lub podepnij bazę danych i pozwól na dodawanie/usuwanie/edycje Item'ow
    3. Dodaj dekorator do endpointu "/" który będzie zliczał ilość wywołań
    More info: https://fastapi.tiangolo.com/#example
"""
import os
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

print(os.environ.get("ENV_EXAMPLE"))
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
