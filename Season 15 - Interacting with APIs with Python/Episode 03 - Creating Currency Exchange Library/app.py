from libs.openexchange import OpenExchangeClient


APP_ID = 'YOUR-APP-ID'
client = OpenExchangeClient(APP_ID)

usd_amount = 1000
inr_amount = client.convert(usd_amount, 'USD', 'INR')

print(f'USD - ${usd_amount} is INR - Rs.{inr_amount:.}')
f