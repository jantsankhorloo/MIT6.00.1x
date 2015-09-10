class Parent():
    def __init__(self, last_name, eye_color):
        print ('Parent Constructor Called')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ('Last name -'+self.last_name)
        print ('Eye color -'+self.eye_color)

class Child(Parent): #This class Child is Inheriting from class Parent, hence in a paranthesis
    def __init__(self, last_name, eye_color, number_of_toys):
        print ('Child Constructor Called')
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def shor_info(self):
        print ('last name -'+self.last_name)
        print ('eye color -'+self.eye_color)
        print ('number of toys -'+str(self.number_of_toys)

billy_cyrus = Parent('Cyrus','Blue')
miley_cyrus = Child('Cyrus','Blue',5)
billy_cyrus.show_info()
miley_cyrus.show_info()
