import sys
bocadillo = {
    'ingredients' : ['jamon', 'pan', 'queso', 'tomate'],
    'meal' : 'almuerzo',
    'prep_time': 10,
    }
tarta = {
    'ingredients' : ['harina', 'azucar', 'huevos'],
    'meal' : 'postre',
    'prep_time': 60,
    }
ensalada = {
    'ingredients' : ['aguacate', 'rucula', 'tomates', 'espinacas'],
    'meal' : 'almuerzo',
    'prep_time': 15,
    }
cookbook = {
    'bocadillo' : bocadillo,
    'tarta' : tarta,
    'ensalada' : ensalada, 
    }

def print_all_recipes():
    all_recipes = cookbook.keys()
    print (all_recipes)

def get_recipe():
    try:
            recipe = input("Enter the recipe you want to retrieve: ")
            print ("Recipe: " + recipe)
            recipe1 = cookbook[recipe] 
            print ("Ingedients: " + ' '.join(recipe1['ingredients']))
            print ("To be eaten for " + cookbook[recipe]["meal"])
            print ("Takes " + str(cookbook[recipe]["prep_time"]) + " minutes of cooking")
    except:
            print ("The given recipe doesn't exist in the DB")

def delete_recipe():
    try:
            recipe = input("Enter the recipe you want to delete: ")
            del cookbook[recipe]
            print ("Recipe successfully deleted from DB")
    except:
            print ("The given recipe doesn't exist in the DB")

def add_recipe():
    print("Enter the recipe name: ")
    try:
            name = input("")
    except Exception as e:
            print(e)
            sys.exit(0)
    ingredients = list()
    ingredient = "f"
    print("Enter the ingredients:")
    while not ingredient == "":
            ingredient = input()
            if not ingredient == "":
                    ingredients.append(ingredient)
    meal = input("Enter meal type: ")
    prep_time = input("Enter prep time: ")
    new_recipe = {
        'ingredients' : ingredients,
        'meal' : meal,
        'prep_time' : prep_time,
    }
    cookbook[name] = new_recipe
    print ("Recipe succesfully added")

menu = """Welcome to the Python Cookbook!
List of available options:
[1] [A]dd a recipe
[2] [D]elete a recipe
[3] [Pr]rint recipe
[4] [Pc]rint cookbook
[5] [Q]uit

Please select an option:"""

error_message = "This is not a valid option, please enter one of the options between [brackets]"

ending_message = "Thanks for using the software, bye!"
option = 'f'
while not (option == '5' or option == 'Q'):
    print (menu)
    option = input()
    if option == '1' or option == 'A':
        add_recipe()
    elif option == '2' or option == 'D':
        delete_recipe()
    elif option == '3' or option == 'Pr':
        get_recipe()
    elif option == '4' or option == 'Pc':
        print_all_recipes()
    elif option == '5' or option == 'Q':
        break
    else:
        print(error_message)
    print()
print(ending_message)
    
