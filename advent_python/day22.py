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
   

data = TEST.split("\n")
print(data)
print(data.index(''))
print(data[:6])

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

print(res)


with open('../inputs/day22.txt', 'r') as f: 
    raw = f.read()

players = parse(raw)
player_1 = players[0]
player_2 = players[1]

i = 1
while len(player_1.deck) > 0 and len(player_2.deck) > 0:
    print(f"Round {i}:")
    i += 1
    player_1.play_round(player_2)
    print(player_1)
    print(player_2)

if len(player_1.deck) != 0:
    winner = player_1
else: 
    winner = player_2

res = 0
for i, c in enumerate(reversed(winner.deck)): 
    res += ((i+1)*c)

print(res)