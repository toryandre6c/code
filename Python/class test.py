class player:
    def __init__(self, nickname):
        self.name = nickname
        
x = input("player1 enter your name ")
y = input("player2 enter your name ")
Player1 = player(x)
Player2 = player(y)
print(Player1.name)        
print(Player2.name)