TEST = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""


class Player: 
    def __init__(self, name, deck):
        self.name = name 
        self.deck = deck
        self.history = []
    
    def __str__(self):
        return f"{self.name} deck: {self.deck}"

    def play_round(self, player2):
        card_1 = self.deck.pop(0)
        card_2 = player2.deck.pop(0)
        if card_1 > card_2:
            self.deck.append(card_1)
            self.deck.append(card_2)
        elif card_2 > card_1:
            player2.deck.append(card_2)
            player2.deck.append(card_1)
        else:
            print("Tie is not implemented!")



class Game: 
    def __init__(self, players):
        self.player_1 = players[0]
        self.player_2 = players[1]

    def play(self) -> int:
        i = 1 
        while len(self.player_1.deck) > 0 and len(self.player_2.deck) > 0:
            print(f"Round {i}")
            # check player history
            if self.player_1.deck in self.player_1.history or self.player_2.deck in self.player_2.history:
                print("Finished because of history")
                return 0
            else: 
                self.player_1.history.append(self.player_1.deck.copy())
                self.player_2.history.append(self.player_2.deck.copy())
                print(len(self.player_1.history))
                print(len(self.player_2.history))

            c1 = self.player_1.deck.pop(0)
            c2 = self.player_2.deck.pop(0)

            if len(self.player_1.deck) >= c1 and len(self.player_2.deck) >= c2:
                n_player_1 = Player(self.player_1.name, self.player_1.deck[:c1].copy())
                n_player_2 = Player(self.player_2.name, self.player_2.deck[:c2].copy())
                print("Start Subgame")
                winner = Game([n_player_1, n_player_2]).play()
                if winner == 0:
                    self.player_1.deck.append(c1)
                    self.player_1.deck.append(c2)
                else: 
                    self.player_2.deck.append(c2)
                    self.player_2.deck.append(c1)

            else: 
                if c1 > c2: 
                    self.player_1.deck.append(c1)
                    self.player_1.deck.append(c2)
                elif c2 > c1: 
                    self.player_2.deck.append(c2)
                    self.player_2.deck.append(c1)
                else: 
                    print("tie not implemented")
            
            i += 1 
        
        return 0 if len(self.player_1.deck) > 0 else 1 

  

data = TEST.split("\n")

def parse(raw: str) -> list:
    players = []
    data = raw.split("\n")
    while '' in data:
        idx = data.index('')
        vals = data[:idx]
        players.append(Player(vals[0][:-1], [int(i) for i in vals[1:]]))
        data = data[idx+1:]
    players.append(Player(data[0][:-1], [int(i) for i in data[1:]]))

    return players


players = parse(TEST)

game = Game(players)
res = game.play()
print(res)
print(game.player_1)
print(game.player_2)

"""
player_1 = players[0]
player_2 = players[1]

i = 1
while len(player_1.deck) > 0 and len(player_2.deck) > 0:
    print(f"Round {i}:")
    i += 1
    player_1.play_round(player_2)
    print(player_1)
    print(player_2)

res = 0
for i, c in enumerate(reversed(player_2.deck)): 
    res += ((i+1)*c)

print(res)"""


with open('../inputs/day22.txt', 'r') as f: 
    raw = f.read()

players = parse(raw)
game = Game(players)
res = game.play()
print(res)
print(game.player_1)
print(game.player_2)

"""
player_1 = players[0]
player_2 = players[1]

i = 1
while len(player_1.deck) > 0 and len(player_2.deck) > 0:
    print(f"Round {i}:")
    i += 1
    player_1.play_round(player_2)
    print(player_1)
    print(player_2)

"""
if len(game.player_1.deck) != 0:
    winner = game.player_1
else: 
    winner = game.player_2

res = 0
for i, c in enumerate(reversed(winner.deck)): 
    res += ((i+1)*c)

print(res)