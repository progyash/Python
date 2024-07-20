class Animals:
    def __init__(self, name, animal_type, price):
        self.name = name
        self.animal_type = animal_type
        self.price = price

    def print_parameters(self):
        print("Name:", self.name)
        print("Type:", self.animal_type)
        print("Price:", self.price)

a1 = Animals("Lab", "Dog", 10000)
a1.print_parameters()
