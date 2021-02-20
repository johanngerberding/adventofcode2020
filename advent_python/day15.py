from collections import Counter
import time 

INPUT = [20,0,1,11,6,3]
TEST = [1,3,2]
TEST_2 = [2,1,3]
TEST_3 = [0,3,6]

class GameCounter:
    def __init__(self, inputs):
        self.inputs = inputs 
        self.counts = Counter(inputs)
        self.count = {v: {'count': 0, 'last_idx': -1, 'last_idx_2': -1} for v in self.inputs}
        for idx, el in enumerate(self.inputs):
            self.count[el]['count'] += 1
            self.count[el]['last_idx_2'] = self.count[el]['last_idx']
            self.count[el]['last_idx'] = idx 
            
            

    
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
    

    def big_step(self):
        last_el = self.inputs[-1]
        last_el_count = self.count[last_el]['count']
        num_inputs = len(self.inputs)
        if num_inputs >= 30000000:
            return False
        if last_el_count == 1:
            self.inputs.append(0)
            self.count[0]['count'] += 1
            self.count[0]['last_idx_2'] = self.count[0]['last_idx']
            self.count[0]['last_idx'] = num_inputs
            return True
        elif last_el_count > 1:
            diff = self.count[last_el]['last_idx'] - self.count[last_el]['last_idx_2']
            self.inputs.append(diff)
            if diff in self.count.keys():
                self.count[diff]['count'] += 1
                self.count[diff]['last_idx_2'] = self.count[diff]['last_idx']
                self.count[diff]['last_idx'] = num_inputs
            else:
                self.count[diff] = {'count': 1, 'last_idx': num_inputs, 'last_idx_2': -1}
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
        
""" counter = GameCounter(TEST_3)
while True:
    done = counter.big_step()
    if not done:
        break

print(counter.inputs[-1]) """

counter = GameCounter(INPUT)
while True:
    done = counter.big_step()
    if not done:
        break

print(counter.inputs[-1])