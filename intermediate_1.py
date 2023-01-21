def unique_list(nums):
    list1 =[]

    for x in nums:
        if x not in list1:
            list1.append(x)
    return list1


mylist = [1, 2, 3, 2, 1, 4]


list3 = unique_list(mylist)
print(list3)