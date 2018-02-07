# importing the requests library
import requests
import webbrowser

# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"

# location given here
location = input("Lokasi yang anda cari: ")

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.json()

# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
link = "https://www.google.com/maps/place/"+formatted_address

# printing the output
print("\nLatitude:%s\nLongitude:%s\nFormat Alamat:%s\nLink:%s"
%(latitude, longitude,formatted_address, link))

# what to do
while True:
    d1a = input ("\nBuka Google Maps Seakarang. [ya/tidak]? : ")
    if d1a in ['ya', 'tidak']:
       break
if d1a == "ya":
    webbrowser.open_new_tab(link)
elif d1a == "tidak":
    print ("\nTerima Kasih.")

