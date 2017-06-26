import logging
from pprint import pformat

import psycopg2

log = logging.getLogger(__name__)


conn = psycopg2.connect(dbname='learnwords_db', user='learnwords', host='192.168.1.64', password='learnwords')
conn.autocommit = True

log.info("Connection with database established: {}".format(conn))
cur = conn.cursor()
cur.execute('SELECT version()')
ver = cur.fetchone()
log.info("Using version: {}".format(ver))


def get_headers():
    cur.execute("SELECT column_name FROM information_schema.columns where table_name='words'")
    response = cur.fetchall()
    log.debug("headers: {}".format(response))
    return response


def get_words_by_user(username):
    cur.execute("SELECT * FROM words WHERE username=%s", (username,))
    response = cur.fetchall()
    log.info("words for user: \n{}".format(pformat(response)))
    return response


if __name__ == '__main__':
    get_words_by_user("julia_vikulina")
