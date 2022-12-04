path = "inputs/puzzle1input.txt"
with open(path, 'r') as file:
    calories_ws = file.readlines()

def read_calories(calo):
    calories = []
    for i in range(0, len(calo)):
        calories.append(calo[i].rstrip())
    return calories

def find_max_calories(kal_list):
    max_calories, current_calories = 0, 0

    for i in range(0, len(kal_list)):
        if kal_list[i] != "":
            current_calories += int(kal_list[i])

        else:
            if current_calories > max_calories: 
                max_calories = current_calories
            current_calories = 0
    return max_calories

def create_calorie_leaderboard(kal_list):
    current_calories = 0
    calorie_leaderboard = []

    for i in range(0, len(kal_list)):
        if kal_list[i] != "":
            current_calories += int(kal_list[i])
        else:
            calorie_leaderboard.append(current_calories)
            calorie_leaderboard.sort()
            if len(calorie_leaderboard) > 3:
                calorie_leaderboard.pop(0)
            current_calories = 0
    return calorie_leaderboard

z = read_calories(calories_ws)
x = find_max_calories(z)
y = create_calorie_leaderboard(z)
print(sum(y))
