from sqlmodel import Session, select
from models import BoardGames, Place, Warehouse, Shop, Worker, User, Check, BGCheck
from sqlalchemy import text,create_engine

DATABASE_URL = "postgresql://postgres:1234@127.0.0.1:5432/postgres"
engine = create_engine(DATABASE_URL)

# Функции для выборки данных
def get_all_board_games():
    with Session(engine) as session:
        statement = select(BoardGames)
        results = session.exec(statement).all()
        return results

def get_all_places():
    with Session(engine) as session:
        statement = select(Place)
        results = session.exec(statement).all()
        return results

def get_all_warehouses():
    with Session(engine) as session:
        statement = select(Warehouse)
        results = session.exec(statement).all()
        return results

def get_all_shops():
    with Session(engine) as session:
        statement = select(Shop)
        results = session.exec(statement).all()
        return results

def get_all_workers():
    with Session(engine) as session:
        statement = select(Worker)
        results = session.exec(statement).all()
        return results

def get_all_users():
    with Session(engine) as session:
        statement = select(User)
        results = session.exec(statement).all()
        return results

def get_all_checks():
    with Session(engine) as session:
        statement = select(Check)
        results = session.exec(statement).all()
        return results

def get_all_bg_checks():
    with Session(engine) as session:
        statement = select(BGCheck)
        results = session.exec(statement).all()
        return results

# Функции для добавления данных
def add_board_game():
    name = input("Введите название игры: ")
    number_of_players = int(input("Введите количество игроков: "))
    price = int(input("Введите цену: "))
    board_game = BoardGames(name=name, number_of_players=number_of_players, price=price)
    with Session(engine) as session:
        session.add(board_game)
        session.commit()
        session.refresh(board_game)
    print(f"Добавлена игра: {board_game.name}")

def add_place():
    address = input("Введите адрес: ")
    place = Place(address=address)
    with Session(engine) as session:
        session.add(place)
        session.commit()
        session.refresh(place)
    print(f"Добавлено место: {place.address}")

def add_warehouse():
    bg_id = int(input("Введите ID настольной игры: "))
    quantity = int(input("Введите количество: "))
    pl_id = int(input("Введите ID места: "))
    warehouse = Warehouse(bg_id=bg_id, quantity=quantity, pl_id=pl_id)
    with Session(engine) as session:
        session.add(warehouse)
        session.commit()
        session.refresh(warehouse)
    print(f"Добавлен склад: ID игры {warehouse.bg_id}, Количество {warehouse.quantity}")

def add_shop():
    pl_id = int(input("Введите ID места: "))
    shop = Shop(pl_id=pl_id)
    with Session(engine) as session:
        session.add(shop)
        session.commit()
        session.refresh(shop)
    print(f"Добавлен магазин: ID места {shop.pl_id}")

def add_worker():
    full_name = input("Введите ФИО работника: ")
    sh_id = int(input("Введите ID магазина (или оставьте пустым): ") or 0)
    worker = Worker(full_name=full_name, sh_id=sh_id if sh_id else None)
    with Session(engine) as session:
        session.add(worker)
        session.commit()
        session.refresh(worker)
    print(f"Добавлен работник: {worker.full_name}")

def add_user():
    full_name = input("Введите ФИО пользователя: ")
    user = User(full_name=full_name)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    print(f"Добавлен пользователь: {user.full_name}")

def add_check():
    us_id = int(input("Введите ID пользователя: "))
    w_id = int(input("Введите ID работника (или оставьте пустым): ") or 0)
    check = Check(us_id=us_id, w_id=w_id if w_id else None)
    with Session(engine) as session:
        session.add(check)
        session.commit()
        session.refresh(check)
    print(f"Добавлен чек: ID пользователя {check.us_id}")

def add_bg_check():
    ch_id = int(input("Введите ID чека: "))
    bg_id = int(input("Введите ID настольной игры (или оставьте пустым): ") or 0)
    bg_check = BGCheck(ch_id=ch_id, bg_id=bg_id if bg_id else None)
    with Session(engine) as session:
        session.add(bg_check)
        session.commit()
        session.refresh(bg_check)
    print(f"Добавлена проверка настольной игры: ID чека {bg_check.ch_id}")

# Функции для вывода данных
def display_board_games():
    board_games = get_all_board_games()
    print("Список настольных игр:")
    for game in board_games:
        print(f"ID: {game.bg_id}, Название: {game.name}, Игроки: {game.number_of_players}, Цена: {game.price}")

def display_places():
    places = get_all_places()
    print("Список мест:")
    for place in places:
        print(f"ID: {place.pl_id}, Адрес: {place.address}")

def display_warehouses():
    warehouses = get_all_warehouses()
    print("Список складов:")
    for warehouse in warehouses:
        print(f"ID: {warehouse.wh_id}, ID Игры: {warehouse.bg_id}, Количество: {warehouse.quantity}, ID Места: {warehouse.pl_id}")

def display_shops():
    shops = get_all_shops()
    print("Список магазинов:")
    for shop in shops:
        print(f"ID: {shop.sh_id}, ID Места: {shop.pl_id}")

def display_workers():
    workers = get_all_workers()
    print("Список работников:")
    for worker in workers:
        print(f"ID: {worker.w_id}, ФИО: {worker.full_name}, ID Магазина: {worker.sh_id}")

def display_users():
    users = get_all_users()
    print("Список пользователей:")
    for user in users:
        print(f"ID: {user.us_id}, ФИО: {user.full_name}")

def display_checks():
    checks = get_all_checks()
    print("Список чеков:")
    for check in checks:
        print(f"ID: {check.ch_id}, ID Пользователя: {check.us_id}, ID Работника: {check.w_id}")

def display_bg_checks():
    bg_checks = get_all_bg_checks()
    print("Список проверок настольных игр:")
    for bg_check in bg_checks:
        print(f"ID: {bg_check.id}, ID Чека: {bg_check.ch_id}, ID Игры: {bg_check.bg_id}")
        
# Функция для очистки базы данных
def clear_database():
    with Session(engine) as session:
        session.execute(text("TRUNCATE TABLE boardgames, place, warehouse, shop, shopbg, worker, \"user\", \"check\", bg_check CASCADE;"))
        session.commit()
    print("База данных очищена.")
