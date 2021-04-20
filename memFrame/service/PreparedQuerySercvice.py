import os

import psycopg2

from config import settings


class PreparedQueryService:
    def __init__(self):
        pass

    # preparedStatementを実行する
    def execute_prepared_statement(self, query, *args):
        # 結果変数
        result = None
        # DBと接続
        dbname = os.environ.get('DATABASE_URL')
        with psycopg2.connect(dbname) as conn:
            try:
                with conn.cursor() as cur:
                    try:
                        # クエリを設定
                        cur.execute(query)
                        cur.execute(query, args)
                        # 　結果を返却
                        result = cur.fetchall()
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
        return result

    # preparedStatementを実行する
    def execute_prepared_statement(self, query, **kwargs):

        #結果変数
        result = None
        # DBと接続
        dbname = os.environ.get('DATABASE_URL')
        with psycopg2.connect(dbname) as conn:
            try:
                with conn.cursor() as cur:
                    try:
                        # クエリを設定
                        cur.execute(query, kwargs)
                        # 　結果を返却
                        result = cur.fetchall()
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)

        return result