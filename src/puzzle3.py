from string import ascii_letters

path = "inputs/puzzle3inputs.txt"
with open(path, 'r') as file:
    rucksacks = file.read().split("\n")

def find_priority(inventory):
    half = len(inventory) // 2 
    left, right = inventory[:half], inventory[half:]
    common = None
    for i in range(0, half): 
        if left[i] in right:
            common = left[i]
            return ascii_letters.find(common, 1) + 1
        elif i == half:
            return 0

print(sum(map(find_priority, (rucksacks))))

def find_badge_priority(inventory):
    common = None
    for i in range(0, len(inventory), 3): 
        a, b, c = inventory[i:i+3]
        

print(find_badge_priority(rucksacks))