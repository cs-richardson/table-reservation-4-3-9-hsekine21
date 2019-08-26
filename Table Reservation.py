# Program that introduced customer to table if they have a reservation, if not
# then apologizes 

# Hina Sekine

reservation_name = 'Sandra'
name = input("Name: ")

if name == reservation_name:
    print("Right this way!")
else:
    print("Sorry, we don't have that reservation under that name.")
