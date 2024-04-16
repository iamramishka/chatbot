import re
import random
import long_responses as long

def calculate_message_relevance(user_message, recognized_keywords, is_single_response=False, required_keywords=[]):
    relevance_score = 0
    contains_required_keywords = True

    for word in user_message:
        if word in recognized_keywords:
            relevance_score += 1

    relevance_percentage = float(relevance_score) / float(len(recognized_keywords))

    for keyword in required_keywords:
        if keyword not in user_message:
            contains_required_keywords = False
            break

    if contains_required_keywords or is_single_response:
        return int(relevance_percentage * 100)
    else:
        return 0

def evaluate_all_messages(message):
    response_probabilities = {}

    def add_response(bot_response, list_of_keywords, is_single_response=False, required_keywords=[]):
        nonlocal response_probabilities
        response_probabilities[bot_response] = calculate_message_relevance(
            message, list_of_keywords, is_single_response, required_keywords)

    add_response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], is_single_response=True)
    add_response('See you!', ['bye', 'goodbye'], is_single_response=True)
    add_response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_keywords=['how'])
    add_response('You\'re welcome!', ['thank', 'thanks'], is_single_response=True)
    add_response('Thank you!', ['i', 'love', 'code', 'palace'], required_keywords=['code', 'palace'])
    add_response(long.R_ADVICE, ['give', 'advice'], required_keywords=['advice'])
    add_response(long.R_EATING, ['what', 'you', 'eat'], required_keywords=['you', 'eat'])

    best_response = max(response_probabilities, key=response_probabilities.get)

    return unknown() if response_probabilities[best_response] < 1 else best_response

def unknown():
    responses = [
        "Could you please re-phrase that?",
        "...",
        "Sounds about right.",
        "What does that mean?"
    ]
    return responses[random.randrange(4)]

def get_user_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = evaluate_all_messages(split_message)
    return response

# Interactive response loop
if __name__ == "__main__":
    while True:
        print('Bot: ' + get_user_response(input('You: ')))
