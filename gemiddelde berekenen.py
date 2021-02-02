lst = [4,5,6,7,85,4,1,5,1,7,8,8,7,5,13]
lst_van_lst = [[2,6],[7,2],[6,2,6]]

def gem_van_lijst(lst):
    return sum(lst) / len(lst)

def lijst_van_gem(lst_van_lst):
    lst_gem = []
    for i in lst_van_lst:
        lst_gem.append(gem_van_lijst(i))
    return lst_gem

print(gem_van_lijst(lst))
print(lijst_van_gem(lst_van_lst))