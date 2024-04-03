import sqlite3

connection = sqlite3.connect('bank_database.db')
cursor = connection.cursor()

#========================================================================================================================
#ФУНЦИИ ПОЛЬЗОВАТЕЛЕЙ
#========================================================================================================================
# Авторизация пользователей

def authorizacion():
    while True:
        user_num = input("введите номер карты: ")
        cursor.execute('SELECT card_num FROM Users WHERE card_num = ?', (user_num,))
        results = cursor.fetchone()
        if results:
            card_pin = input("введите PIN-код: ")
            if card_pin == results[0]:
                print("\nДобро пожаловать в банк!")
                return card_pin
                break
            else:
                print("Неверный PIN-код. Попробуйте снова.")
        else:
            print("пользователь не найден попробуйте снова ")

# Баланс пользователя
def balance_card(input_card_num):
    cursor.execute("SELECT balance FROM Users WHERE card_num = ?",
                   (input_card_num, ))
    result = cursor.fetchone()
    if result is None:
        print("Нету такой карты")
        return
    if len(result) != 0:
        print("\nНа вашем счету " + str(result[0]) + "$")

# Пополнение
def replenish(input_balance):
    input_balance = int(input_balance)
    if input_balance >= 0 and input_balance < 10001:
        cursor.execute('UPDATE Users SET balance = balance + ? WHERE card_num = ?', (int(input_balance), users,))
        print("\nваш счет пополнен на: " + str(input_balance) + "$")
    else:
        print("\nизвените нельзя пополнить на сумму свыше 10 000$, обратитесь в банк")

# Снятие средств
def takeoff(balance):
    if int(balance) <=0:
        print("Ошибка пополнения")
    else:
        cursor.execute('UPDATE Users SET balance = balance - ? WHERE card_num = ?', (int(balance), users,))
        print("\nс вашего счета снято: " + balance + "$")

# Отобразить всех пользователейы
def card(number):
    cursor.execute('SELECT * FROM Users WHERE card_num = ?', (number,))
    results = cursor.fetchall()

    for res in results:
        print(res)


#========================================================================================================================
#ФУНЦИИ АДМИНА
#========================================================================================================================

# Баланс админа
def balance_card_admin(input_card_num):
    cursor.execute("SELECT balance FROM Users WHERE card_num = ?",
                   (input_card_num, ))
    result = cursor.fetchone()
    if result:
        print("\nНа карте " + input_card_num + " баланс " + str(result[0]) + "$\n")
    else:
        print("нету такой карты\n")

# Пополнение 
def replenish_admin(num):
     cursor.execute('SELECT card_num FROM Users WHERE card_num = ?', (num,))
     results = cursor.fetchall()
     if results:
         x = input("введите сумму пополнения: ")
         if int(x) >=0:
             cursor.execute('UPDATE Users SET balance = balance + ? WHERE card_num = ?', (int(x), num,))
             connection.commit()
             print("\nваш счет пополнен на: " + x + "$\n")
         else:
            print("извените нельзя пополнить, введите другую сумму\n")
     else:
         print("\nпользователь не найден\n")


# Снятие
def takeoff_admin(num):
     cursor.execute('SELECT card_num FROM Users WHERE card_num = ?', (num,))
     results = cursor.fetchall()
     if results:
         x = input("введите сумму для снятия: ")
         if int(x) >=0:
             cursor.execute('UPDATE Users SET balance = balance - ? WHERE card_num = ?', (int(x), num,))
             connection.commit()
             print("\nс вашего счета снято: " + x + "$\n")
         else:
            print("\nизвените нельзя снять, введите другую сумму\n")
     else:
         print("\nпользователь не найден\n")

# Перевод между пользователями
def money_transaction(card_minus):
    cursor.execute("SELECT balance FROM Users WHERE card_num = ?",(card_minus, ))
    results = cursor.fetchone()
    if results:
         print("\nНа карте " + card_minus + " баланс " + str(results[0]) + "$\n")
         x = int(input("введите сумму для списания: "))
         if x > 0:
             cursor.execute('UPDATE Users SET balance = balance - ? WHERE card_num = ?', (x, card_minus))
             connection.commit()
             print("со счета снято: " + str(x)+ "$\n")

             m = input("введите карту для перевода: ")
             cursor.execute("SELECT balance FROM Users WHERE card_num = ?",(m, ))
             results = cursor.fetchone()
             if results:
                 cursor.execute('UPDATE Users SET balance = balance + ? WHERE card_num = ?', (x, m))
                 connection.commit()
                 print("\nУспешно переведено пользователю " + m + " " + "сумма " + str(x) + "$\n")
             else:
                 print("Данного пользователя нету\n")
         else:
             print("\nНельзя пополнить на такую сумму, обратитесь в банк\n")
    else:
        print("Даннного пользователя нету\n")

users = authorizacion()


#Вызов меню АДМИНА
#========================================================================================================================
if users == "0000":
    print("\nДобро пожаловать в админ панель\n")
    while True:
        print("1 - баланс пользователя")
        print("2 - пополнить счет")
        print("3 - снять средства пользователя")
        print("4 - перевести другому пользователю")
        print("5 - показать всех пользователей в системе и их баланс")
        print("6 - завершить работу")

        enter = input("введите номер: ")

        if enter == "1":
            a = input("введите номер карты: ")
            balance_card_admin(a)
        elif enter == "2":
            b = input("введите номер карты: ")
            replenish_admin(b)
        elif enter == "3":
            u = input("введите номер карты: ")
            takeoff_admin(u)
        elif enter == "4":
            d = input("введите карту для списания: ")
            money_transaction(d)
        elif enter == "5":
            cursor.execute('SELECT * FROM Users')
            users = cursor.fetchall()

            for res in users:
                print("\nПользователь: " + (res[0]))
                print("Баланс: " + str(res[2]) + "$")
        elif enter == "6":
            break
        else:
            print("\nДанного пункта нету, выберите другой\n")

#Вызов меню ПОЛЬЗОВАТЕЛЯ!
#========================================================================================================================
else:
    while True:
        print("\n1 - Баланс пользователя")
        print("2 - пополнить счет")
        print("3 - снять со счета")
        print("4 - завершить работу")

        a = input("выберите действие: ")

        if a == "1": 
            balance_card(users)

        elif a == "2":
            c = input("введите сумму для пополнения: ")
            replenish(c)
        elif a == "3":
            b = input("введите сумму для снятия: ")
            takeoff(b)
        elif a == "4":
            print("\nСпасибо за обращение, всего доброго!\n")
            break
        else:
            print("неверный ввод ")
            enter = input(c)




connection.commit()
connection.close()
