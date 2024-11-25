class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        ingredients = "\n".join(self.ingredients)
        return f"Recipe for {self.name}:\n\nIngredients:\n{ingredients}\n\nInstructions:\n{self.instructions}"

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        print(f"Recipe for {recipe.name} added successfully.")
        
    def view_recipes(self):
        if not self.recipes:
            print("No recipes available.")
            return
        for recipe in self.recipes:
            print(recipe)
            print("-" * 40)

    def delete_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                self.recipes.remove(recipe)
                print(f"Recipe for {name} deleted successfully.")
                return
        print(f"Recipe for {name} not found.")

def main():
    manager = RecipeManager()

    while True:
        print("\nRecipe Management System")
        print("1. Add a recipe")
        print("2. View recipes")
        print("3. Delete a recipe")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the recipe name: ")
            ingredients = []
            print("Enter the ingredients (type 'done' when finished):")
            while True:
                                ingredient = input()
                if ingredient.lower() == "done":
                    break
                ingredients.append(ingredient)
            instructions = input("Enter the instructions: ")
            recipe = Recipe(name, ingredients, instructions)
            manager.add_recipe(recipe)
        elif choice == "2":
            manager.view_recipes()
        elif choice == "3":
            name = input("Enter the name of the recipe to delete: ")
            manager.delete_recipe(name)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()