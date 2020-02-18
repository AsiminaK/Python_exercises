import random
fan1 = "RED"
fan2 = "RED"
fan3 = "RED"
pl1 = random.randint(0,20)
pl2 = random.randint(0,20)
pl3 = random.randint(0,20)
choose = 0
STOP = pl1 + pl2 + pl3
while STOP!=0:
   meg = max(pl1,pl2,pl3)
   if (pl1 == meg) and (pl2 == meg):
       choose = random.randint(1, 4)
   elif (pl1 == meg) and (pl3 == meg):
       choose = random.randint(1, 4)
   elif (pl2 == meg) and (pl3 == meg):
       choose = random.randint(1, 4)
   right = 0
   if ((pl1 == meg) and (pl2 < meg) and (pl3 < meg)) or (choose == 1):
       fan1 = "GREEN"
       while right == 0:
         cars = random.randint(5, 10)
         pl1 = pl1 - cars
         if pl1 >= 0:
          right = 1
       cars_coming1 = random.randint(1, 5)
       cars_coming2 = random.randint(1, 5)
       pl2 = pl2 + cars_coming1
       pl3 = pl3 + cars_coming2
       print("Το φανάρι έχει",pl1,"αυτοκίνητα!")
   elif ((pl2 == meg) and (pl1 < meg) and (pl3 < meg)) or (choose == 2):
       fan2 = "GREEN"
       while right == 0:
         cars = random.randint(5, 10)
         pl2 = pl2 - cars
         if pl2 >= 0:
           right = 1
       cars_coming1 = random.randint(1, 5)
       cars_coming2 = random.randint(1, 5)
       pl1 = pl2 + cars_coming1
       pl3 = pl3 + cars_coming2
       print("Το φανάρι έχει",pl2,"αυτοκίνητα!")
   elif ((pl3 == meg) and (pl2 < meg) and (pl1 < meg)) or (choose == 3):
       fan3 = "GREEN"
       while right == 0:
        cars = random.randint(5, 10)
        pl3 = pl3 - cars
        if pl3 >= 0:
         right = 1
       cars_coming1 = random.randint(1, 5)
       cars_coming2 = random.randint(1, 5)
       pl2 = pl2 + cars_coming1
       pl1 = pl3 + cars_coming2
       print("Το φανάρι έχει",pl3,"αυτοκίνητα!")
   print("Φεύγουν",cars,"αυτοκίνητα!")
   print("Έρχονται στα άλλα δύο φανάρια",cars_coming1 + cars_coming2,"αυτοκίνητα!")
   STOP= pl1 + pl2 + pl3
