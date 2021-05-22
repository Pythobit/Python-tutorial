# The on success block and re-raising exceptions.

class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagment_metrics = engagement

    def __repr__(self):
        return f'< User {self.name} >'

def get_user_score(user):
    try:
        return perform_calculation(user.engagment_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
        raise

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_engagement_notification(user):
    print(f'Notification sent to {user}.')


my_user = User('Rolf', {'clicks': 40, 'hits': 60})
print(get_user_score(my_user))
"""
if we want our error to bubble up, just type raise under except block indented.. as in <line 16>
if we want to send notification to the user of user score > 500
we need to modify <line 12 - 16> as
"""
def get_user_score(user):
    try:
        perform_calculation(user.engagment_metrics)     # removing the return keyword
    except KeyError:
        print('Incorrect values provided to our calculation function.')
    else:
        send_engagement_notification(user)
        # or
        if perform_calculation(user) > 500:
            send_engagement_notification(user)

