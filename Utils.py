from os import system
import sqlite3

from models.User import User


class Menu():
    # Prints a separator
    def printSeparator(size):
        print("#%s#" % ("=" * size))

    # Creates a simple menu
    def menu(title, options):
        system("clear")

        system("""gum style --border normal --margin "1" --padding "1 2" --border-foreground 212 "%s"
    """ % title)

        gumstr = "gum choose "

        for option in options:
            gumstr += "'%s' " % option

        system(gumstr + " > tes.txt")

        with open("tes.txt", "r") as f:
            option = f.readline()
            option = option.split(" ")[0].strip()
            system("rm tes.txt")
            return int(option)

    # Reads input
    def ginp(placeholder, password=False):
        usePassword = ""

        if (password):
            usePassword = "--password"

        system("gum input %s --placeholder \"%s\" > tes.txt" %
               (usePassword, placeholder))

        with open("tes.txt", "r") as f:
            option = f.readline().replace("\n", "")
            system("rm tes.txt")
            return (option)


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
            user = User("", "", "", "", "", "", "", "")
            users.append(user.fromSql(row))

        for user in users:
            print(user)
