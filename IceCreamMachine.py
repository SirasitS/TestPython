class IceCreamMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        
    def scoops(self):
        scoop = []
        for ingredient in self.ingredients:
            for topping in self.toppings:
                scoop.append([ingredient, topping])
        return scoop

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops()) #should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]