from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pytest


db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"


@pytest.fixture
def db():
    """Создаёт движок и соединение, после теста закрывает соединение."""
    engine = create_engine(db_connection_string)
    connection = engine.connect()
    transaction = connection.begin()
    yield connection
    transaction.rollback()   # ← вот очистка: любые изменения теста отменяются
    connection.close()
    engine.dispose()


def test_insert(db):
    sql = text("insert into teacher (email) values (:new_email)")
    result = db.execute(sql, new_email='raj@yandex.ru')
    assert result.rowcount == 1  # "Должна быть вставлена ровно одна строка"
    check_res = db.execute(
        text("SELECT email FROM teacher WHERE email = :email"),
        {"email": "raj@yandex.ru"},
    )
    # Проверяем, что данные действительно добавлены
    row = check_res.mappings().first()
    assert row is not None, "Запись не найдена в таблице"
    assert row["email"] == "raj@yandex.ru"


def test_update(db):
    sql = text("update teacher set teacher_id = :t_id,"
               "group_id = :g_id where email = :email")
    result = db.execute(sql, t_id='35000', g_id='500', email='raj@yandex.ru')
    assert result.rowcount == 1, "Обновлена ровно одна запись"
    row = db.execute(
        text("SELECT teacher_id, group_id FROM teacher WHERE email = :email"),
        {"email": "raj@yandex.ru"},
      ).mappings().first()
    assert row is not None
    assert row["teacher_id"] == 35000 and row["group_id"] == 500


def test_delete(db):
    sql = text("delete from teacher where email = :email")
    rows = db.execute(sql, email='raj@yandex.ru')
    assert rows.rowcount == 1, "Удалена ровно одна запись"
