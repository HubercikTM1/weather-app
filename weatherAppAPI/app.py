import requests
import PySimpleGUI as psg 

api = '3aa8355b362347f593d171604231609'

city = input('Enter city: ')
print(f'{city}')

weather_data = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api}&q={city}&aqi=no")

# if weather_data.json()['cod'] =='404': #cod - status code that the api returns
#     print("No City Found")
# else:
print(weather_data.json())

date_and_time = weather_data.json()['current']['last_updated']
temperature = weather_data.json()['current']['temp_c']
print(f'date and time: {date_and_time}\ntemperature: {temperature} °C')

layout = [[psg.Text(city)], [psg.Text(date_and_time)], [psg.Text(temperature)], [psg.Button("close")]]
window = psg.Window(city, layout, margins=(100,50))
isRunning = True

while isRunning:
    event, values = window.read()

    if event == "close" or event == psg.WIN_CLOSED:
        break

window.close()
