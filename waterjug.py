# class WaterJug:
#     def __init__(self, jug1_capacity, jug2_capacity, target):
#         self.jug1_capacity = jug1_capacity
#         self.jug2_capacity = jug2_capacity
#         self.target = target

#     def solve(self):
#         jug1 = 0
#         jug2 = 0

#         while True:
#             # Fill jug1 to its maximum capacity
#             jug1 = self.jug1_capacity

#             # Check if jug1 contains the target amount of water
#             if jug1 == self.target:
#                 return True

#             # Transfer water from jug1 to jug2 until jug2 is full or jug1 is empty
#             while jug2 < self.jug2_capacity and jug1 > 0:
#                 jug2 += 1
#                 jug1 -= 1

#                 # Check if jug2 contains the target amount of water
#                 if jug2 == self.target:
#                     return True

#             # Empty jug2 if it is full
#             if jug2 == self.jug2_capacity:
#                 jug2 = 0

#             # Check if jug2 contains the target amount of water
#             if jug2 == self.target:
#                 return True

#             # Check if jug1 is empty
#             if jug1 == 0:
#                 return False

# water_jug = WaterJug(4, 3, 2)
# result = water_jug.solve()
# print(result)


# Works, but isnt what i have to study

from collections import defaultdict

jug1, jug2, aim = 4, 3, 2
visited = defaultdict(lambda: False)
def waterjugSolver(amt1, amt2):
    if(amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
    
    if visited[(amt1,amt2)] == False:
        print(amt1, amt2)
        visited[(amt1,amt2)] = True

        return(waterjugSolver(0,amt2) or waterjugSolver(amt1,0) or waterjugSolver(jug1,amt2) or waterjugSolver(amt1,jug2) or waterjugSolver(amt1 - min(amt1, (jug2-amt2)), amt2 + min(amt1, (jug2-amt2))) or waterjugSolver(amt1 + min(amt2, (jug1-amt1)), amt2 - min(amt2, (jug1-amt1))))
    else:
        return False
    
print("steps: ")
waterjugSolver(0,0)
