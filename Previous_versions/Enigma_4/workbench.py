
drum3 = {0 : 3,
         1 : 0,
         2 : 1,
         3 : 2}

key = [3, 1, 2, 2]#, 2, 2, 2]  #długość klucza określa ile bębnów !!!

text_before = [0, 1, 2, 3, 0]# , 1, 2, 3]

key_plus = key[:]
key_plus.append(True)
cycles = 30000


print(key_plus)
for i in range(0, cycles):
    key_plus[1] += 1
    for ii in range(1, 4):
        if key_plus[ii] == 4:
            key_plus[ii] = 0
            if ii < (len(key_plus) - 2):
                key_plus[ii + 1] += 1
    print(key_plus)


print("--------------")
print(key_plus)
for i in range(0, cycles):
    key_plus[1] -= 1
    for ii in range(1, 4):
        if key_plus[ii] < 0:
            key_plus[ii] = 3
            if ii < (len(key_plus) - 2):
                key_plus[ii + 1] -= 1
    print(key_plus)
    
    

