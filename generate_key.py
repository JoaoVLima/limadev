from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()

fp = open('secret_keys.py', 'w')
fp.write(f"django_key = '{secret_key}'")
fp.close()