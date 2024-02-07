def tower_of_hanoi(disks,source,auxiliary,target):
    if disks == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(disks-1,source,target,auxiliary)
    print(f"Move disk {disks} from {source} to {target}")
    tower_of_hanoi(disks-1,auxiliary,source,target)

disks = int(input("Enter the number of disks: "))
tower_of_hanoi(disks,'A','B','C')