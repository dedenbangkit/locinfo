# locinfo
Search location with Google Maps API

## Basic Installation

Before you run the installation, you must generate Google APIKEY with Maps, Routes and Places services enabled, to Generate new API KEY:

- Go to the [Google Maps Platform](https://cloud.google.com/maps-platform/)
- Click 'Get Started'
- Check 'Maps', 'Routes' and 'Places'
- If you want to use an existing project, please select it from the list. Otherwise, select 'Create a new project' and enter a project name.
- Click 'Next' to enable the APIs for the project
- Copy the generated API key from the popup, you'll need this to set your key later.

```
$ git clone https://github.com/dedenbangkit/locinfo 
$ sh locinfo/run.sh
$ export GOOGLE_MAP_APIKEY='YOUR_GOOGLE_MAP_APIKEY'
``` 

## Usage

```
$ locinfo

 ██╗      ██████╗ ██╗  ██╗ █████╗ ███████╗██╗
 ██║     ██╔═══██╗██║ ██╔╝██╔══██╗██╔════╝██║
 ██║     ██║   ██║█████╔╝ ███████║███████╗██║
 ██║     ██║   ██║██╔═██╗ ██╔══██║╚════██║██║
 ███████╗╚██████╔╝██║  ██╗██║  ██║███████║██║
 ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝

Lokasi yang anda cari: Jl. Tukad Badung XI no 3 

## KATA KUNCI #####
Jl. Tukad Badung XI no 3

## KORDINAT #######
Latitude       : -8.684997599999999
Longitude      : 115.240134
 
## DETAIL INFO ####
Format Lokasi  : Jl. Tukad Badung XI No.30, Renon, Denpasar Sel., Kota Denpasar, Bali 80226, Indonesia
Tipe Alamat    : Street Numbe

## BREAKDOWN ######
1. St. Number  : 30
2. Route       : Jalan Tukad Badung Xi
3. Adm. Lv-4   : Renon
4. Adm. Lv-3   : Denpasar Selatan
5. Adm. Lv-2   : Kota Denpasar
6. Adm. Lv-1   : Bali
7. Country     : Indonesia
8. Postal Code : 8022

Buka Google Maps Seakarang. [ya/tidak]? : ya // open new google maps within the location
```

## License
MIT
