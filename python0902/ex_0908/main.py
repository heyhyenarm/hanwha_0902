from fastapi import FastAPI
from enum import Enum

class ModelNmae(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q":q}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# API
# http://127.0.0.1:8000/models/{model_name}
@app.get("/models/{model_name}")
async def get_model(model_name: ModelNmae):
    # 키를 요청
    if model_name is ModelNmae.alexnet:
        return {"model_name": model_name, "message": "키 요청: Deep Learning FTW!"}
    # 값을 요청
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "값 요청: LeCNN all the images"}
    # 그 외 상황
    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# 쿼리 매개변수
# http://127.0.0.1:8000/items2/
# http://127.0.0.1:8000/items2/?skip=n&limit=m
@app.get("/items2/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]   # 범위 연산자 list[n부터:m번째까지]

# 선택적 매개변수
# http://127.0.0.1:8000/items2/{item_id}
# http://127.0.0.1:8000/items2/{item_id}?q={q}
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
