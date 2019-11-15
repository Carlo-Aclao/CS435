import math

class MaxHeap:

  def __init__(self):
    self.data = []

  def parent(self, index):
    return int((index-1)/2)

  def insert(self, value):
    data = self.data
    
    #add it to the end of the list
    data.append(value)

    index = len(data)-1

    #while the current index is bigger than it's parent, 
    #swap them and update index to the parent's index.
    while(data[index] > data[self.parent(index)]):
      data[index], data[self.parent(index)] = data[self.parent(index)], data[index]
      index = self.parent(index) 

  def remove(self, index):
    #swap the last element/node with the current index
    self.data[index], self.data[len(self.data)-1] = self.data[len(self.data)-1], self.data[index]
    #remove the last index
    del self.data[-1]

    #while there is a left node AND either of the children are bigger than the parent.
    while((index*2+1 < len(self.data)-1) and (self.data[index*2+1] > self.data[index] or self.data[index*2+2] > self.data[index])):

      if(self.data[index*2+1] > self.data[index*2+2]):
        #print('Left Swapping: ' + str(self.data[index]) + ' ' + str(self.data[index*2+1]))
        self.data[index], self.data[index*2+1] = self.data[index*2+1], self.data[index]
        index = index*2+1
      elif  (self.data[index*2+2] > self.data[index*2+1]):
        #print('Right Swapping: ' + str(self.data[index]) + ' ' + str(self.data[index*2+2]))
        self.data[index], self.data[index*2+2] = self.data[index*2+2], self.data[index]
        index = index*2+2

  def extractMax(self):
    maxH = self.data[0]
    self.remove(0)
    return maxH

  def getMax(self):
    return self.data[0]

  def isEmpty(self):
    return False if len(self.data) == 0 else True

  def printH(self):
    print(self.data)

h = MaxHeap()
print('INSERTING')
h.insert(1);
h.printH();
h.insert(2);
h.printH();
h.insert(3);
h.printH();
h.insert(4);
h.printH();
h.insert(5);
h.printH();
h.insert(6);
h.printH();
h.insert(7);
h.printH();
h.insert(8);
h.printH();
print('REMOVING 2th index!')
h.remove(2)
print('DONE REMOVING \n')

hSort = []
while(h.isEmpty()):
  hSort.append(h.extractMax())

print(hSort)