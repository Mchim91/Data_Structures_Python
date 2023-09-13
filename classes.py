#### Classes ###
# Classes are used to create personal data type
# Constructor -  is a unique function that gets called automatically when an object is created of a class.
class Cookie:
    def __init__(self, color): # __init__ is a constructor
        self.color = color # it creates a specific instance of color we are creating
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color

cookie_one = Cookie('green') # The variable name cookie_one is be setup to a type Cookie and passing color green which is passed to the constructor
cookie_two = Cookie('red')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
