import index as p

def menu():
    # Меню системы
    print(f"{'Код':<5} | {'Действие в системе'}")
    print("-" * 32)
    print(f"{'1':<5} | Получить JSON-файл")
    print(f"{'2':<5} | Поговорить с ИИ")
    print(f"{'3':<5} | Связь с автором")

    while(True):     
        try:
            a = int(input(">>> "))
            if a==1:
                print(1)
                p.jsonc()
                break
            elif a==2:
                print(2)
                p.ai()
                break
            elif a==3:
                print("Наши контакты:\n @imyrj - TG\n kievsky332 - github")
                
            else:
                print("От 1 до 3!")
        except Exception as e:
            print(f"Ошибка! {e}")
menu()
    