from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

class ItemInfo(str, Enum):
    apple = "사과"
    boiled_egg = "삶은 계란"
    meat = "고기"

class Game(BaseModel):
    name: str
    price: float

games_db = {
    1: {"name": "maplestory", "price": 0},
    2: {"name": "DavetheDiver", "price": 25000},
}

app = FastAPI()

# get 복습
@app.get("/")
async def root():
    return {"message": "login"}

@app.get("/games/items/{item_id}")
async def read_item(item_id: int):
    if item_id is 1:
        return {"item_id": item_id, "message": ItemInfo.apple.value}
    if item_id is 2:
        return {"item_id": item_id, "message": ItemInfo.boiled_egg.value}
    if item_id is 3:
        return {"item_id": item_id, "message": ItemInfo.meat.value}
    return {"No Item"}

# Read_전체 조회
@app.get("/games/")
async def read_games():
    return games_db

# Read_개별 조회
@app.get("/games/{game_name}")
async def read_game_by_name(game_name: str):
    return {"game_name": game_name}

# Create_생성
# post 배움, 프론트 기능이 없어 Swagger UI로 post 테스트.
@app.post("/games/")
async def create_game(game: Game):
    # 전달받은 데이터 처리
    new_id = len(games_db) + 1
    # pydantic에서는 dict 대신 model_dump 사용
    games_db[new_id] = game.model_dump()
    return {
        "message": "post game success.", 
        "game_name": game.name, 
        "game_price": game.price,
        "in games_db": games_db[new_id]
        }

# {
#   "message": "post game success.",
#   "game_name": "test2",
#   "game_price": 0,
#   "in games_db": {
#     "name": "test2",
#     "price": 0
#   }
# }

# Update_ 수정
# put 예제(update)
@app.put("/games/{game_id}")
async def update_game(game_id: int, game: Game):
    # 게임 존재 여부 확인
    if game_id not in games_db:
        return HTTPException(status_code=404, detail="해당 게임을 찾을 수 없습니다. ")
    
    # 데이터 업데이트
    games_db[game_id] = game.model_dump()
    return {
        "message": f"game id: {game_id} update success",
        "update_game": games_db[game_id]
    }

# Delete 삭제
# delete 예제
@app.delete("/games/{game_id}")
async def delete_game(game_id: int):
    # 게임이 존재 여부 확인
    if game_id not in games_db:
        raise HTTPException(status_code=404, detail="해당 게임을 찾을 수 없습니다. ")
    
    # 데이터 삭제 처리
    delete_game = games_db.pop(game_id)

    return {
        "message": f"game id: {game_id} delete success",
        "deleted_game": delete_game
    }

# CRUD란?
# Create
# Read
# Update
# Delete