from os import system
import sqlite3
import subprocess

from models.User import User


class Menu():
    # Prints a card
    def card(text, clear=False):
        if clear:
            system("clear")

        args = ["gum", "style", "--border", "normal", "--margin",
                "1", "--border-foreground", "212", text]

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
    def ginp(placeholder, password=False):
        args = ["gum", "input", "--placeholder", placeholder]

        if (password):
            args.append("--password")

        return subprocess.run(args, stdout=subprocess.PIPE, text=True).stdout.strip()


# Database manager
class Manager():
    def __init__(self, database):
        self.__database = database
        self.__table_users = "users"

        self.__con = sqlite3.connect(self.__database)
        self.__cur = self.__con.cursor()

    def saveUser(self, user: User):
        sqlQuery = "INSERT INTO %s VALUES %s" % (
            self.__table_users, user.toSql())

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
