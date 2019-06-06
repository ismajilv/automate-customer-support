import time
import random
import uwsgi

def increment_request_count(user_id):
    worker_id = str(uwsgi.worker_id())
    
    if uwsgi.cache_get(worker_id):
        c = int(uwsgi.cache_get(worker_id))
        c += 1
        uwsgi.cache_update(worker_id, str(c))
    else:
        uwsgi.cache_set(worker_id, '0')

    return f"user_id:{user_id}:workder_id:{worker_id}:request_number:{uwsgi.cache_get(worker_id).decode()}"


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

    new_request_count = increment_request_count(user_id)
    
    return new_request_count