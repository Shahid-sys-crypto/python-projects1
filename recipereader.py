def load_recipe(file_path):
    try:
        with open(file_path) as file:
            content=file.read()
            recipes=content.split("\n\n")
            recipe_dict={}
            for recipe in recipes:
                lines=recipe.split("\n")
                if len(lines)>=3:
                    name=lines[0].strip()
                    ingredients=lines[1].replace("ingredients","").strip()
                    instructions=lines[2].replace("instructions","").strip()
                    recipe_dict[name]={"ingredients":ingredients,"instructions":instructions}
            return recipe_dict
    except FileNotFoundError:
        print("file is not found")
        return {}
def show_menu():
    print("\n---recipe viewer menu---")
    print("1. view recipe by name")
    print("2. list all recipes")
    print("3. exit")
def view_recipe(recipes):
    name=input("enter the name of recipe:").strip()
    if name in recipes:
        print(f"\n----recipe {name} details----")
        print(f"ingredients: {recipes[name]['ingredients']}")
        print(f"instuctions: {recipes[name]['instructions']}")
    else:
        print("recipe not found")
recipe_file=input("enter the file name")
recipes=load_recipe(recipe_file)
while True:
    show_menu()
    choice=int(input("Enter your choice (1/2/3)"))
    if choice==1:
        view_recipe(recipes)
    elif choice==2:
        print("\n----all recipes----")
        for name in recipes:
            print(name)
    elif choice==3:
        print("exit the program")
        break
    else:
        print("invalid choice.please try again")
