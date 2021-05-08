# Сделать проверку в базе данных. Если номер телефона есть в файле - добавлять его в базу данных с пометкой True. Если в базе данных нет, добавлять с пометкой False. Дальнейшие действия проводить при наличии в базе данных True

import sqlite3


class Database:
    '''База данных'''

    def __init__(self, path_to_db):
        self.path_to_db = path_to_db

    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):

        if not parameters:
            parameters = ()

        connection = self.connection()
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()

        connection.close()
        return data


    def exc(self, sql: str, fetchone=False, fetchall=False, commit=False):

        connection = self.connection()
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()

        connection.close()
        return data

    def all_id_users(self):
        sql = """SELECT id FROM Course_students"""
        return self.execute(sql, fetchall=True)


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f'{item} = ?' for item in parameters
        ])

    def select_all(self):
        sql = """SELECT * FROM course_students"""
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = """SELECT * FROM course_students WHERE """
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)


    def all_phone(self, **kwargs):
        sql = """SELECT phone FROM course_students"""
        return self.exc(sql, fetchall=True)

    def update_user_id(self, id, phone):
        sql = f"""
        UPDATE course_students SET id=? WHERE phone=?
        """
        return self.execute(sql, parameters=(id, phone), commit=True)

    def check_tariff_plan(self, id):
        sql = f"""
        SELECT tariff_plan FROM course_students WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)

    def delete_user(self):
        pass



def logger(statement):
    print(f"""Executing:{statement}\n""")
