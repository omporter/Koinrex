import django_rq
from .models import AddressABC
from koinrex.users.models import User
import requests
from rq import  Worker
# change current_user() to current_user(request)


def current_user():

	current_user = User.objects.get(id=1)

	current_user_id = current_user.id

	return current_user_id

def get_tx_count():

	current_user_id = current_user()

	queue = django_rq.get_queue('default', autocommit=True, async=True)

	queue.enqueue(AddressABC.fetch_tx_count , current_user_id)
    


def get_balance():

	current_user_id = current_user()

	queue = django_rq.get_queue('default', autocommit=True, async=True)

	queue.enqueue(AddressABC.fetch_balance , current_user_id)


def get_amt_received():

	current_user_id = current_user()

	queue = django_rq.get_queue('default', autocommit=True, async=True)
	
	queue.enqueue(AddressABC.fetch_amt_received , current_user_id)
    

def get_amt_sent():

	current_user_id = current_user()

	queue = django_rq.get_queue('default', autocommit=True, async=True)

	queue.enqueue(AddressABC.fetch_amt_sent , current_user_id)
    