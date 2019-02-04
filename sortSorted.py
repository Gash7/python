li=[1,2,7,6,5,1,2,3,4,5]
li_sorted=sorted(li)
print('Sorted in built funtion-',li_sorted,li == li_sorted,li is li_sorted)
print('Sorted in built method -',li)

#Sorted in built funtion [1, 1, 2, 2, 3, 4, 5, 5, 6, 7]
#Sorted in built method  [1, 2, 7, 6, 5, 1, 2, 3, 4, 5]

li_sort=li.sort()
print('Sorted in built funtion-',li_sort,li == li_sorted,li is li_sorted)
print('Sorted in built method- ',li)

#Sorted in built funtion None
#Sorted in built method  [1, 1, 2, 2, 3, 4, 5, 5, 6, 7]