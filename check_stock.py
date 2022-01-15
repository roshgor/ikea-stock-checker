# %%

import requests
import alerts

online_store_code = '598'
product_id = '40500350' # Utespelare gaming desk
# product_id = '40504065' # Mug
# product_id = '40317078' # Hanger 

url = f"https://api.ingka.ikea.com/cia/availabilities/ru/in?itemNos={product_id}&expand=StoresList,Restocks,SalesLocations"
headers = {'x-client-id':'b6c117e5-ae61-4ef5-b4cc-e0b1e37f0631'}

response = requests.get(url, headers=headers)

data = response.json()['data']

online_store_data = [store for store in data if store['classUnitKey']['classUnitCode']==online_store_code][0]

stock_avl = online_store_data['availableStocks'][0]

# print(stock_avl)

current_stock = stock_avl['quantity']
last_update = stock_avl['updateDateTime']

print(f"Current stock : {current_stock}")

if(current_stock):
    # Trigger ALERTS
    message = f"BACK IN STOCK - {current_stock} NOs AVAILABLE"
    alerts.send_chat_alert(message)
    print(message)

else:
    print('OUT OF STOCK') 
    exp_quant = stock_avl['restocks'][0]['quantity']
    earliest_date = stock_avl['restocks'][0]['earliestDate']
    reliability = stock_avl['restocks'][0]['reliability']

    # alerts.send_chat_alert(f"Expecting {exp_quant} pieces to be in stock as early as {earliest_date}  ({reliability} reliability)")
    
    print(f"Expecting {exp_quant} pieces to be in stock as early as {earliest_date}  ({reliability} reliability)")

