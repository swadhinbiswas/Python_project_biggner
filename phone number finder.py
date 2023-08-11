import phonenumbers
from phonenumbers import timezone,geocoder,carrier
#input number
number=str(input("input number with country code:  "))
#phone number detiles
phone=phonenumbers.parse(number)
#time zone
time=timezone.time_zones_for_number(phone)
#company of number
carri=carrier.name_for_valid_number(phone,"en")
#Country of your number
registe=geocoder.description_for_number(phone,"en")

print(phone)

print(time)

print(carri)

print(registe)
