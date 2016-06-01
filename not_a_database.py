import csv


class NotADatabase:

    def __init__(self):
        self.username = ""
        self.password = ""

    def login(self):
        while True:
            self.username = input("Please enter your username: ")
            self.password = input("Please enter your password: ")
            with open("notadatabase.csv") as readfile:
                user_input = csv.DictReader(readfile, fieldnames=["username", "password", "fullname",
                                                                  "quality", "random"])
                for row in user_input:
                    if row["username"].lower() == self.username.lower():
                        if row["password"] == self.password:
                            break
                        else:
                            print("###111###Username or Password incorrect.  Try again.")
                            continue
                    else:
                        print("###222###Username or Password incorrect.  Try again.")
                        continue

    def create_user(self):
        self.username = input("Please enter your username: ")
        self.password = input("Please enter your password: ")
        fullname = input("Please enter your first and last name: ")
        quality = input("Of Bill's many good qualities, please enter your favorite: ")
        random = input("Please enter a random word of your choosing: ")
        user_input = "{}, {}, {}, {}, {}\n".format(self.username, self.password, fullname, quality, random)
        with open("notadatabase.csv", "a") as inputfile:
            inputfile.write(user_input)
