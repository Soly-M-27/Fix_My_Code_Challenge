#!/usr/bin/python3
''' User class '''


class User():
    ''' Create User Object '''

    def __init__(self):
        ''' Initialize User Object '''
        self.__email = None

    @property
    def email(self):
        ''' Getter for private instance attribute email '''
        return self.__email

    @email.setter
    def email(self, value):
        ''' Setter for User's email '''
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
