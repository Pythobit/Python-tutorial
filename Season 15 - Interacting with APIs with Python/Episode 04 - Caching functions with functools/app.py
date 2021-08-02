import time
from libs.openexchange import OpenExchangeClient


APP_ID = 'YOUR-APP-ID'
client = OpenExchangeClient(APP_ID)

start = time.time()
usd_amount = 1000
inr_amount = client.convert(usd_amount, 'USD', 'INR')
end = time.time()

print(end-start)
print(f'USD - ${usd_amount} in INR - Rs.{inr_amount:.2f}')
