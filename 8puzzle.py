# class Puzzle:
#     def __init__(self, initial_state):
#         self.initial_state = initial_state
#         self.goal_state = [[1, 2, 3], [7, 8, 6], [4, 5, 0]]

#     def solve(self):
#         open_list = [(self.initial_state, 0)]
#         closed_list = set()

#         while open_list:
#             current_state, current_cost = open_list.pop(0)
#             closed_list.add(tuple(map(tuple, current_state)))
#             print(current_state, "current cost: ", current_cost)

#             if current_state == self.goal_state:
                
#                 return current_cost

#             zero_row, zero_col = self.find_zero(current_state)

#             for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 new_row = zero_row + move[0]
#                 new_col = zero_col + move[1]

#                 if 0 <= new_row < 3 and 0 <= new_col < 3:
#                     new_state = [list(row) for row in current_state]
#                     new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]

#                     if tuple(map(tuple, new_state)) not in closed_list:
#                         open_list.append((new_state, current_cost + 1))

#         return -1

#     def find_zero(self, state):
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] == 0:
#                     return i, j

# # Example usage
# initial_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
# puzzle = Puzzle(initial_state)
# steps = puzzle.solve()
# print(f"Number of steps required: {steps}")


import copy
from heapq import heappop, heappush

n = 3
row = [1, 0, -1, 0]
col = [0, -1, 0, 1]

class PriorityQueue:
    def __init__(self):
        self.heap = []
    def push(self, k):
        heappush(self.heap, k)
    
    def pop(self):
        return heappop(self.heap)
    
    def empty(self):
        if not self.heap:
            return True
        else:
            return False

class node:
    def __init__(self,parent,mat,empty_tile_pos,cost,level):
        self.parent = parent
        self.mat = mat
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.level = level

    def __lt__(self, nxt):
        return self.cost < nxt.cost
    
def calculateCost(mat,final)->int:
    count = 0
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if((mat[i][j])and(mat[i][j] != final[i][j])):
                count += 1
    return count

def newNode(mat,empty_tile_pos,new_empty_tile_pos,level,parent,final)->node:
    new_mat = copy.deepcopy(mat)
    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]
    x2 = new_empty_tile_pos[0]
    y2 = new_empty_tile_pos[1]
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
    cost = calculateCost(new_mat, final)
    new_node = node(parent,new_mat,new_empty_tile_pos,cost,level)
    return new_node

def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print("%d"%mat[i][j], end = " ")
        print()

def isSafe(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def printPath(root):
    if root == None:
        return
    printPath(root.parent)
    print()
    printMatrix(root.mat)
    print()

def solve(initial,empty_tile_pos,final):
    pq = PriorityQueue()
    cost = calculateCost(initial, final)
    root = node(None, initial, empty_tile_pos, cost, 0)
    pq.push(root)
    while not pq.empty():
        minimum = pq.pop()
        if minimum.cost == 0:
            printPath(minimum)
            return
        
        for i in range(4):
            new_tile_pos = [minimum.empty_tile_pos[0] + row[i], minimum.empty_tile_pos[1] + col[i]]
            if isSafe(new_tile_pos[0], new_tile_pos[1]):
                child = newNode(minimum.mat, minimum.empty_tile_pos, new_tile_pos, minimum.level + 1, minimum, final)
                pq.push(child)

    
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1 ,2 ,3], [5, 8, 6], [0, 7, 4]]
empty_tile_pos = [1, 2]

solve(initial, empty_tile_pos, final)