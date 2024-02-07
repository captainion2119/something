# class Monkey:
#     def __init__(self, name):
#         self.name = name
#     def climb(self, box):
#         print(self.name + " is climbing the box " + str(box))
#     def reach_bananas(self):
#         print(self.name + " has reached the bananas")

# def monkey_and_banana():
#     monkey_name = input("Enter the name of the monkey: ")
#     monkey = Monkey(monkey_name)
#     try:
#         num_boxes = int(input("Enter the number of boxes: "))
#     except ValueError:
#         print("Invalid input")
#         return
#     boxes = list(range(1, num_boxes + 1))
#     for box in boxes:
#         monkey.climb(box)
#     monkey.reach_bananas()

# if __name__ == "__main__":
#     monkey_and_banana()

name = "jaggu"
num_boxes = 5

for i in range(1,num_boxes):
    print(f"{name} is climbing the box", i)

print(f"{name} has reached the bananas")
