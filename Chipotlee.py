import os

#order dictionaries. They are assigned as ingreditent:upcharge
main_ingredients = {
    "Ground Beef" : 0,
    "Carne asada" : 1.00,
    "Carne adovada" : 1.00,
    "Scrambled eggs" : 0,
    "Chicken" : 0,
    "Sofritas" : 0
}

starch_ingredients = {
    "Rice": 0.25,
    "Cilantro rice" : 0.25,
    "Beans" : 0,
    "No beans" : 0
}

filling_ingredients = {
    "Extra beans" : 0.50,
    "Chorizo" : 1.00,
    "Onion" : 0,
    "Peppers" : 0,
    "Salsa" : 0,
    "Green chile salsa" : 0.25,
    "Cheese" : 0,
    "Extra cheese" : 0.50,
    "Potatoes" : 1.00
}
def list_ingredients(ingredient):
    loop_num = 1
    for x in ingredient:
        print(str(loop_num), ". ", x , " -> ", "${:.2f}".format(ingredient[x]))
        loop_num += 1

def list_order(current_order):
    #for x in current_order:
    print(current_order)

def select_item(ingredient, selection):
    ingredient_table = []
    for x in ingredient:
        ingredient_table.append(x)
    return ingredient_table[int(selection) - 1]

def get_total(base_price, current_order):
    working_total = base_price
    for x in range(len(current_order)):
        if current_order[x] in main_ingredients:
            working_total += main_ingredients[current_order[x]]
        elif current_order[x] in starch_ingredients:
            working_total += starch_ingredients[current_order[x]]
        elif current_order[x] in filling_ingredients:
            working_total += filling_ingredients[current_order[x]]
    return(working_total)


def main_order():
    clear = lambda: os.system('clear')
    starting_cost = 5.00
    customer_name = input("What is the name you'd like for the order to be under?: ")
    ingredients_order = []
    total_cost = 5.00
    loop_check = True
    input("Press Enter to begin placing your order.")
    clear()
    
    while(loop_check):
        try:
            print(customer_name,"'s order: ", "${:.2f}".format(get_total(starting_cost, ingredients_order)), ingredients_order)
            print("Please select your main ingredient.")
            list_ingredients(main_ingredients)
            ingredients_order.append(select_item(main_ingredients, input()))
            loop_check = False
        except:
            input("Invalid selection. Please try again")
        clear()

    loop_check = True
    while(loop_check):
        try:
            print(customer_name,"'s order: ", "${:.2f}".format(get_total(starting_cost, ingredients_order)), ingredients_order)
            print("Please select your starch ingredients.")
            list_ingredients(starch_ingredients)
            ingredients_order.append(select_item(starch_ingredients, input()))
            loop_check = False
        except:
            input("Invalid selection. Please try again")
        clear()

    loop_variable = ""
    while loop_variable != "exit":
        print(customer_name,"'s order: ", "${:.2f}".format(get_total(starting_cost, ingredients_order)), ingredients_order)
        print("Please select your filling ingredients. Type \"exit\" when done.")
        list_ingredients(filling_ingredients)
        loop_variable = input()
        if loop_variable != "exit":
            try:
                ingredients_order.append(select_item(filling_ingredients, loop_variable))
                loop_check = False
            except:
                input("Invalid selection. Please try again")
        clear()

    #total
    print("Your burrito build: ", ingredients_order)
    print("Your total for this order is:", "${:.2f}".format(get_total(starting_cost, ingredients_order)))

main_order()