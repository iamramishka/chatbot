import random

# Static responses related to specific contexts
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def generate_unknown_response():
    # Random responses for unclear input
    responses = [
        "Could you please re-phrase that?",
        "...",
        "Sounds about right.",
        "What does that mean?"
    ]
    # Select a random response
    selected_response = responses[random.randrange(4)]
    return selected_response
