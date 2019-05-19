import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from data_virtualization import GraphVirtualization
#from dv_menu import Menu
import sys
from validation import Validation

class Graph():

    def __init__(self):
        self.dv = GraphVirtualization()
        #self.menu = Menu()
        self.vd = Validation()

    """def save_prompt(self):
        invalid_message = print("Invalid input!! Please enter (Y/N/Yes/No)")
        
        print("\n Do you want to save the figure?")
        userInput = input("Please Confirm (Y/N) :")
        
        if userInput == "Y" or userInput == "Yes":
            filename = self.vd.first_file_name()
            plt.savefig(filename+ ".png")
        elif userInput == "N" or userInput == "No":
            print("\n File will not be saved. Thankyou!")
            uInput = input("\n Do you want to go back to the main menu(1) or exit program(2)?")
            if (uInput == 1):
                self.menu.mainMenu()
            elif (uInput == 2):
                print("\n Thankyou, GoodBye")
                sys.exit()
            else:
                invalid_message
        else:
            invalid_message """

    def line_plot(self, data, y):
        datas = data
        datas.plot(kind='line', x = 'Timestamp', y = y)
        plt.show()
        #self.save_prompt()

    def bar_plot(self, data, y):
        datas = data
        datas.plot(kind='bar',x='Timestamp',y= y)
        plt.show()
        #self.save_prompt()

    def scatter_plot(self, data):
        datas = data
        datas.plot(kind='scatter',x='Temperature(C)',y= 'Humidity(%)', color ='red')
        plt.show()
        #self.save_prompt()

    def multiple_plot(self, data):
        print("coming soon. Postponed for now as i need to make website project for company")
            
