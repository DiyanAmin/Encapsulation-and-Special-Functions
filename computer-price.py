#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
class Computer:
    def __init__(self,):
        self.__max_price=100000000000000000000000000000000000000000000000000000000000000000000000000
    def sell(self):#                             
        print(f'{self.__max_price}')
    def set_max_price(self,price):
        self.__max_price=price
o=Computer()
o.sell()
o.__max_price=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000
o.sell()
o.set_max_price(99999999999999999999999999999999999999999999999999999999999999999999999999999999999)
o.sell()