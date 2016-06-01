import csv


class InfoCollector:

    def __init__(self):
        self.username = input("Please enter your username: ")
        self.password = input("Please enter your password: ")
        self.fullname = input("Please enter your first and last name: ")
        self.quality = input("Please tell me your favorite of Bill's many good qualities: ")
        self.random = input("Please enter a random word of your choosing: ")
        self.user_input = "{}, {}, {}, {}, {}\n".format(self.username, self.password, self.fullname,
                                                        self.quality, self.random)
        with open("notadatabase.csv", "a") as inputfile:
            inputfile.write(self.user_input)


info_collect = InfoCollector()