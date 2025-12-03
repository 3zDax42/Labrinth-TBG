#Labrinth type game -- You must go the same direction 3 times in a row to excape

class Player:
    def __init__(self):
        self.HP = 50
        self.Direction = None
        self.Last_Direction = None
        self.Number_Of_Same_Direction = 0
        self.Golden_Feather = 0
        self.Items = []

player = Player()

# Room gives decription based on where you are and remembers where you were last turn, but auto generates all other directions
# Start room
Room_Decriptions = {
    "Start_Room" : "The area around is covered in a heavy mist. It's hard to see anything too far ahead.",
    "Soft_Medow" : "The area here is very calming, nothing seems to make any nose in respect to the land."
}

while player.HP > 0 and player.Number_Of_Same_Direction <= 3:
    pass
