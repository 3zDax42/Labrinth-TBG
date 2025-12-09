#Labrinth type game -- You must go the same direction 3 times in a row to excape
# Colored text - ANSI escape =
# Red = '/033[91m
# END = '/033[0m
# print(Red + "Text" + END)
global Running; Running = True
class Player:
    def __init__(self):
        self.HP = 50
        self.Direction = None
        self.Last_Direction = None
        self.Number_Of_Same_Direction = 0
        self.Current_Room = "Start_Room"
        self.Last_Room = None
        self.North_Room = None; self.East_Room = None; self.South_Room = None; self.West_Room = None
        self.Room_Map = (self.North_Room, self.East_Room, self.South_Room, self.West_Room)
        self.Golden_Feather = 0
        self.Items = []
    def Process_Input(self):
        self.Input = input().capitalize
        if self.Input == "Help":
            self.Help()
        elif self.Input == "Q":
            global Running; Running = False
        elif self.Input == "R":
            self.Reset()
        elif self.Input == "I":
            for i in range(len(self.Items)):
                print(i)
        elif self.Input == "N" or self.Input == "North":
            self.Direction = "North"
            #Check if realy want to go this way
            if (self.Input == "N" or self.Input == "North" or self.Input == "Y" or self.Input == "Yes"):
                if self.Direction == self.Last_Direction:
                    self.Number_Of_Same_Direction += 1
    def Next_Rooms(self):
        if self.Number_Of_Same_Direction == 3:
            pass#self.Last_Direction
    def Reset(self):
        self.HP = 50
        self.Direction = None
        self.Last_Direction = None
        self.Number_Of_Same_Direction = 0
        self.Current_Room = "Start_Room"
        self.Golden_Feather = 0
        self.Items = []
    def Help(self):
        print("Press 'q' to quit")
        print("Press 'r' to restart the game")
        print("Press 'i' to view your items")
        print("Press 'n' or 'north' to go north")
        print("Press 'e' or 'east' to go east")
        print("Press 's' or 'south' to go south")
        print("Press 'w' or 'west' to go west")

player = Player()

# Room gives description based on where you are and remembers where you were last turn, but auto generates all other directions
# Start room
Room_Decriptions = {
    "Start_Room" : "The area around is covered in a heavy mist. It's hard to see anything too far ahead.",
    "Soft_Medow" : "The area here is very calming, nothing seems to make any nose in respect to the land.",
    "Willow_Tree": "There's a willow tree not too far from away. It's eerily silent here and it feels like something is watching.",
    "Rocky_Path" : "There are a lot of loose sharp stones around here and the ground is uneven. It's very easy to trip.",
    "Hot_Spring" : "There seems to be a natural hot spring here. The water looks pleasantly warm.",
    "Dark_Forest": "The area quickly becomes dark because of the number of trees. Nothing seems to move here, not even the mist.",
    "Old_Ruins"  : "The area is filled with the ruins of civilizations passed. Maybe something valuable was left behind.",
    "Ash_Forest" : "The heavy mist gives way to a stunning view of burned trees covered in ash rather than leaves. Staying here might not be a good idea.",
    "River_Side" : "There is a stream here. The water looks clean, but drinking it might not be a good idea.",
    "Single_Tree": "Through the mist there is a single tree standing tall. If it wasn't for the mist it would be a nice place to take a nap.",
    "Dense_Mist" : "The mist is so thick here that no one would be able to see even a meter ahead. Could animals even live here?",
    "Lake_Side"  : "There is a large lake ahead. The water has a black colored patten comming from the center. What's in there?",
    "Cave_Opening" : "There is a cliff with a cave opening ahead. There are huge spider webs within the cave, how would spiders spin webs so large?",
    "Geyser_Mine": "Every so often jets of steam erupt from the ground. It's dangerous to stay here, but this place might explain the ever present mist.",
    "End_Room_1" : "What is this place? Why is everything white here? What happend to the mist?",
    "End_Room_2" : "Why? Why did you create this twisted place, \"Player\"? Does seeing the suffering of others cause you joy?"
} #Another person! Maybe they know something about this place.

while player.HP > 0 and player.Number_Of_Same_Direction <= 3 and Running == True:
    player.Process_Input()
