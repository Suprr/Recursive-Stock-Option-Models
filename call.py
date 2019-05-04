# LRU Cached Asian Call Option Calculator by Michael Rizzo
import functools
import time
import math
import os
import sys

# Import python optimizer which may vary computation times [left for reference]
from numba import autojit 

class Node:
    def __init__(self, v):
        self.right = None
        self.left = None
        self.val = v
    
# @autojit
@functools.lru_cache(maxsize=None)
def makeTree(currLevel,runningSum, sp):
    if (currLevel == 0):
        node = Node (sp)
    else: 
# compute the running average per timestep
        node = Node(runningSum/(currLevel+1))

    if currLevel == n:
        return node
    else:
        currLevel += 1
        
    a = sp * u
    b = sp * d

    node.right = makeTree(currLevel, runningSum + a, a)
    node.left = makeTree(currLevel, runningSum + b, b)
    return node

def printTree(root, inorder):
    if root != None:
        inorder.append(root.val)
        printTree(root.left, inorder)
        printTree(root.right, inorder) 

# @autojit
@functools.lru_cache(maxsize=None)
def priceTree(root):    

    if root.left == None and root.right == None:
        return max(root.val - K, 0)

    left = priceTree(root.left)
    right = priceTree(root.right)
#     print("UP- " ,right , " Down- ", left, "Value- ", root.val)
    return round(max(ert*(p*right+(1-p)*left), root.val - K),4)

path = sys.argv[1]
preorder = []
sys.setrecursionlimit(2000)
if(os.path.exists(path)):
    with open(path) as f:
        for line in f.readlines():
            r,T,n,sigma,s0,K = line.split("\t")
            
            sk = float(s0)
            sigma = float(sigma)
            r = float(r)
            T = float(T)
            n = int(n)
            K = float(K)
            
            deltaT = T/n
            u = math.exp(sigma*math.sqrt(deltaT))
            d = 1/u
            p = (math.exp((r*deltaT)) - d) / (u - d)
            ert = math.exp(-1*(r*deltaT))
            
#             print("R:" ,r, " T:", T, " n:", n, " sigma:", sigma, " s0:", sk, " K:", K)
#             print (n)
#             print("U:", u, " D:", d, " P:", p)

#             start = time.process_time()   
            root = makeTree(0.0, sk,sk)
            print (priceTree(root))
#             print ("TIME TAKEN: ", (time.process_time() - start ), "ms")