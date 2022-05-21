import sqlite3


class BotDB:
    def __init__(self, db_file):
        """DB connection initialization"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """User exists query"""
        result = self.cursor.execute("SELECT `id` FROM users where `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Get the user id"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?",  (user_id,))
        return result.fetchone()[0]

    def add_user(self, user_id, user_name):
        """Create the new user"""
        self.cursor.execute("INSERT INTO users (`user_id`,`first_name`) VALUES (?,?)", (user_id, user_name,))
        return self.conn.commit()

    def create_resume(self, user_name):
        """Create a resume for new user"""
        self.cursor.execute("INSERT INTO resume (firs_name) VALUES (?)", (user_name,))
        return self.conn.commit()

    # INSERT INTO resume (firs_name,city,spesiolization,salary,experience,employment,schedule) VALUES (?)

    def update_resume(self, user_name, city, specialization, salary, experience, employment, schedule):
        self.cursor.execute("UPDATE resume SET  city = ?, spesiolization =?, salary = ?, experience = ?, employment = "
                            "?, schedule = ? WHERE first_name = ?", (city, specialization, salary, experience,
                                                                    employment, schedule, user_name))
        return self.conn.commit()

    def get_resume(self, user_name):
        """Get the data of resume table"""
        result = self.cursor.execute("SELECT firs_name, city, spesiolization, salary, experience, employment, schedule FROM `resume` WHERE `firs_name` = ?", (user_name,))
        return bool(len(result.fetchall()))

    def resume_exists(self,user_name):
        result = self.cursor.execute("SELECT `firs_name` FROM resume where `firs_name` = ?", (user_name,))
        return bool(len(result.fetchall()))

    def set_city(self, user_name, city):
        """Set city in my search qwery"""
        result = self.cursor.execute("UPDATE resume SET city = ? WHERE firs_name = ?", (city, user_name,))
        return self.conn.commit()

    def set_spesiolization(self, user_name, spesiolization):
        """Set spesiolization in my search qwery"""
        result = self.cursor.execute("UPDATE resume SET spesiolization = ? WHERE firs_name = ?", (spesiolization, user_name,))
        return self.conn.commit()

    def set_salary(self, user_name, salary):
        """Set salary in my search qwery"""
        result = self.cursor.execute("UPDATE resume SET salary = ? WHERE firs_name = ?", (salary, user_name,))
        return self.conn.commit()

    def set_experience(self, user_name, experience):
        """Set experience in my search qwery"""
        result = self.cursor.execute("UPDATE resume SET experience = ? WHERE firs_name = ?", (experience, user_name,))
        return self.conn.commit()


    def set_employment(self, user_name, employment):
        """Set employment in my search qwery"""
        result = self.cursor.execute("UPDATE resume SET employment = ? WHERE firs_name = ?", (employment, user_name,))
        return self.conn.commit()

    def set_schedule(self, user_name, schedule):
        """Set schedule in my search qwery"""
        result = self.cursor.execute("UPDATE resume SET schedule = ? WHERE firs_name = ?", (schedule, user_name,))
        return self.conn.commit()


    def close(self):
        """Close the connection with DB"""
        self.conn.close()
