TEST = "389125467"
INPUT = "653427918"

class CrabCups:
    def __init__(self, labeling):
        self.labeling = [int(el) for el in labeling]
        self.num_moves = 0


    def move(self):
        self.num_moves += 1
        print(f"labeling: {self.labeling}")
        print(f"move ({self.num_moves})")
        temp = self.labeling[4:].copy()
        dest = self.get_destination(temp, self.labeling[0])
        dest_idx = temp.index(dest)
        n_labeling = temp[:dest_idx+1] + self.labeling[1:4].copy() + temp[dest_idx+1:] + [self.labeling[0]]
        self.labeling = n_labeling


    @staticmethod
    def get_destination(sub_labeling, curr):
        assert len(sub_labeling) > 0
        dest = curr - 1 
        while True:
            if dest in sub_labeling:
                return dest 
            elif dest == 0:
                return max(sub_labeling)
            dest -= 1 
  

    



def main():
    game = CrabCups(INPUT)
    print(game.labeling)
    
    for _ in range(100):
        game.move()

    idx = game.labeling.index(1)
    res_1 = ''.join([str(el) for el in game.labeling[idx+1:]])
    res_2 = ''.join([str(el) for el in game.labeling[:idx]])
    res = res_1 + res_2 
    print(res)

if __name__ == "__main__":
    main()
