import requests

# Function to fetch a random quote from ZenQuotes.io
def get_quote():
    quote_response = requests.get('https://zenquotes.io/api/random')
    data = quote_response.json()
    quote = data[0]['q'] + " -" + data[0]['a']  # Extracting the quote and author
    return quote

# Function to fetch a joke from JokeAPI
def get_joke():
    joke_response = requests.get("https://v2.jokeapi.dev/joke/Programming?blacklistFlags=religious,political,racist,sexist,explicit")
    data = joke_response.json()
    joke = data["setup"] + " -" + data["delivery"]
    return joke

def main():
    print("Welcome to the Quote and Joke Fetcher!")
    while True:
        print("\nChoose an option:")
        print("1. Fetch a random quote")
        print("2. Fetch a programming joke")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            quote = get_quote()
            print("Random Quote:", quote)
        elif choice == "2":
            joke = get_joke()
            print("Programming Joke:", joke)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
