import logging
from pprint import pformat

import psycopg2

from app.config.config import read_config

log = logging.getLogger(__name__)


cur = None


def connect_db():
    cfg = read_config('db')
    name = cfg['name']
    user = cfg['user']
    host = cfg['host']
    password = cfg['passwd']
    conn = psycopg2.connect(dbname=name, user=user, host=host, password=password)
    conn.autocommit = True

    log.debug("Connection with database established: {}".format(conn))
    global cur
    cur = conn.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    log.debug("Using version: {}".format(ver))


def get_headers():
    cur.execute("SELECT column_name FROM information_schema.columns where table_name='words'")
    response = cur.fetchall()
    log.debug("headers: {}".format(response))
    return response


def get_words_by_user(username):
    cur.execute("SELECT * FROM words WHERE username=%s", (username,))
    response = cur.fetchall()
    log.info("len of words for user: {}".format(len(response)))
    return response


if __name__ == '__main__':
    get_words_by_user("julia_vikulina")
