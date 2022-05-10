#read file
file = open('world.txt')

my_list_1 = []
for line in file:
        # strip off the \n and \r spaces & carriage returns.
        line = line.strip()
        #print to view current contents
        #print(line)
        my_list_1.append(line)
file.close()

# Linear search
i = 0
key = 'English'
while i < len(my_list_1) and my_list_1[i] != key:
        i += 1

if i == len(my_list_1):
        print('The name was not in the list')
else:
        print('The name is at position ', i)

#insertion sort
def insertion_sort(my_list_1):
    """ Sort a list using the insertion sort """
 
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list_1)):
 
        # Get the value of the element to insert
        key_value = my_list_1[key_pos]
 
        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1
 
        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list_1[scan_pos] > key_value):
            my_list_1[scan_pos + 1] = my_list_1[scan_pos]
            scan_pos = scan_pos - 1
 
        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list_1[scan_pos + 1] = key_value
    return my_list_1
#print new list
i = 0
for i in range(0, len(insertion_sort(my_list_1))):
        print (my_list_1[i])
