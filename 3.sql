-- 1. Создание таблицы, если ещё нет
CREATE TABLE IF NOT EXISTS phonebook1 (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    phone_number VARCHAR(255)
);

-- 2. Вставка тестовых данных
INSERT INTO phonebook1 (username, phone_number)
VALUES
  ('Tomiris', '123456789'),
  ('John Doe', '987654321'),
  ('Alice Smith', '555666777');

-- 3. Функция для поиска по шаблону
CREATE OR REPLACE FUNCTION search_records(pattern TEXT)
RETURNS TABLE(user_id INT, username VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT user_id, username, phone_number
    FROM phonebook1
    WHERE username ILIKE '%' || pattern || '%'
       OR phone_number LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 4. Процедура: вставить нового пользователя или обновить номер
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook1 WHERE username = p_name) THEN
        UPDATE phonebook1
        SET phone_number = p_phone
        WHERE username = p_name;
    ELSE
        INSERT INTO phonebook1 (username, phone_number)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE FUNCTION get_users_paginated(limit_count INT, offset_count INT)
RETURNS TABLE(user_id INT, username TEXT, phone_number TEXT)
LANGUAGE SQL
AS $$
    SELECT user_id, username, phone_number
    FROM phonebook1
    ORDER BY user_id
    LIMIT limit_count OFFSET offset_count;
$$;

