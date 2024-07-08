# File: script.py
API_KEY = "AIzaSyA1B2C3D-4E5F6G7H8I9J0K1L2M3N4O5P"

def get_data():
    url = f"https://api.giguardian.com/data?api_key={API_KEY}"
    response = requests.get(url)
    return response.json()

data = get_data()
print(data)
