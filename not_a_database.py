import csv


class NotADatabase:

    def login(self):
        print("Please log in: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        with open("notadatabase.csv") as readfile:
            data = csv.DictReader(readfile, fieldnames=["username", "password", "fullname",
                                                        "quality", "random"])
            for row in data:
                if row["username"].lower() == username.lower():
                    if row["password"] == password:
                        NotADatabase().user_choice()
            else:
                print("Username or Password incorrect.  Try again.")

    def user_choice(self):
        user_choice = input("(C)reate new user or (L)ogout?")
        if user_choice.lower() == "c":
            NotADatabase().create_user()

    def user_name_checker(self, username):
        with open("notadatabase.csv") as readfile:
            data = csv.DictReader(readfile, fieldnames=["username", "password", "fullname",
                                                        "quality", "random"])
            for row in data:
                if row["username"].lower() == username.lower():
                    print("Username already in use.  Try again.")
                    NotADatabase().create_user()
                else:
                    break

    def create_user(self):
        username = input("Please enter your username: ")
        NotADatabase().user_name_checker(username)
        password = input("Please enter your password: ")
        fullname = input("Please enter your first and last name: ")
        quality = input("Of Bill's many good qualities, please enter your favorite: ")
        random = input("Please enter a random word of your choosing: ")
        user_input = "{},{},{},{},{}\n".format(username, password, fullname, quality, random)
        with open("notadatabase.csv", "a") as inputfile:
            inputfile.write(user_input)

        NotADatabase().login()

while True:
    NotADatabase().login()