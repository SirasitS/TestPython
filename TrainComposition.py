import collections

class TrainComposition:
    
    def __init__(self):
        self.items = collections.deque()
    
    def attach_wagon_from_left(self, wagonId):
        print("Before append left =", self.items)
        self.items.appendleft(wagonId)         #self.items.append(wagonId)
        print("After append left =", self.items)
    
    def attach_wagon_from_right(self, wagonId):
        print("Before append right =", self.items)
        self.items.append(wagonId)     #self.items.insert(len(self.items)-1, wagonId)       #self.items.extend(wagonId)
        print("After append right =", self.items)

    def detach_wagon_from_left(self):
        return self.items.popleft()         #self.items.pop(len(self.items) - 1)
    
    def detach_wagon_from_right(self):
        return self.items.pop()             #self.items.pop(0)

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print("Detach right wagon =", train.detach_wagon_from_right()) # should print 7
    print("Detach left wagon =", train.detach_wagon_from_left()) # should print 13