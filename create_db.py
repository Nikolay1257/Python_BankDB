import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('bank_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
card_num TEXT PRIMARY KEY,
pin TEXT NOT NULL,
balance INTEGER
)
''')

# Добавляем нового пользователя
cursor.execute('INSERT INTO Users (card_num, pin, balance) VALUES (?, ?, ?)', ('0000', '0000', 1500))
cursor.execute('INSERT INTO Users (card_num, pin, balance) VALUES (?, ?, ?)', ('1111', '1111', 20))
cursor.execute('INSERT INTO Users (card_num, pin, balance) VALUES (?, ?, ?)', ('2222', '2222', 50))

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()