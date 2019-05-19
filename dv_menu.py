from data_virtualization import GraphVirtualization
from graphic import Graph
import sys

class Menu():

    def __init__(self):
        self.keyboardInt = KeyboardInterrupt, EOFError
        self.dv = GraphVirtualization()
        self.mb = Graph()

    def mainMenu(self):
        while(True):
            print(("-" * 10) + "Please choose the time range of report that you want" +  ("-" * 10))
            print("1. Daily Report")
            print("2. Weekly Report")
            print("3. Monthly  Report ")
            print("4. Exit Program")

            userInput = input("\n Please enter your choice(1 - 4) :")

             #Using If .. Elif .. Else statement/conditional check to check user input and run the matched function.
            if(userInput == "1"):
                results = self.dv.get_data(7)
                self.menu(results)

            elif(userInput == "2"):
                results = self.dv.get_data(7)
                self.menu(results)

            elif(userInput == "3"):
                results = self.dv.get_data(30)
                self.menu(results)

            elif(userInput == "4"):
                #When user input 4 it will exit the program
                print("\n -------------- Good Bye -------------------")
                break
            elif(userInput == self.keyboardInt):
                print("\n Exit program because of keyboard interruption!!")
            else:
                #When user input other than 1 - 4 it will print this line
                print("Invalid input - please try again.") 

    def menu(self, results):
        #Use while loop for menu looping
        while(True):
            print("-" * 40)
            print( ("-" * 10) + "Hi, This is my sensehat learning menu" + ("-" * 10))
            print("1. Show graphic")
            print("2. Save graphic to a file")
            print("3. Back to time choice")
            print("4. Exit")

            #This will take user input and assign it into userInput variable.
            userInput = input("\nPlease enter your choice (1 - 4): ")

            #Using If .. Elif .. Else statement/conditional check to check user input and run the matched fucntion.
            if(userInput == "1"):
                #When user input 1 it will ask for user for more input(calling showMeny function)
                self.showMenu(results)
             
            elif(userInput == "2"):
                #When user input 2 it will prompt user for more input(calling saveMenu function)
                self.saveMenu(results)
              
            elif(userInput == "3"):
                #When user input 2 it will prompt user for more input(calling saveMenu function)
                self.mainMenu()               
            elif(userInput == "4"):
                #When user input 3 it will exit the program
                print("\n -------------- Good Bye -------------------")
                sys.exit()
                break
            elif(userInput == self.keyboardInt):
                print("\n Exit program because of keyboard interruption!!")
            else:
                #When user input other than 1 - 3 it will print this line
                print("Invalid input - please try again.")
        
    def showMenu(self, results):
        while(True):
            print(("-" * 10) + "Please choose the type of chart that you want to see" + ("-" *10))
            print("1. Line Chart")
            print("2. Bar Chart")
            print("3. Scatter(temperature vs humidity)")
            print("4. Multiple Charts")
            print("5. Back to main menu")
            print("6. Exit Program")

            #This will take user input and assign it into userInput variable.
            userInput = input("\nPlease enter your choice (1 - 6): ")

            #Using If .. Elif .. Else statement/conditional check to check user input and run the matched fucnction.
            if(userInput == "1"):
                graph = "line"
                self.columMenu(results, graph)
            elif(userInput == "2"):
                graph = "bar"
                self.columMenu(results, graph)
            elif(userInput == "3"):
                self.mb.scatter_plot(results)
            elif(userInput == "4"):
                graph = "multiple"
                self.columMenu(results, graph)
            elif(userInput == "5"):
                self.mainMenu() 
            elif(userInput == "6"):
                #When user input 6 it will exit the program
                print("\n -------------- Good Bye -------------------")
                sys.exit()
            elif(userInput == self.keyboardInt):
                print("\n Exit program because of keyboard interruption!!")
            else:
                #When user input other than 1 - 6 it will print this line
                print("Invalid input - please try again.")
        
    def saveMenu(self, results):
        while(True):
            print(("-" * 10) + "Please choose the type of chart that you want to save" + ("-" * 10))
            print("1. Line Chart")
            print("2. Bar Chart")
            print("3. Scatter")
            print("4. Multiple Charts")
            print("5. Back to main menu")
            print("6. Exit Program")

            #This will take user input and assign it into userInput variable.
            userInput = input("\nPlease enter your choice (1 - 6): ")

            #Using If .. Elif .. Else statement/conditional check to check user input and run the matched function.
            if(userInput == "1"):
                userInput = input("\nPlease enter your choice (1 - 6): ")
            elif(userInput == "2"):
                pass
            elif(userInput == "3"):
                pass
            elif(userInput == "4"):
                pass
            elif(userInput == "5"):
                self.mainMenu()
            elif(userInput == "6"):
                #When user input 6 it will exit the program
                print("\n -------------- Good Bye -------------------")
                sys.exit()
            elif(userInput == self.keyboardInt):
                print("\n Exit program because of keyboard interruption!!")
            else:
                #When user input other than 1 - 6 it will print this line
                print("Invalid input - please try again.")

    def columMenu(self, results, g):
        while(True):
            print(("-" * 10) + "Please choose the column that you want to see" + ("-" * 10))
            print("1. Temperature")
            print("2. Humidity")
            print("3. Pressure")
            print("4. Multiple Column")
            print("5. Exit")
            userInput = input("Please Choose between(1-4): ")
            if (userInput == "1" and g == "line"):
                self.mb.line_plot(results, y = 'Temperature(C)')
            elif userInput == "2" and g == "line":
                self.mb.line_plot(results, 'Humidity(%)')
            elif userInput == "3" and g == "line":
                self.mb.line_plot(results, 'Pressure')
            elif userInput == "1" and g == "bar":
                self.mb.bar_plot(results, 'Temperature(C)')
            elif userInput == "2" and g == "bar":
                self.mb.bar_plot(results, 'Humidity(%)')
            elif userInput == "3" and g == "bar":
                self.mb.bar_plot(results, 'Pressure')
            elif userInput == "1" and g == "multiple":
                self.mb.multiple_plot(results)
            elif userInput == "2" and g == "multiple":
                self.mb.multiple_plot(results)
            elif userInput == "3" and g == "multiple":
                self.mb.multiple_plot(results)
            elif userInput == "4" and g == "multiple":
                self.mb.multiple_plot(results)
            elif(userInput == "5"):
                #When user input 6 it will exit the program
                print("\n -------------- Good Bye -------------------")
                sys.exit()                
            elif(userInput == self.keyboardInt):
                print("\n Exit program because of keyboard interruption!!")
                sys.exit()
            else:
                print("Not withing choice range")
   
def main():
    m = Menu()
    m.mainMenu()

if __name__ == '__main__':
    main()