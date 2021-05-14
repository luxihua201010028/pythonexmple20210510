def make_pizza(size,*toppings):
    '''print the the pizzas to make'''
    print("\nmakeing a " + str(size) +
          "-inch pizza with the following toppings")
    for topping in toppings:
        print("- " + topping)
