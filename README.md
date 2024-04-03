# Пример установки на debian 12

- обновите репозиторий
  - $ apt-get update

- Установите гит
  - $ apt install git

- Установите sqlite3
  - $ apt install sqlite3 

- Графичиская среда для управления sqlite3
  - apt install sqlitebrowser



(Примечание: Во избежание ошибок прав доступа выполняйте копирование от имени пользователя а не root)


- Клонируем репозиторий
  - $ git clone https://github.com/Nikolay1257/Python_BankDB.git
  
- Заходим в проект
  - $ cd Python_BankDB

- Миграция базы данных (создание таблиц)
  - $ python3 create_db.py

- Запуск кода
  - $ python3 bank.py
   
