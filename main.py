from sqlmodel import create_engine, Session
from sqlalchemy import text
from requests import *
  
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить настольную игру")
        print("2. Добавить место")
        print("3. Добавить склад")
        print("4. Добавить магазин")
        print("5. Добавить работника")
        print("6. Добавить пользователя")
        print("7. Добавить чек")
        print("8. Добавить проверку настольной игры")
        print("9. Показать все настольные игры")
        print("10. Показать все места")
        print("11. Показать все склады")
        print("12. Показать все магазины")
        print("13. Показать всех работников")
        print("14. Показать всех пользователей")
        print("15. Показать все чеки")
        print("16. Показать все проверки настольных игр")
        print("17. Очистка")
        print("18. Выход")

        choice = input("Ваш выбор: ")
        
        if choice == '1':
            add_board_game()
        elif choice == '2':
            add_place()
        elif choice == '3':
            add_warehouse()
        elif choice == '4':
            add_shop()
        elif choice == '5':
            add_worker()
        elif choice == '6':
            add_user()
        elif choice == '7':
            add_check()
        elif choice == '8':
            add_bg_check()
        elif choice == '9':
            display_board_games()
            input()
        elif choice == '10':
            display_places()
            input()
        elif choice == '11':
            display_warehouses()
            input()
        elif choice == '12':
            display_shops()
            input()
        elif choice == '13':
            display_workers()
            input()
        elif choice == '14':
            display_users()
            input()
        elif choice == '15':
            display_checks()
            input()
        elif choice == '16':
            display_bg_checks()
            input()
        elif choice == '17':
            print("Очистка")
            clear_database()
            input()
        elif choice == '18':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()