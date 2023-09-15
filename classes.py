#### Classes ###
# Classes are used to create personal data type
# Constructor -  is a unique function that gets called automatically when an object is created of a class.

# Define a class named 'Cookie'.
class Cookie:
    # The constructor (__init__) is a special method that gets called automatically when an object is created.
    def __init__(self, color):  # 'self' refers to the instance being created, 'color' is a parameter.
        # Create an instance variable 'color' and assign it the value passed as a parameter.
        self.color = color

    # Define a method 'get_color' to retrieve the color of the cookie.
    def get_color(self):
        return self.color
    
    # Define a method 'set_color' to change the color of the cookie.
    def set_color(self, color):
        self.color = color

# Create instances (objects) of the 'Cookie' class.
cookie_one = Cookie('green') # Create a 'Cookie' object with color 'green'.
cookie_two = Cookie('red')   # Create another 'Cookie' object with color 'red'.

# Print the initial colors of the cookies.
print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

# Change the color of 'cookie_one' to 'yellow'.
cookie_one.set_color('yellow')

# Print the updated colors of the cookies.
print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
