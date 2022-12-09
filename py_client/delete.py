import requests

product_id = input("Product ID \n")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not a valid product ID')
    
if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

data = {
    'title': 'Hello World',
    'price': 100,
}

get_response = requests.delete(endpoint, json=data)

#print(get_response.json())
print(get_response.status_code, get_response.status_code==204)
