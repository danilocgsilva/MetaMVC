from getpass import getpass

class DatabaseUserData:

    def __init__(self):

        defaultHosts = [
            "localhost",
            "127.0.0.1"
        ]

        defaultPorts = [
            3306
        ]

        self.host = self.__ask_with_defaults(defaultHosts, "host")
        self.user = input("Please, provides the database username: ")
        self.name = input("Please, provides the database name: ")
        self.password = getpass("Please, provides the database password (wont will be shown in the output): ")
        self.port = self.__ask_with_defaults(defaultHosts, "port")

    def getName(self):
        return self.name

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port

    def getPassword(self):
        return self.password

    def getUser(self):
        return self.user

    def __ask_with_defaults(self, defaults: list, member: str):
        message = "If "

        for option in defaults:
            message += option

        message += " is not the " + member + ", then please, provides the correct one: "

        return input(message)

    
