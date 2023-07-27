import requests

lat = 37.56
lon = 126.97 


API_key = 'fc34f02819908d72c22e2235e7066962'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
data = requests.get(url).json()

print(data)