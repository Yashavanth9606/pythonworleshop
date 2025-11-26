class aadhar:
    def __init__(self,name,aadhar_number,dob,finger_print,retina):
        self.name=name
        self.aadhar_number=aadhar_number
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina

    def display_userData(self):
        print(f"retina :{self.__retina} ,aadhar number : {self.aadhar_number}")

var=aadhar("YASH", 234556,"1-jul-2003", "True","False")
var.display_userData()
retina_var=var.getretina()
print(retina_var)