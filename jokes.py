import requests

def get_joke():
    endpoint = "https://api.humorapi.com/jokes/search?api-key=558593e6d1334bfb94d4d2795de42e1e"
    response = requests.get(endpoint)

    if response.status_code == 200:
        joke = response.json()
        joke_text = joke["jokes"]
        return joke_text
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    joke_display = get_joke()
    print(joke_display)