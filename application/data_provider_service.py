import pymysql
# from passlib.hash import sha256_crypt


class DataProviderService:
    def __init__(self):
        """
        :creates: a new instance of connection and cursor
        """
        host = 'localhost'
        port = 3306
        user = 'root'
        password = ''
        database = 'person_db'
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
        self.cursor = self.conn.cursor()

    def add_person(self, firstname, lastname):
        sql = """insert into person (firstname, lastname) values (%s, %s)"""
        input_values = (firstname, lastname)
        try:
            self.cursor.execute(sql, input_values)
            self.conn.commit()
        except Exception as exc:
            print(exc)
            self.conn.rollback()
            print("rolled back")
        sql_new_person_id = "select id from person order by id desc limit 1"
        self.cursor.execute(sql_new_person_id)
        new_person = self.cursor.fetchone()
        return new_person[0]

    def get_people(self, person_id=None, limit=None):
        all_people = []
        if person_id is None:
            sql = "SELECT * FROM person order by id desc"
            self.cursor.execute(sql)
            all_people = self.cursor.fetchall()
        else:
            sql = """Select * from person where id = %s"""
            input_values = (person_id,)
            self.cursor.execute(sql, input_values)
            all_people = self.cursor.fetchone()
        return all_people

