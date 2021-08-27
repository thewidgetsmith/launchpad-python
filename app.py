from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return app.send_static_file("index.html")


@app.route("/db_test/<username>", methods=["GET"])
def db_test(username):
    import cx_Oracle
    conn = cx_Oracle.connect(dsn=os.environ.get("ORACLE_DB_URL"),
                             user=os.environ.get("ORACLE_DB_USER"),
                             password=os.environ.get("ORACLE_DB_PASS"),
                             encoding="UTF-8",
                             nencoding="UTF-8")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            spriden_pidm
        FROM
            spriden
        WHERE spriden_change_ind IS null
            AND spriden_id = :uname
    """, uname=username)
    rows = cursor.fetchall()

    return {
        "username": username,
        "pidm": rows[0][0]
    }


@app.route("/env_test", methods=["GET"])
def env_test():
    test_val = os.environ.get(
        "ENV_TEST_VALUE", "The environment test value failed to load")
    return {
        "test_val": test_val
    }

# Runnable code snippets. #### --------------------------------------------------------------------------------------

# Highlight the code below, right-click, select 'Run Code' from the context menu.


def roll_the_dice():
    from random import randint
    print("Rolled: {}".format(randint(1, 6)))


roll_the_dice()
