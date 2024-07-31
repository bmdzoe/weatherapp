import requests
api_key = "b812ffbcf5b7db7a5278f1a1e50f9a64"
user_input= input("enter city: ")
weather_data= requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json()['cod'] == '404':
    print("No City Found")
else: 
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f"The weather today in {user_input} is {weather}")
    print(f"The tempature today in {user_input} is {temp} °F")
