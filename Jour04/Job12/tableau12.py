def mylen(list):
    total = 0
    for i in list:
        total = total + 1
    return total

list = [46,8,3,10,4]
def ordrecrois(list):
    i = 0
    for i in range(mylen(list)):
        for j in range(i+1,mylen(list)):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
    return list

print(ordrecrois(list))