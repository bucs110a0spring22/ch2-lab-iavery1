import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class)
print("\n")

#Part B

#declare empty list
my_list = [0,0,0,0,0]

#loop over list
for x in range(len(my_list)):
  my_list[x] = random.randrange(1,100)

random_choice = random.choice(my_list)

print("Random choice: ", random_choice)
