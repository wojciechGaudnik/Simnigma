from moduly import *

# a = [513]
# print(chr(a[0]))
#
#
# lista = [1, 2, 3, 4, 5]
# print(lista)
# lista.pop(-1)
# print(lista)

# //todo Ładuje dict z pliku
be1 = load("dict1")  #/todo jest od 0 do 512 włącznie !!!
be2 = load("dict2")
be3 = load("dict3")




#/todo szyftowanie
i1 = 0
i2 = 0
i3 = 0

lit1 = 97
lit2 = 97
lit3 = 97
lit4 = 97

lit1 += i1
sz_lit1 = hasz(be1, lit1)
sz_lit1 += i2
sz_lit1 = hasz(be2, sz_lit1)
sz_lit1 += i3
sz_lit1 = hasz(be3, sz_lit1)
i1 = 1
i2 = 0
i3 = 0
print(sz_lit1)

lit2 += i1
sz_lit2 = hasz(be1, lit2)
sz_lit2 += i2
sz_lit2 = hasz(be2, sz_lit2)
sz_lit2 += i3
sz_lit2 = hasz(be3, sz_lit2)
i1 = 2
i2 = 0
i3 = 0
print(sz_lit2)

lit3 += i1
sz_lit3 = hasz(be1, lit3)
sz_lit3 += i2
sz_lit3 = hasz(be2, sz_lit3)
sz_lit3 += i3
sz_lit3 = hasz(be3, sz_lit3)
i1 = 3
i2 = 0
i3 = 0
print(sz_lit3)

lit4 += i1
sz_lit4 = hasz(be1, lit4)
sz_lit4 += i2
sz_lit4 = hasz(be2, sz_lit4)
sz_lit4 += i3
sz_lit4 = hasz(be3, sz_lit4)
i1 = 4
i2 = 0
i3 = 0
print(sz_lit4)

#/todo deszyfrowanie
print("---------")
i1 = 4 - 1
i2 = 0
i3 = 0

lit1 = 330
lit2 = 305
lit3 = 103
lit4 = 215

deszy_lit4 = de_hasz(be3, lit4)
deszy_lit4 -= i3
deszy_lit4 = de_hasz(be2, deszy_lit4)
deszy_lit4 -= i2
deszy_lit4 = de_hasz(be1, deszy_lit4)
deszy_lit4 -= i1
print(deszy_lit4)
i1 = 3 - 1
i2 = 0
i3 = 0

deszy_lit3 = de_hasz(be3, lit3)
deszy_lit3 -= i3
deszy_lit3 = de_hasz(be2, deszy_lit3)
deszy_lit3 -= i2
deszy_lit3 = de_hasz(be1, deszy_lit3)
deszy_lit3 -= i1
print(deszy_lit3)
i1 = 2 - 1
i2 = 0
i3 = 0

deszy_lit2 = de_hasz(be3, lit2)
deszy_lit2 -= i3
deszy_lit2 = de_hasz(be2, deszy_lit2)
deszy_lit2 -= i2
deszy_lit2 = de_hasz(be1, deszy_lit2)
deszy_lit2 -= i1
print(deszy_lit2)
i1 = 1 - 1
i2 = 0
i3 = 0

deszy_lit1 = de_hasz(be3, lit1)
deszy_lit1 -= i3
deszy_lit1 = de_hasz(be2, deszy_lit1)
deszy_lit1 -= i2
deszy_lit1 = de_hasz(be1, deszy_lit1)
deszy_lit1 -= i1
print(deszy_lit1)
i1 = 0 - 1
i2 = 0
i3 = 0