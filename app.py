# importing the requests library
from os import system, environ
import requests
import webbrowser
from termcolor import cprint
from app import Misc

APIKEY = environ['GOOGLE_MAP_APIKEY']

#printcolor
prc = lambda x: cprint(' ' + x, 'cyan')
pry = lambda x: cprint(' ' + x, 'yellow')
prr = lambda x: cprint(' ' + x, 'red')

system('clear')

Sign = Misc.Sign
Sign.logo('white')
# api-endpoint
URL = "https://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = input(" Lokasi yang anda cari: ")

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location,'key':APIKEY}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

if data["status"] == "INVALID_REQUEST":
    Sign.logo('red')
    prr("\n -- MAAF DATA TIDAK DITEMUKAN --")
    exit()

Sign.logo('cyan')
# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
address_types = data['results'][0]['address_components']
link = "https://www.google.com/maps/place/"+formatted_address

# printing the output
pry('## KATA KUNCI #####')
prc(location)

pry('\n ## KORDINAT #######')
prc("Latitude       : " + str(latitude))
prc("Longitude      : " + str(longitude))

pry('\n ## DETAIL INFO ####')
prc("Format Lokasi  : " + formatted_address)
prc("Tipe Alamat    : " + address_types[0]['types'][0].replace("_"," ").title())
pry('\n ## BREAKDOWN ######')
for i,x in enumerate(address_types):
    loc_type = x["types"][0].replace("area","").replace("_"," ").title()
    loc_type = loc_type.replace("Level ","Lv-")
    loc_type = loc_type.replace("Street Number","St. Number")
    loc_type = loc_type.replace("Administrative ","Adm.")
    loc_name = x["long_name"].title()
    number = str(i + 1)
    type_len = 12 - len(loc_type)
    for x in range(type_len):
        loc_type = loc_type + " "
    prc(number+". "+ loc_type + ": " + loc_name)



# what to do
while True:
    d1a = input ("\n Buka Google Maps Seakarang. [ya/tidak]? : ")
    if d1a in ['ya', 'tidak', 'y', 't']:
       break
if d1a == "ya" or d1a == "y":
    webbrowser.open_new_tab(link)
elif d1a == "tidak" or d1a == "t":
    print ("Terima Kasih.")
