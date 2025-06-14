class Employee:
    language = "python"
    salary = 120000
    def __init__(self,name,job,college):
        self.name=name
        self.job=job
        self.college=college
        print(f"i am creating a beautiful oject")
    
    def getinfo(self):
        print(f"The language is very easy to understand: {self.language}")
    @staticmethod
    def greet(self):
        print("Good morning")
   
harry = Employee("harry","engineer","uit")
print(harry.college,harry.job)
