from welcome import *
from functions import *


try:
    profile.gender, profile.name, profile.age = profile.check_profile()
    backend.load_inventory()
    backend.load_location()
except:
    if profile.gender == '':
        welcome.start()
        profile.profile_setup()
        backend.save_inventory()
        backend.save_location()


while True:
    command = int(input("\nChoose your option:\n1. Play\n2. Items\n3. Profile\n4. Quit\n")) 

    try:

        if command == 1:

            while True:
                command = int(input("\nChoose your option:\n1. Explore\n2. Scan\n3. Quest\n4. Quit\n"))

                try:
                    if command == 1: 
                        game.explore()
                    if command == 2:
                        game.scan()
                    if command == 3: 
                        continue
                    if command == 4:
                        backend.save_location()
                        break 
                except:
                    print("Enter the correct command")


        elif command == 2:
            options.items()
        elif command == 3:
            options.profile()
        elif command == 4:
            backend.save_inventory() 
            break
    except:
            print("Enter the correct command.")