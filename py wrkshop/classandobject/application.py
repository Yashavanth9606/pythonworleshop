class Application:

    def __init__(self,application_Name,categary,company,app_size,rating):
        self.application_Name=application_Name
        self.categary=categary
        self.company=company
        self.app_size=app_size
        self.rating=rating

    def signup(self):
        print(f"You signed up,{self.application_Name}")

    def login(self):
        print(f"ONE PIECE{self.application_Name}")

    def logout(self):
        print("WHITE BEARD")

    def info(self):
        print(f"welcome to app:{self.application_Name}\n categary:{self.categary}\n company:{self.company}\n app_size:{self.app_size}\n rating:{self.rating}")



app1=Application("instagram","social media","meta",42.47,4.4)
app2=Application("facebook","social media","meta",45.47,4.4)
app3=Application("youtube","social media","meta",47.50,4.4)

app1.signup()
app2.signup()
app1.login()
app2.login()
app3.login()
app1.info()






