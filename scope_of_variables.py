numbers = [5, 9, 12] #global list

def process_numbers():
    total = 0 #initialized to 0
    def add_to_total():
        nonlocal total  #nonlocal keyword used
        global numbers  #global keyword used
        total += numbers[-1] #adds the last number in list to total
        numbers.append(total) #appends new value of total to the end of the list
        print("Total is: ", total, "\nNumbers are: ", numbers)

    add_to_total() #calling function
    add_to_total()
    add_to_total()
    add_to_total()

process_numbers()

print("Final total", numbers)

#Output
'''
Total is:  12
Numbers are:  [5, 9, 12, 12]
Total is:  24
Numbers are:  [5, 9, 12, 12, 24]
Total is:  48
Numbers are:  [5, 9, 12, 12, 24, 48]
Total is:  96
Numbers are:  [5, 9, 12, 12, 24, 48, 96]
Final total [5, 9, 12, 12, 24, 48, 96]
'''