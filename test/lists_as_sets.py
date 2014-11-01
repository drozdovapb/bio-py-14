
def delete_duplicates(lst):
    newlist = list()
    for item in lst:
        if item not in newlist:
            newlist.append(item)
    return newlist

def unite_lists(lst1, lst2):
    newlist = lst1
    for item in lst2:
        if item not in newlist:
            newlist.append(item)
    return newlist

def intersect_lists(lst1, lst2):
    newlist = list()
    for item in lst1:
        if item in lst2:
            newlist.append(item)
    return newlist
    
def subtract_lists(lst1, lst2):
    for item in lst2:
            lst1.remove(item)
    return lst1
