#using temp variable...

# def bubble_sort(lst):
#     for i in range(len(lst)-1,0,-1):
#         for j in range(i):
#             if lst[j] > lst[j+1]:
#                 temp = lst[j]
#                 lst[j] = lst[j+1]
#                 lst[j+1] = temp

# lst=[5,3,8,6,7,2]
# bubble_sort(lst)
# print(lst)




#without using third variable....


def bubble_sort(lst):
    for ind1 in range(len(lst)-1,0,-1):
        for ind2 in range(ind1):
            if lst[ind2] > lst[ind2+1]:
                lst[ind2],lst[ind2+1] = lst[ind2+1],lst[ind2]
lst=[5,3,8,6,7,2]
bubble_sort(lst)
print(lst)