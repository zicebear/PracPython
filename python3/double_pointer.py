# 未完成
list1 = [38, 49, 65, 97]
list2 = [13, 27, 76]
list3 = []

while range(len(list1)) :
    for j in range(len(list2)):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1

print(list3)