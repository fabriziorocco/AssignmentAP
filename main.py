### The following script contains the class and methods to manage a warehouse and specific stocks.
### It contains 2 main classes (Stocks and Warehouse), 4 minor classes related to the specific stocks (Phone, Television, Tablet, Computer) and a main function to handle user's inputs.

from utils import let_user_pick


class Stock:

    def __init__(self) -> None:
        self.amount = 0


    def add(self, amount:int) -> None:
        """ This function increases the amount of stock by the input variable"""
        self.amount += amount


    def remove(self, amount:int) -> None:
        """ This function decreases the amount of stock by the input variable"""
        self.amount -= amount


    def get_amount(self) -> None:
        """ This function returns the amount of the given stock"""
        return self.amount


# This part initializes 4 classes relative to the specific stocks we're going to use.
# Each of this class inherits methods from the main "Stock" class.
class Phone (Stock):

    def __init__(self) -> None:
        super().__init__()

class Computer (Stock):

    def __init__(self) -> None:
        super().__init__()

class Tablet (Stock):

    def __init__(self) -> None:
        super().__init__()

class Television (Stock):
    
    def __init__(self) -> None:
        super().__init__()



# The following part initializes a warehouse to manage all the previously defined stocks.
# The constructor uses the method from the "Stock" class.

class Warehouse():
    
    def __init__(self, phone, computer, tablet, television) -> None:
        """ The following constructor takes as parameter the instances of the stocks previously created and compute the current amount"""
        self.phone = phone.get_amount()
        self.computer = computer.get_amount()
        self.tablet = tablet.get_amount()
        self.television = television.get_amount()


    def addStock(self, stock:str, amount:int =1) -> None:
        """ The following function takes two parameters (stock, amount) which are respectively the type of the stock ("phone", "tablet", "computer", "television")
            and the amount of stocks we want to add as integer (Default value = 1).
            It increases the specific stock by the amount.
        """
        match stock:
            case "phone":
                self.phone += amount
            case "computer":
                self.computer += amount
            case "tablet":
                self.tablet += amount
            case "television":
                self.television += amount


    def removeStock(self, stock:str, amount:int=1) -> None:
        """ The following function takes two parameters (stock, amount) which are respectively the type of the stock ("phone", "tablet", "computer", "television")
            and the amount of stocks we want to remove as integer (Default value = 1).
            It decreases the specific stock by the amount.
            To avoid negative values, this function computes the maximum value between 0 and the difference of the current value and the amount given by the user.
            If the amount is 0, the function will print a warning message.
        """
        match stock:
            case "phone":
                self.phone = max(self.phone - amount, 0)
                if self.phones == 0:
                    print("\n\n Warning: no more phones! \n\n")
            case "computer":
                self.computer =  max(self.computer - amount, 0)
                if self.computer == 0:
                    print("\n\n Warning: no more computers! \n\n")
            case "tablet":
                self.tablet =  max(self.tablet - amount, 0)
                if self.tablet == 0:
                    print("\n\n Warning: no more tablets! \n\n")
            case "television":
                self.television =  max(self.television - amount, 0)
                if self.television == 0:
                    print("\n\n Warning: no more televisions! \n\n")


    def search(self, stock:str):
        """ The following function takes a single parameter (stock) which is the type of the stock ("phone", "tablet", "computer", "television").
            It searches the specific stock in the warehouse.
            It prints a message if the stock is available or not.
        """
        match stock:
            case "phone":
                if self.phone > 0:
                    print( "\n {} found! \n".format(stock))
                else:
                    print( "\n {} found! \n".format(stock))
            case "computer":
                if self.computer > 0:
                    print( "\n {} found! \n".format(stock))
                else:
                    print( "\n {} found! \n".format(stock))
            case "tablet":
                if self.tablet > 0:
                    print( "\n {} found! \n".format(stock))
                else:
                    print( "\n {} found! \n".format(stock))
            case "television":
                if self.television > 0:
                    print( "\n {} found! \n".format(stock))
                else:
                    print( "\n {} found! \n".format(stock))
    

    def generateReport (self):
        """ The following function takes no parameters and print a dictionary with the amount of stocks available"""
        self.report = {"Amount of Phones": self.phone, "Amount of Computers": self.computer, "Amount of Tablets": self.tablet, "Amount of Televisions": self.television,}
        return self.report


###################################### Main function that execute the script in the terminal ######################################

def main():
    """ The following variables instantiate the 4 stock's classes"""
    phone = Phone()
    computer = Computer()
    tablet = Tablet()
    television = Television()

    """ The following lines allow the user to choose the city on which establish the warehouse between Barcelona and Madrid
        To do that, a specific function called "let_user_pick" has been provided in a separate file (utils.py) to facilitate user's choice
    """
    cities = ["Barcelona", "Madrid"]
    region = let_user_pick(cities)
    match region:
        case 1:
            barcelonaWarehouse = Warehouse(phone, computer, tablet, television)
        case 2:
            madridWarehouse = Warehouse(phone, computer, tablet, television)


    """ This is the main menù of the script. It allows the user to choose the action to do between
        - Add a stock
        - Remove a stock
        - Find a stock
        - Get all the stocks for the current warehouse
        - Quit the script
        To do that, a specific function called "let_user_pick" has been provided in a separate file (utils.py) to facilitate user's choice
    """
    options = ["Add Stock", "Remove Stock", "Find Stock", "Get all Stocks", "Quit"]
    while True:
        handler = let_user_pick(options)
        match handler:
            
            case 1:
                if region == 1:
                    stockTypeOptions = ["Add a Phone stock", "Add a Computer stock", "Add a Tablet stock", "Add a Television stock"]
                    stockType = let_user_pick(stockTypeOptions)
                    match stockType:
                        case 1:
                            stockType = "phone"
                        case 2:
                            stockType = "computer"
                        case 3:
                            stockType = "tablet"
                        case 4:
                            stockType = "television"
                    try:
                        stockAmount = int(input("How many stocks of {} do you want to add?".format(stockType)))
                    except:
                        print("Please insert only numbers!")
                    barcelonaWarehouse.addStock(stockType, stockAmount)
                    print("\n\n Added {} stocks of {} ! \n\n".format(stockAmount,stockType))
                else:
                    stockTypeOptions = ["Add a Phone stock", "Add a Computer stock", "Add a Tablet stock", "Add a Television stock"]
                    stockType = let_user_pick(stockTypeOptions)
                    match stockType:
                        case 1:
                            stockType = "phone"
                        case 2:
                            stockType = "computer"
                        case 3:
                            stockType = "tablet"
                        case 4:
                            stockType = "television"
                    try:
                        stockAmount = int(input("How many stocks of {} do you want to add?".format(stockType)))
                    except:
                        print("Please insert only numbers!")
                    madridWarehouse.addStock(stockType,stockAmount)
                    print("\n\n Added {} stocks of {} ! \n\n".format(stockAmount,stockType))
            
            case 2:
                if region == 1:
                    stockTypeOptions = ["Remove a Phone stock", "Remove a Computer stock", "Remove a Tablet stock", "Remove a Television stock"]
                    stockType = let_user_pick(stockTypeOptions)
                    match stockType:
                        case 1:
                            stockType = "phone"
                        case 2:
                            stockType = "computer"
                        case 3:
                            stockType = "tablet"
                        case 4:
                            stockType = "television"
                    try:
                        stockAmount = int(input("How many stocks of {} do you want to remove?".format(stockType)))
                    except:
                        print("Please insert only numbers!")
                    barcelonaWarehouse.removeStock(stockType, stockAmount)
                    print("\n\n Removed {} stocks of {} ! \n\n".format(stockAmount,stockType))
                else:
                    stockTypeOptions = ["Remove a Phone stock", "Remove a Computer stock", "Remove a Tablet stock", "Remove a Television stock"]
                    stockType = let_user_pick(stockTypeOptions)
                    match stockType:
                        case 1:
                            stockType = "phone"
                        case 2:
                            stockType = "computer"
                        case 3:
                            stockType = "tablet"
                        case 4:
                            stockType = "television"
                    try:
                        stockAmount = int(input("How many stocks of {} do you want to remove?".format(stockType)))
                    except:
                        print("Please insert only numbers!")
                    madridWarehouse.removeStock(stockType, stockAmount)
                    print("\n\n Removed {} stocks of {} ! \n\n".format(stockAmount,stockType))
            
            case 3:
                if region == 1:
                    stockTypeOptions = ["Find a Phone stock", "Find a Computer stock", "Find a Tablet stock", "Find a Television stock"]
                    stockType = let_user_pick(stockTypeOptions)
                    match stockType:
                        case 1:
                            stockType = "phone"
                        case 2:
                            stockType = "computer"
                        case 3:
                            stockType = "tablet"
                        case 4:
                            stockType = "television"
                    print(barcelonaWarehouse.search(stockType))

                else:
                    stockTypeOptions = ["Find a Phone stock", "Find a Computer stock", "Find a Tablet stock", "Find a Television stock"]
                    stockType = let_user_pick(stockTypeOptions)
                    match stockType:
                        case 1:
                            stockType = "phone"
                        case 2:
                            stockType = "computer"
                        case 3:
                            stockType = "tablet"
                        case 4:
                            stockType = "television"
                    print(madridWarehouse.search(stockType))
            
            case 4:
                if region == 1:
                    print(barcelonaWarehouse.generateReport())
                else:
                    print(madridWarehouse.generateReport())
            
            case 5:
                break


if __name__ == "__main__":
    main()

    
            



    