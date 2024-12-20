from sqlmodel import SQLModel, Field
from typing import Optional, List

class BoardGames(SQLModel, table=True):
    bg_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    number_of_players: int
    price: int

class Place(SQLModel, table=True):
    pl_id: Optional[int] = Field(default=None, primary_key=True)
    address: str

class Warehouse(SQLModel, table=True):
    wh_id: Optional[int] = Field(default=None, primary_key=True)
    bg_id: int = Field(foreign_key="boardgames.bg_id")
    quantity: int = Field(default=0)
    pl_id: int = Field(foreign_key="place.pl_id")

class Shop(SQLModel, table=True):
    sh_id: Optional[int] = Field(default=None, primary_key=True)
    pl_id: int = Field(foreign_key="place.pl_id")

class ShopBG(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sh_id: int = Field(foreign_key="shop.sh_id")
    bg_id: int = Field(foreign_key="boardgames.bg_id")
    quantity: int = Field(default=0)

class Worker(SQLModel, table=True):
    w_id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    sh_id: Optional[int] = Field(default=None, foreign_key="shop.sh_id")

class User(SQLModel, table=True):
    us_id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str

class Check(SQLModel, table=True):
    ch_id: Optional[int] = Field(default=None, primary_key=True)
    us_id: int = Field(foreign_key="user.us_id")
    w_id: Optional[int] = Field(default=None, foreign_key="worker.w_id")

class BGCheck(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ch_id: int = Field(foreign_key="check.ch_id")
    bg_id: Optional[int] = Field(default=None, foreign_key="boardgames.bg_id")