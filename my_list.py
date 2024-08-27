my_list = [10, 20, 30]
my_list = [10,15,20,30]
my_list = [10,15,20,30,40,50,60,70]

print(my_list[3])



# Step 1: Create an empty list called my_list
my_list = []

# Step 2: Append the elements 10, 20, 30, and 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # List indices start from 0

# Step 4: Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element from my_list
my_list.pop()  # Removes the last element

# Step 6: Sort my_list in ascending order
my_list.sort()

# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
