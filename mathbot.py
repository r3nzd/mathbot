import wolframalpha
import wikipedia

# Set up Wolfram Alpha API credentials
app_id = "JH8JX2-ULWWW2UV47"
client = wolframalpha.Client(app_id)

# Define a function to handle user input and generate response
def handle_input(user_input):
    try:
        # Query Wolfram Alpha API
        res = client.query(user_input)
        answer = next(res.results).text
        
        return answer
    except:
        try:
            print('Please wait...')
            return summary
        except:
            #If bot doesnt know answer
            apology = "I'm sorry, I don't know the answer to that. Can you ask me something else?"
            
            return apology

# Define a function to start the chatbot
def start_chatbot():
    print("Hi I'm MathBot. Ask me any basic calculation in math.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "bye":
            print("MathBot: Goodbye!")
            break
        else:
            chatbot_response = handle_input(user_input)
            print("MathBot:", chatbot_response)

# Start the chatbot
start_chatbot()
