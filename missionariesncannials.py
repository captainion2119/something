# from collections import deque

# def is_valid_state(state):
#     missionaries, cannibals, boat = state
#     if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
#         return False
#     if missionaries < cannibals and missionaries > 0:
#         return False
#     if missionaries > cannibals and missionaries < 3:
#         return False
#     return True

# def is_goal_state(state):
#     return state == (0, 0, 0)

# def get_next_states(state):
#     states = []
#     missionaries, cannibals, boat = state

#     if boat == 1:
#         for i in range(3):
#             for j in range(3):
#                 if i + j <= 2 and i + j > 0:
#                     new_state = (missionaries - i, cannibals - j, 0)
#                     if is_valid_state(new_state):
#                         states.append(new_state)
#     else:
#         for i in range(3):
#             for j in range(3):
#                 if i + j <= 2 and i + j > 0:
#                     new_state = (missionaries + i, cannibals + j, 1)
#                     if is_valid_state(new_state):
#                         states.append(new_state)

#     return states

# def bfs():
#     start_state = (3, 3, 1)
#     visited = set()
#     queue = deque([(start_state, [])])

#     while queue:
#         state, path = queue.popleft()
#         if is_goal_state(state):
#             return path
#         if state in visited:
#             continue
#         visited.add(state)
#         for next_state in get_next_states(state):
#             queue.append((next_state, path + [next_state]))

#     return None

# path = bfs()
# if path:
#     print("Solution found!")
#     for state in path:
#         print(state)
# else:
    #  print("No solution found.")
#  Not the code i want.
Lm,Lc,Rm,Rc = 3,3,0,0  
k = 0
try:
    while True:
        while True:
            print("Left to right")
            m = int(input("Enter the number of missionaries: "))
            c = int(input("Enter the number of cannibals: "))
            if m+c > 2 and Lm-m >= 0 and Lc-c >= 0:
                print("Invalid input")
            elif (m == 0 and c == 0):
                print("Empty travel not possible")
            else: 
                break
        Lm -= m
        Lc -= c
        Rm += m
        Rc += c
        k += 1
        print("Left: ",Lm,Lc)
        for i in range(Lm):
            print("M",end = " ")
        for i in range(Lc):
            print("C",end = " ")
        print("| --> |",end =" ")
        print("\nRight: ",Rm,Rc)
        for i in range(Rm):
            print("M",end = " ")
        for i in range(Rc):
            print("C",end = " ")
        print("\n")
        if (Lm < Lc and Lm > 0) or (Rm < Rc and Rm > 0):
            print("Game over")
            break
        if Rm == 3 and Rc == 3:
            print("Congratulations")
            break
        while True:
            print("Right to left")
            m = int(input("Enter the number of missionaries: "))
            c = int(input("Enter the number of cannibals: "))
            if m+c > 2 and Lm-m >= 0 and Lc-c >= 0:
                print("Invalid input")
            elif (m == 0 and c == 0):
                print("Empty travel not possible")
            else: 
                break
        Lm += m
        Lc += c
        Rm -= m
        Rc -= c
        print("Left: ",Lm,Lc)
        for i in range(0,Lm):
            print("M",end = " ")
        for i in range(0,Lc):
            print("C",end = " ")
        print("| <-- |",end =" ")
        print("\nRight: ",Rm,Rc)
        for i in range(0,Rm):
            print("M",end = " ")
        for i in range(0,Rc):
            print("C",end = " ")
        print("\n")
        k += 1
        if (Lm < Lc and Lm > 0) or (Rm < Rc and Rm > 0):
            print("Game over")
            break
except ValueError:
    print("Try again")

