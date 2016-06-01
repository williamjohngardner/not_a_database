import csv


class NotADatabase:

    def __init__(self):
        self.username = ""
        self.password = ""

    def login(self):
        while True:
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            with open("notadatabase.csv") as readfile:
                data = csv.DictReader(readfile, fieldnames=["username", "password", "fullname",
                                                            "quality", "random"])
                for row in data:
                    if row["username"].lower() == username.lower():
                        if row["password"] == password:
                            return False
                else:
                    print("Username or Password incorrect.  Try again.")

    def create_user(self):
        self.username = input("Please enter your username: ")
        self.password = input("Please enter your password: ")
        fullname = input("Please enter your first and last name: ")
        quality = input("Of Bill's many good qualities, please enter your favorite: ")
        random = input("Please enter a random word of your choosing: ")
        user_input = "{},{},{},{},{}\n".format(self.username, self.password, fullname, quality, random)
        with open("notadatabase.csv", "a") as inputfile:
            inputfile.write(user_input)

while True:
    NotADatabase().login()
    user_choice = input("(C)reate new user or (L)ogout?")
    if user_choice.lower() == "c":
        NotADatabase().create_user()
    else:
        continue
