class employee:
    company="ITC"
    name="default"
    def show(self):
        print(f"the name of the employee is {self.name}")

class coder:
    language="Python"
    def printlanguage(self):
        print(f"the language to be followed is {self.language}")

class programmer(employee,coder):
    company="itc infotech"
    def showlanguage(self):
        print(f"the language is {self.language}")

a=employee()
b=programmer()
b.show()
b.printlanguage()
b.showlanguage()            


