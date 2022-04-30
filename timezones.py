from datetime import datetime
import pytz
# use this link to find the timexone database name that will be used with .timezone()
#  https://en.wikipedia.org/wiki/List_of_tz_database_time_zones 
my_city_timezone = pytz.timezone('America/Bogota') #this one is the timezone for Bogotá
my_city_time = datetime.now(my_city_timezone) #with this, the function .now() brings the specific time for the TZ we requested with pytz.timezone()
print("Bogotá:", my_city_time.strftime("%d/%m/%Y, %H:%M:%S"))

my_city_timezone = pytz.timezone('America/Mexico_City') #same here for méxico city
my_city_time = datetime.now(my_city_timezone)
print("Ciudad de México:", my_city_time.strftime("%d/%m/%Y, %H:%M:%S"))

my_city_timezone = pytz.timezone('America/Caracas') #same here for caracas
my_city_time = datetime.now(my_city_timezone)
print("Caracas:", my_city_time.strftime("%d/%m/%Y, %H:%M:%S")) # con strftime, ponemos el formato exacto que queremos para este caso. 