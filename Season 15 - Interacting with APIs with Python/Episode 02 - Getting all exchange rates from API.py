import requests

APP_ID = 'e07eff8a09ea4d0c9cb1b1ff996646bf'
ENDPOINT = 'https://openexchangerates.org/api/latest.json'

response = requests.get(f'{ENDPOINT}?app_id={APP_ID}')
exchange_rates = response.json()['rates']

usd_amount = 1000
inr_amount = usd_amount * exchange_rates['INR']

print(f'USD - ${usd_amount} is INR - Rs.{inr_amount}')

