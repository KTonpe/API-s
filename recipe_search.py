# webitse- https://www.edamam.com/

import requests

def find_recipes(query):
    # Edamam Recipe Search API endpoint
    endpoint = "https://api.edamam.com/search"

    # API Credentials - Replace 'YOUR_APP_ID' and 'YOUR_APP_KEY' with your actual credentials
    app_id = "0668ce0c"
    app_key = "f80a4f2d0a9459e21e760c455c0053c8"

    # Parameters for the API request
    params = {
        'q': query,
        'app_id': app_id,
        'app_key': app_key
    }

    # Sending HTTP GET request to the API
    response = requests.get(endpoint, params=params)
    data = response.json()

    # Check if request was successful
    if response.status_code == 200:
        # Extracting recipe information
        recipes = data['hits']
        for recipe in recipes:
            recipe_details = recipe['recipe']
            print(f"Recipe: {recipe_details['label']}")
            print(f"URL: {recipe_details['url']}")
            print("Ingredients:")
            for ingredient in recipe_details['ingredientLines']:
                print(f"- {ingredient}")
            print()
            break
    else:
        print("Error:", data['error'])

if __name__ == "__main__":
    query = input("Enter a dish to search for recipes: ")
    find_recipes(query)
