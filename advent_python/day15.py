from collections import Counter

INPUT = [20,0,1,11,6,3]
TEST = [1,3,2]
TEST_2 = [2,1,3]

class GameCounter:
    def __init__(self, inputs):
        self.inputs = inputs 
        self.counts = Counter(inputs)
    
    def step(self):
        last_el = self.inputs[-1]
        last_el_count = self.counts[last_el]

        if len(self.inputs) >= 2020:
            return False
        if last_el_count == 1:
            self.inputs.append(0)
            self.counts = Counter(self.inputs)
            return True
        elif last_el_count > 1:
            idxs = [(i+1) for i in range(len(self.inputs)) if self.inputs[i] == last_el]
            self.inputs.append((idxs[-1] - idxs[-2]))
            self.counts = Counter(self.inputs)
            return True
        


counter = GameCounter(TEST)
while True:
    done = counter.step()
    if not done:
        break

assert counter.inputs[-1] == 1  

counter = GameCounter(TEST_2)
while True:
    done = counter.step()
    if not done:
        break

assert counter.inputs[-1] == 10

counter = GameCounter(INPUT)
while True:
    done = counter.step()
    if not done:
        break

print(counter.inputs[-1])
        
