# LRU Cached American Put Option Calculator by Michael Rizzo
import functools
import time
import math
import os
import sys

class Node:
    def __init__(self, v):
        self.right = None
        self.left = None
        self.val = v
    
@functools.lru_cache(maxsize=None)
def makeTree(sk, currLevel):
    node = Node(sk)

    if currLevel == n:
        return node
    else:
        currLevel += 1

    node.right = makeTree(sk * u, currLevel)
    node.left = makeTree(sk * d, currLevel)
    return node

def printTree(root, inorder):
    if root != None:
        inorder.append(root.val)
        printTree(root.left, inorder)
        printTree(root.right, inorder) 
        
@functools.lru_cache(maxsize=None)
def payoffAmericanPut(K):
    payoff = 0.0
    if s0>K:
         payoff = s0-K
    return round(payoff,4)

@functools.lru_cache(maxsize=None)
def priceTree(root):    
    if root.left == None and root.right == None:
        return max(K - root.val, 0)
    left = priceTree(root.left)
    right = priceTree(root.right)
#     print("UP- " ,right , " Down- ", left, "Value- ", root.val)
    return round(max(ert*(p*right+(1-p)*left), K-root.val),4)

path = sys.argv[1]
preorder = []
sys.setrecursionlimit(10000)
# start = time.process_time()   
if(os.path.exists(path)):
    with open(path) as f:
        for line in f.readlines():
            r,T,n,sigma,s0,K = line.split("\t")
            
            s0 = float(s0)
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
            
#             print("R:" ,r, " T:", T, " n:", n, " sigma:", sigma, " s0:", s0, " K:", K)
#             print (n)
#             print("U:", u, " D:", d, " P:", p)
        
#             start = time.process_time()   
            root = makeTree(int(s0), 0.0)
            print (priceTree(root))
    
            # print ("TIME TAKEN: ", (time.process_time() - start ), "ms")