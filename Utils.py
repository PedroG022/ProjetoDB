from os import system
import sqlite3
import subprocess

from models.User import User


class Menu():
    # Prints a card
    def card(text, clear=False):
        if clear:
            system("clear")

        args = ["gum", "style", "--border", "double", "--margin",
                "0", "--padding", "1 2", "--border-foreground", "212", "--align", "center", "--width", "30", text]

        res = subprocess.run(
            args, stdout=subprocess.PIPE, text=True).stdout

        print(res)

    # Creates a simple menu
    def menu(title, options):
        Menu.card(title, True)

        args = ["gum", "choose"]

        for option in options:
            args.append(option)

        result = subprocess.run(
            args, stdout=subprocess.PIPE, text=True).stdout.strip().split(" ")[0]

        return int(result)

    # Reads input
    def inp(placeholder, password=False):
        args = ["gum", "input", "--placeholder", placeholder]

        if (password):
            args.append("--password")

        result = subprocess.run(
            args, stdout=subprocess.PIPE, text=True).stdout.strip()

        if password:
            "*" * len(result)

        print("> %s: %s" %
              (placeholder.split(" (")[0], ("*" * len(result) if password else result)))

        return result

# Database manager


class Manager():
    def __init__(self, database):
        self.__database = database
        self.__table_users = "users"

        self.__con = sqlite3.connect(self.__database)
        self.__cur = self.__con.cursor()

    def createTableUsers(self):
        self.__cur.execute("DROP TABLE users")
        self.__cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            'name',
            'email',
            'password',
            'birthDate',
            'subscription',
            'address',
            'phone',
            'paymentMethod'
        );
        """)

    def close(self):
        self.__con.close()

    def saveUser(self, user: User):
        sqlQuery = "INSERT INTO %s %s VALUES %s" % (
            self.__table_users, user.columns(), user.toSql())

        self.__cur.execute(sqlQuery)
        self.__con.commit()

    def getUsers(self):
        sqlQuery = "SELECT * FROM %s" % self.__table_users
        result = self.__cur.execute(sqlQuery).fetchall()

        users = list()
        for row in result:
            users.append(User("", "", "", "", "", "", "", "").fromSql(row))

        for user in users:
            Menu.card(user.__str__())

    def deleteUser(self, id):
        res = self.__cur.execute("DELETE FROM %s WHERE id=%s" %
                                 (self.__table_users, id)).fetchall()

        self.__con.commit()

        if self.__cur.rowcount > 0:
            return True
        else:
            return False