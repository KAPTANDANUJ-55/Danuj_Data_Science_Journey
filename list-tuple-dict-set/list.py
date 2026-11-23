# Creating a list
nums = [10, 20, 30, 40]
mixed = [1, "Danuj", 3.14, True]  # Different data types are also allowed

# Indexing (starts at 0)
print(nums[0])   # 10
print(nums[-1])  # 40 -> negative index counts from the end

# Slicing: [start : stop : step], stop is exclusive
print(nums[1:3])   # [20, 30]
print(nums[::-1])  # [40, 30, 20, 10] -> popular trick to reverse a list
print(nums[1:3:2])
# Modifying the list (lists are mutable)
nums[0] = 99
nums.append(50)     # Add to the end -> O(1)
nums.insert(1, 15)  # Add in the middle -> O(n), because elements need to shift
nums.remove(30)     # Removes the first matching value -> O(n)
last = nums.pop()   # Removes and returns the last element -> O(1)
print(nums)
