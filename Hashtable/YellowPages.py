class YellowPages:
    def __init__(self, first_name,last_name, address,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number


    def email(self):
        name = self.last_name + self.first_name 
        return name+"@gmail.com"
