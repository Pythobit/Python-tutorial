import requests

APP_ID = 'YOUR-APP-ID'
ENDPOINT = 'https://openexchangerates.org/api/latest.json'

response = requests.get(f'{ENDPOINT}?app_id={APP_ID}')
exchange_rates = response.json()['rates']

usd_amount = 1000
inr_amount = usd_amount * exchange_rates['INR']

print(f'USD - ${usd_amount} is INR - Rs.{inr_amount}')

