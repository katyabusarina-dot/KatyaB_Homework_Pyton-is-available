from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pytest


db_connection_string = "postgresql://postgres:123@localhost:5432/postgres"
new_email = 'raj@yandex.ru'

@pytest.fixture
def db():
    engine = create_engine(db_connection_string)
    # уборка до теста — гарантирует повторяемость запуска
    with engine.begin() as conn:
        conn.execute(
            text("delete from teacher where email = :email"),
            {"email": new_email},
        )
    yield engine
    # уборка после теста — тест «удаляет за собой»
    with engine.begin() as conn:
        conn.execute(
            text("delete from teacher where email = :email"),
            {"email": new_email},
        )

    engine.dispose()
    

def test_insert(db):
    sql = text("insert into teacher (email) values (:new_email)")
    rows = db.execute(sql, new_email = 'raj@yandex.ru')


def test_update(db):
    sql = text("update teacher set teacher_id = :t_id, group_id = :g_id where email = :email")
    rows = db.execute(sql, t_id = '35000', g_id = '500', email = 'raj@yandex.ru')


def test_delete(db):
    sql = text ("delete from teacher where email = :email")
    rows = db.execute(sql, email = 'raj@yandex.ru')