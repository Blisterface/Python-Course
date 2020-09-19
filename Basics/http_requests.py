import requests


#my_request = requests.get('http://go.codeschool.com/spamvanmenu')
#menu_list = my_request.json()
#print(menu_list)

#import requests
  
url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=2de143494c0b295cca9337e1e96b00e0"
request = requests.get(url)

weather_json = request.json()
print(weather_json)