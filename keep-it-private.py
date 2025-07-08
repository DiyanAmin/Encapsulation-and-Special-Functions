#Write a program to create a class with following variables and methods - 1. Private variable named privateVar that contains an integer value 2. Create a  function privMeth that prints a message 3. Create a function hello that prints the value of privateVar 4. Create an object for the class and call all the functions.
class Noname:
    __privateVar=90
    def __privMeth(self):
        print('Hello World')
    def Hello(self):
        print(Noname.__privateVar)
objet=Noname()
print(f'Private Mthod:\nHello function: {objet.Hello()}')
