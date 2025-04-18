import psycopg2

conn = psycopg2.connect(
    dbname="tomiriszarylkasyn",  # Имя базы данных
    user="postgres",             # Имя пользователя
    password="123",              # Пароль
    host="localhost",            # Хост
    port="5432"                  # Порт
)

# Создаём курсор
cur = conn.cursor()

# Пример создания таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    );
""")

# Выполняем запрос на добавление данных в таблицу
cur.execute("""
    INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com');
""")

# Подтверждаем изменения
conn.commit()

# Проверяем данные
cur.execute("SELECT * FROM users;")
rows = cur.fetchall()
print("Данные в таблице users:")
for row in rows:
    print(row)

# Закрываем курсор и соединение
cur.close()
conn.close()
