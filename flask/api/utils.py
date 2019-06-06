import time
import random

def increment_request_count(user_id):
    pass


def run_classifier():
    time.sleep(1) #mocked by 1 second 
    
    return True


def get_external_data():
    """
        I understood it like if the external api return response it should do in microseconds if not then waiting. 
        I did it like, there is 90 percent of chance to get response immediately and 10 percent chance of waiting.
    """
    choices = [0] * 90 + [60] * 10 
    choice = random.choice(choices)

    if choice ==  60:
        time.sleep(5)
    
    return True


def request(user_id):
    run_classifier()
    get_external_data()

    # new_request_count = increment_request_count(user_id)
    pass