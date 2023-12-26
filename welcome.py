import os
import time
from data import inventory

class profile():
    gender = ''
    name = ''
    age = int() 

    def profile_setup(self):
        print("Aetherion: May I know your gender?")
        while profile.gender == '':
            temp = input("Enter your gender (Male, Female, Other): ")
            if temp == 'Male' or temp == 'male':
                profile.gender = 'Male'
            elif temp == 'Female' or temp == 'female':
                profile.gender = 'Female'
            elif temp == 'Other' or temp == 'other':
                profile.gender = 'Other'
            else:
                print("Please try again.")

        print("Aetherion: Understood, May I also know what your name could be?")
        profile.name = input("Enter your name: ")

        print(f"Aetherion: Well then {profile.name}, Can you tell me your age too?")
        profile.age = int(input("Enter your age: "))

        os.makedirs('com.eldoria.enigma', exist_ok = True)
        with open('com.eldoria.enigma/profile.enigma', 'w') as file:
            file.write(f"profile.gender: {profile.gender}\nprofile.name: {profile.name}\nprofile.age: {profile.age}")
        
        welcome.firsttext()
        welcome.mothertext()
     

    def check_profile(self):
        os.makedirs('com.eldoria.enigma', exist_ok = True)
        profile = {}
        with open('com.eldoria.enigma/profile.enigma', 'r') as file:
            for line in file:
                key, value = line.strip().split(": ")
                profile[key] = value 
        return profile.get("profile.gender"), profile.get("profile.name"), profile.get("profile.age") 


class welcome():

    def start(self):
        print('\n\nWelcome to the mystical realm of Eldoria, a land steeped in magic and mystery. In Eldoria, a powerful artifact known as the "Crystal of Eternity" holds the balance between light and darkness. For centuries, the crystal has been safeguarded by the Eldorians, an ancient order of magical beings. However, a sinister force, known as the Shadow Cult, has risen to seize the Crystal of Eternity and plunge Eldoria into eternal darkness.')
        time.sleep(5)
        print("Eldorius The Wise was a great man who fought until his last breadth to save the crystal of Ethernity from falling into the hands of evil. However he was killed by Malik The ShadowMaster, the head of the Shadow Cult.")
        time.sleep(5)
        print("Eldorius was your mentor so after his death you decided to join the adventurer's guild and walk on the same footsteps as your mentor and defeat the ShadowMaster.")
        time.sleep(5)
        print("Let's start by filling the form for Adventurer's guild. Aetherion is the cheif of Adventurer's guild and will guide you further ahead\n\n")
        time.sleep(5)

    def firsttext(self):
        print("\nAetherion: Congratulations your guild application form has been filled successfully.")
        time.sleep(1)
        print("You: Thank you very much professor, Can I start on doing the tasks now?")
        time.sleep(1)
        print(f"Aetherion: Not so fast{profile.name}. Remember what your mom said, You need to meet your mom first before starting your adventure")
        time.sleep(1)
        print(f"Aetherion: Ok I will go meet her.")

    def mothertext(self):
        print("\nYou reached at your home\n")
        time.sleep(2)
        print("Mother: Oh! You already became a member of the guild.") 
        time.sleep(1)
        print("Mother: Take care on your journey son") 
        time.sleep(2)
        print("You: Thank you mom. I think I should be going for now.")
        time.sleep(1)

        
welcome = welcome()
profile = profile()