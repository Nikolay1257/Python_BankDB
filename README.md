- Пример установки на debian 12

- обновите репозиторий
  - $ apt-get update

-  Установите гит
  -  $ apt install git

- Установите sqlite3
  -  $ apt install sqlite3 

- Графичиская среда для управления sqlite3
- apt install sqlitebrowser
;

2. Клонируем репозиторий
git clone https://github.com/Nikolay1257/Python_BankDB.git

cd Python_BankDB

4. Миграция базы данных (создание таблиц)

python3 create_db.py

3. Запуск кода 
