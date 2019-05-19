class Validation():

    def input_empty(self, userInput):
        rePass = False
        if not userInput or not userInput.strip():
            rePass = False
        else:
            rePass = True
        return rePass
        
    def first_file_name(self):
        filename = input("Please enter the desired filename for the graphs:")
        passed = self.input_empty(filename)
        while passed != True:
            filename = input(("\nPlease enter the desired filename for the graphs:"))
        return filename
                    
                