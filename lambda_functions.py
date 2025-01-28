modulus = lambda num1, num2 : num1 % num2  #lambda function that returns remainder

list1 = [10, 20, 30, 40, 50]

add_5 = map(lambda num: num + 5, list1) #map function adds 5 to each number on list

list2 = [5, 15, 25, 35, 45]

within_range = filter(lambda a : (a >= 10 and a<= 30), list2) #filter only returns values that matches prerequisites

print (list(add_5))  #Output: [15, 25, 35, 45, 55]

print (list(within_range)) #Output: [15, 25]