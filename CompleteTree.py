import queue

class Node:
    def __init__(self, d):
        self.left = None
        self.right = None
        self.data = d
        
def fromArray(arr, root, i, n):
    if i < n:
        root = Node(arr[i])
        
        root.left = fromArray(arr, root.left, i*2+1, n)
        root.right = fromArray(arr, root.right, i*2+2, n)
        
    return root

def toArray(root): 
    if root is None: 
        return
      
    queue = [] 
    returnL = []
    queue.append(root) 
  
    while(len(queue) > 0): 
        returnL.append(queue[0].data)
        node = queue.pop(0) 
  
        if node.left is not None: 
            queue.append(node.left) 
   
        if node.right is not None: 
            queue.append(node.right)
            
    return returnL

def isBST(root):

    def is_bst(node, minN, maxX):
        if float(node.data) <= float(minN):
            return False

        if float(node.data) >= float(maxX):
            return False

        left_ok = True
        right_ok = True

        if node.left is not None:
            left_ok = is_bst(node.left, minN, node.data)
        if node.right is not None:
            right_ok = is_bst(node.right, node.data, maxX)

        return left_ok and right_ok

    if root is None:
        return True

    return is_bst(root, float('-inf'), float('inf'))


def preOrder(root):
    if root:
        print(root.data, end=" ")
    
        preOrder(root.left)
        preOrder(root.right)
        
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        
        print(root.data, end=" ")
        
def numNodesInLookUp(root, value):
    numNodes = 1
    while root != None: 
           
        if value > root.data:  
            numNodes += 1
            root = root.right 
  
        elif value < root.data: 
            numNodes += 1
            root = root.left  
        else: 
            return True # if the key is found return 1  
    return numNodes 
    
    
numOfElements = int(input())
givenNumbers = input()
givenList = givenNumbers.split()

numCommands = input()
commands = []
for i in range(0, int(numCommands)):
    c = input()
    commands.append(c)
    
root = None
root = fromArray(givenList, root, 0, len(givenList))
whichSearch = None
l = []
numNodes = 1

for command in commands:
    
    if command == 'isBST':
        if(isBST(root) == False):
            print('false')
            whichSearch = 'nonBST'
        else:
            print('true')

    if command == 'preOrder':
        preOrder(root)
        print()

    if command == 'postOrder':
        postOrder(root)
        print()

    if command == 'toArray':
        l = toArray(root)
        for num in l:
            print(num, end=" ")
        print()

    if 'numNodesInLookup' in command:
        if whichSearch == 'nonBST':
            for i in l:
                if int(i) != int(command[-1]):
                    numNodes += 1
                else:
                    break
                    
            print(numNodes)
        else:
            print(numNodesInLookUp(root, command[-1]))
            









        
                    
