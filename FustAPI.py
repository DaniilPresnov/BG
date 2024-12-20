from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, create_engine, Session, select
from models import BoardGames, Place, Warehouse, Shop, Worker, User, Check, BGCheck

DATABASE_URL = "postgresql://postgres:1234@127.0.0.1:5432/postgres"
engine = create_engine(DATABASE_URL)

app = FastAPI()

# Создание таблиц, если они не существуют
SQLModel.metadata.create_all(engine)

@app.post("/boardgames/", response_model=BoardGames)
def create_board_game(board_game: BoardGames):
    with Session(engine) as session:
        session.add(board_game)
        session.commit()
        session.refresh(board_game)
    return board_game

@app.get("/boardgames/", response_model=list[BoardGames])
def read_board_games():
    with Session(engine) as session:
        statement = select(BoardGames)
        results = session.exec(statement).all()
    return results

@app.post("/places/", response_model=Place)
def create_place(place: Place):
    with Session(engine) as session:
        session.add(place)
        session.commit()
        session.refresh(place)
    return place

@app.get("/places/", response_model=list[Place])
def read_places():
    with Session(engine) as session:
        statement = select(Place)
        results = session.exec(statement).all()
    return results

# Аналогично добавьте другие эндпоинты для Warehouse, Shop, Worker, User, Check, BGCheck

@app.delete("/boardgames/{board_game_id}", response_model=BoardGames)
def delete_board_game(board_game_id: int):
    with Session(engine) as session:
        board_game = session.get(BoardGames, board_game_id)
        if not board_game:
            raise HTTPException(status_code=404, detail="Board game not found")
        session.delete(board_game)
        session.commit()
    return board_game