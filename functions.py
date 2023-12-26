from data import *
import time
class options():

    def profile(self):
        while True:
            print(f"\nYour Profile:\nName: {profile.name}\nGender: {profile.gender}\nAge: {profile.age}")
            input("Press Enter to go back to the options menu: ")
            break
        

    def items(self):
        while True:
            print("\nItems: ")
            count = 1
            for item in inventory:
                print(f"{count}: {item}")
                count += 1
            input("Press Enter to go back to the options menu: ")
            break
            

class backend():

    def save_inventory(self):
        with open('com.eldoria.enigma/inventory.enigma', 'w') as file:
            for item in inventory:
                file.write(f"{item}\n")
    
    def load_inventory(self):
        global inventory
        with open('com.eldoria.enigma/inventory.enigma', 'r') as file:
            inventory = [line.strip() for line in file]

    def save_location(self):
        with open('com.eldoria.enigma/location.enigma', 'w') as file: 
            file.write(f"{location}")

    def load_location(self):
        global location
        with open('com.eldoria.enigma/location.enigma',  'r') as file:
            for line in file:
                location = (f"{line.strip()}")


class game():

    def explore(self):
        while True:
            global location
            print(f"\nYou are currently at {location}.\nChoose your destination:\n")
            count = 1
            for place in Area[location]:
                if type(place) == list:
                    print(f"{count}. Go to {place[1]} through {place[0]}")
                    count += 1
                else:
                    print(f"{count}. Go to {place}")
            temp = int(input("Where do you want to go: "))
            choice = temp - 1
            if type(Area[location][choice]) == list:
                if Area[location][choice][1] == "City of Jewels" and "Holy Sword" not in inventory:
                    print("Aldorin: City lf Jewels is taken over by shadow cult and you aren't strong enough to defeat shadowcult members. You should not go there now.")
                elif Area[location][choice][1] == "Mysthaven" and "Fog Clearer" not in inventory:
                    print("Oh no the fog. I can't see anything.\nHow did I reached here")
                    locaion = "Celestria"
                else:
                    location = Area[location][choice][1]
            else:
                location = Area[location][choice]
    
    def scan(self):
        global location_element
        print(f"\nThe Places in you can visit in {location} are:\n")
        count = 1 
        for item in Area_elements[location]:
            print(f"{count}. {item}")
            count += 1
        temp = int(input("What would you like to visit: "))
        location_element = Area_elements[location][temp - 1] 
        print(f"\nYou are now in {location_element}")
        scan.location_element_function()
        

class scan():

    def location_element_function(self):
        global location_element
        if location_element == '':
            pass
        elif location_element == 'Your House':
            temp = int(input(f"What would you like to do: \n1. Talk to mom\n2. Go Back\n"))
            if temp == 1:
                print("Mom: Take care son. I hope you turn out to be just like your mentor, Eldorius the wise.")
            else:
                pass
        elif location_element == "Someone's House":
            print("I shouldn't just barge into someones house like that")
        elif location_element == "Lyra's Enchantment Store":
            print("Lyra: This is my enchantment store but is closed until I finish my expedition to kill him. I sure hope to return to my store soon.")
        elif location_element == "Guildcenter":
            story.guildcenter()
        elif location_element == "Eldorius's Statue":
            print("This is the statue of the great warrior Eldorius The Wise")
        elif location_element == "A Pond":
            print("What a beautiful Pond. I wonder if I can fish here")
        elif location_element == "Celestria's Circus":
            print("Lyra: This is the most famous circus of Eldoria. I once came to this place with my mother while I was still a child.")
        elif location_element == "Celestria's Mart":
            print("Dev: Marts are still in development.")
        elif location_element == "Backyard":
            print("You: Who could have imagined there could be such a beautiful place in Eldoria.\nLyra: Can't argue about that. I know Malik once came here, do you think he could have hidden something in this plce? Should we searvh this place around")
        elif location_element == "Rebellion's Residence":
            print("Someone: Hey, Who are you? What are you doing here? Are you with the mayor too.\nYou: No we are just some adventurers wanderng around the place.\nLyra: Who are you people and why are you armed with magical Weapons like that.\nRebellion's Leader: We are the rebellion's of Emberfall. Our new mayor was elected a few months ago. But the mayor turned out to believe that The Red Waterfall is the devil's doing and the reason for all the chaos in the world. That's why he is trying to destroy it and we the Rebellion's are here to stop the mayor from destroying our waterfall")
            if 'Myst Clearer' not in inventory:
                print("Rebellion's Leader: Here take this as a gratitute for coming to our place\n\n")
                time.sleep(2)
                print("You recieved a Fog Clearer")
                time.sleep(3)
                inventory.append('Fog Clearer')
            else:
                print("Rebellion's Leader: Now you should probably get going from here before getting mixed up in this more.")
        elif location_element == "The Red Waterfall":
            print("Lyra: The Red Waterfall is a amazing waterfall. The waterfall has a red colour for some unknown reason. That's why it is believed to be holy water for some people and Devil's doing for others.")
        elif location_element == "Jewellery Shop":
            print("Dev: Marts are still on development")
        elif location_element == "Shadow Hideout":
            story.hideout()
        elif location_element == "Eldoria's Museum":
            print("You: Lyra, it is the famous museum that everyone in the village used to talk about.\nLyra: Yes it is. It is also the place where the crystal of ethernity was placed before it was stollen by the Shadow Cult. That the reason shadow cult took over this place.")
        elif location_element == "Brook's House":
            if 'Key' not in inventory:
                print("Brook: Hey, Are you people adventurers. I was a adventurer just like you in my old day.In fact, I was in the same team as the person you all might know as the great hero Eldorius. But it all changed that day when Malik came to the City of Jewels. At that time the our whole life turned upside down. We were driven to darkness when most of our team members were killed by Malik and his Army. Even though Eldorius fought that guy until his last breath even he was unable to defeat Malik and his team. However I know that someday peole like you will be able to get the crystal back and return the light and prosperity of Eldoria once again.")
                time.sleep(5)
                print("Here take this with you. It's a key that Malik drooped while we were fighting each other. You might need it.")
                time.sleep(2)
                print("You have recieved a Key")
                time.sleep(3)
                inventory.append("Key")
            else:
                print("I hope for the best for you. Go and bring back peace to this world.")
        elif location_element == "Train Station":
            story.train()
        elif location_element == "Jeremy's House":
            if "Good Luck Bracelet" not in inventory:
                print("Jeremy: Hello there friend. I am Jeremy. Here take this if you have this you will get what you want. ")
                time.sleep(2)
                print("You recieved a Good Luck Bracelet")
                time.sleep(3)
                inventory.append("Good Luck Bracelet")
            else:
                print("Have a nice day.")
        elif location_element == "Solstice's Arena":
            print("The Arena is currently closed.")
        elif location_element == "Malik's House":
            print("Lyra: This is the that Malik used to live in the old days. It reminds me of that time before the incident that changed Malik and this whole Kingdom")
        elif location_element == "Ruined Guildcenter":
            print("Lyra: This was the guildcenter of Rogue Town back in the days when both Malik and my father used to work in the same team as a adventurer\nYou: Wait so you mean you were born in this town too.\nLyra: Yes, I was still a young girl when that Malik decided to obtain the crystal of ethernity and obtain what he wants.")
        elif location_element == "Ancient Ruins":
            story.ruins()
        elif location_element == "Graveyard":
            story.graveyard()
        elif location_element == "Ghosted House":
            time.delay(2)
            print("A strange figure appears")
            time.delay(2)
            print("Get out of this house right now")
        elif location_element == "A Strange Sign":
            print(f"I am waiting to meet you {profile.name} - Malik")
        elif location_element == "Eldoria's Palace":
            story.palace
        elif location_element == "Wishing Well":
            print("You: I wish that Lyra's soul can rest in heaven and soon see the light that will soon rise on the land of Eldoria")
        elif location_element == "Shipping Area":
            story.ship()
        elif location_element == "Local Mart":
            print("Marts are currently in development.")
        location_element = ''
        input("Press enter to quit: ")
        pass

class story():

    def guildcenter(self):
        print(f"Alderion: Hello there {profile.name}. Are you here to see if there are any tasks available.\nYou: Yes, I am actually. Could you see if I have any quest to complete")
        try:
            if current_task == []:
                current_task = task.pop[0]
                print("Your new task is to", current_task)
            else:
                print("Alderion: You already have a uncompleted quest. Please finish that quest first.")
        except:
            print("There aren't any tasks available currently.")
    
    def hideout(self):
        if 'Invitation Letter' not in inventory:
            print(f"Shodow Cult Member: Wait right there boy.Who gave you the permission to barge in here like that.\n\nAldorin: They look like they are a member of shadow cult, What are you going to do {profile.name}.\n\n")
            temp = int(input("Should I fight them or not.....\n1. Fight them\n2. Turn back and go"))
            if temp == 1:
                time.sleep(2)
                print("\nYou take your sword out")
                time.sleep(2)
                print("You: I think I need to fight and punish them for all that they have done to Eldoria. They must pay for their sins. Help me kill them Eldorius.")
                time.sleep(2)
                print("You kill all of the shadow cult members present with one blow.")
                time.sleep(2)
                pint("A strange voice appeared")
                time.sleep(2)
                print(f"Malik: Congratulations, {profile.name}. You were able to kill all of my people with a single blow. Here take this as a reward {profile.name}.")
                time.sleep(2)
                print("You recieved a Invitation Letter")
                time.sleep(2)
                inventory.append("Invitation Letter")
                print("Malik: I wish to see you soon.")
            else:
                pass
        else:
            print("You: I am going to kill you Malik. No matter what.")
    
    def train(self):
        global location
        if "Train Pass" in inventory:
            if location == "Stonegate":
                print("Choose where would you like to go")
                temp = int(input("1. City of Death\n2. Solstice City"))
                if temp == 1:
                    location = "City of Death"
                    print(f"You have reached your destination{location}")
                elif temp == 2:
                    location == "Solstice City"
                    print(f"You have reached your destination{location}")
                else:
                    print("Please Enter the correct command")
            if location == "Solstice City":
                print("Choose where would you like to go")
                temp = int(input("1. Stonegate"))
                if temp == 1:
                    location = "Stonegate"
                    print(f"You have reached your destination{location}")
                else:
                    print("Please Enter the correct command")
            if location == "City of Death":
                print("Choose where would you like to go")
                temp = int(input("1. Stonegate"))
                if temp == 1:
                    location = "Stonegate"
                    print(f"You have reached your destination{location}")
                else:
                    print("Please Enter the correct command")

    def ruins(self):
        if 'Ruins' not in visited:
            print("Lyra: This is the place where it all started\nYou: What do you mean it all started.\nLyra: This is the place where Malik's whole life got ruined. During that day my father and Malik went on to explore the ancient ruins. They were directly ordered to explore the ruins and retreve the Holy Sword by the king of Eldoria. When they both retrieved the sword and were coming out of the ancient ruins they saw the horrible state of this town. The king and his men had already killed all of the villagers including Malik's family. So they decided to hide the sword in this ancient ruins and fought the king. They killed the king but Malik was in a despair after that incident. He thought that this world didn't deserved to exist and stole the crystal of ethernity to fulfill his purpose.")
            time.sleep(5)
            print("You: How do you know about all of this Lyra and who was your father, he seems like a great warrior to have fought and defeated the king with it's whole army.\nLyra: My father is the person you all know as Eldorius the wise but we should focus on getting our hands on the Holy Sword for now.Look I found it and there is something else too, it looks a train pass. Here take this you should weild the sword after all your sword skills are greater than mine.")
            time.sleep(2)
            print("You recieved a sword and Train Pass")
            time.sleep(3)
            inventory.append("Train Pass")
            inventory.append("Sword")
            visited.append("Ruins")

        else:
            print("**So this is where it all started, huh!**")
    
    def graveyard(self):
        global dead
        if "Lyra" not in dead:
            print("You: Wait where are we.\nLyra: This seems to be some kind of graveyard. Look there is someone over there maybe we should ask them for direction")
            time.sleep(2)
            print("You approach the unknown person.")
            time.sleep(2)
            print(f"Lyra: {profile.name} stop. He is Malik.\nYou take your sword out and attack Malik.\Malik cuts the sword in half with his sword.\nMalik: I have been expecting you {profile.naem}. I thought you would be a good warmup for me but seeing your foolishness, I have started to doubt that you think that really was the holy sword. No it's just a replica of the sword the real sword is hidden inside the palace of eldoria. Maybe my expectations were for nothing I think I should kill you you now.\nMalik tries to slash you with the sword but it is block =ed by Lyra.\nYou: Wait Lyra, you are bleeding.\nLyra: It's no use now {profile.name}. Just live and return the crystal of Ethernity to it's original place.\nMalik: Looks like your friend saved your life so just live on for now, until we meet again {profile.name}\nMalik disappeared.")
            inventory.remove("Sword")
            dead.append("Lyra") 
        else:
            print("I will never forget your kindness Lyra.")
    def palace(self):
        if 'Holy Sword' not in inventory:
            print(f"**Why doesn't anybody live in here. I wonder if it is Malik's doing.**\nAldorin: Look {profile.name}, That's the holy sword take it you might need it.")
            time.sleep(2)
            print("You recieved a Holy Sword")
            inventory.append("Holy Sword")
            print("Aldorin: You have the holy sword now. I think you are now powerful enough to go to City of Jewels.")
        else: 
            print("Where are all the people of the palace.")
    def ship(self):
        if "Invitation Letter" in inventory():
            print("Dev: Please wait until we finish the preparation of Shadowmere")                            
        else:
            print("You need a ticket to enter.")
            
game = game() 
options = options()
backend = backend()
scan = scan()