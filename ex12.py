
import datetime
from datetime import datetime,time
year = input("Πληκτρολογήστε ένα έτος: ")
month = input("Πληκτρολογήστε έναν μήνα: ")
day = input("Πληκρολογήστε μία ημερομηνία: ")
month1=int(month)
year1=int(year)
day12= year+'-'+month+'-'+day
date12= datetime.strptime(day12, "%Y-%m-%d")

if month1 == 2:
    if year1 % 4 == 0:
        print("Ο μήνας έχει 29 μέρες!")
    else:
        print("O μήνας έχει 28 μέρες!")

if (month1 < 8) and (month1 != 2):
    if month1 % 2 == 0:
        print("Ο μήνας έχει 30 μέρες!")
    else:
        print("Ο μήνας έχει 31 μέρες!")
elif month1 >= 8:
    if month1 % 2 == 0:
        print("Ο μήνας έχει 31 μέρες!")
    else:
        print("Ο μήνας έχει 30 μέρες!")

today = datetime.now()

def date_diff_in_seconds(dat2, dat1):
  timedelta = abs(dat2 - dat1)
  return timedelta.days * 24 * 3600 + timedelta.seconds
def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)
day1 = date12
day2 = today
print("H ημερομηνία που δώσατε απέχει απο την σημερινή κατα \n%d μέρες, %d ώρες, %d λεπτά, %d δευτερόλεπτα" % dhms_from_seconds(date_diff_in_seconds(day2, day1)))

