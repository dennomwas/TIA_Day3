def find_missing (a,b):
    list1 = a
    list2 = b
    
    if list1 and list2 == 0:
        msg = 0
    elif list2 == list1:
        msg =  0
    elif list1 != list2:
        mylist = set(list2)-set(list1)
        msg = mylist.pop()

    return msg


print(find_missing([1,2,3],[1,2,3,5]))