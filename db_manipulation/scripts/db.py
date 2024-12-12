import contextlib
import psycopg2

CONFIG = {
    "database": "supply_department",
    "host": "database.drobot-vlad.com",
    "user": "vlad",
    "password": "drobot",
    "port": "5432"
}


@contextlib.contextmanager
def get_cursor():
    with psycopg2.connect(**CONFIG) as psycopg_conn:
        print("Database connected!")
        with psycopg_conn.cursor() as cursor:
            try:
                yield cursor
                psycopg_conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
                psycopg_conn.rollback()

    print("Database connection closed!")
