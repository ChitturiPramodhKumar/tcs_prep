def missing_number(li):
    for i in range(len(li)):
        if li[i] ==  i+1:
            continue
        else:
            return i+1


t0 = [1,2, 3, 4, 5, 7, 8]
t1 = [1, 3, 4, 5]
t2 = [1, 2, 3, 4, 6]
print(missing_number(t0))
print(missing_number(t1))
print(missing_number(t2))