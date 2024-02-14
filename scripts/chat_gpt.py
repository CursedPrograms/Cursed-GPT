import json
import openai

# Function to load API key from a JSON file
def load_api_key(file_path='./key.json'):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            api_key = data.get('api_key', '')
            if not api_key:
                raise ValueError("API key is missing in the configuration file.")
            return api_key
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Error decoding JSON in the configuration file: {file_path}")

# Load the API key
api_key = load_api_key()
openai.api_key = api_key

while True:
    user_input = input("Enter your input (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break

    # Use OpenAI API for language generation
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    # Print the generated response
    print("Generated response:", completion.choices[0].message.content)
