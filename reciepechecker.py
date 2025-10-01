recipe={"sugar","eggs","flour","oil","milk"}
user_recipe=input("enter the recipe using commas\n")
user_recipe=set(user_recipe.split(","))
#print(user_recipe)
#print(recipe)
missing_ingredient=recipe-user_recipe
extra_ingredient=user_recipe-recipe

if missing_ingredient:
    for item in missing_ingredient:
        print(item+" should be added")
if extra_ingredient:
    for items in extra_ingredient:
        print(items+" should be avoided")