# from Szyfr_enigma.Enigma_3.modules_3 import (check_rand_dict, save_dict, cre_mix_dict, load_dict, check_rand_dict,
#                        Drum_first_encrypt, Drum_last_decrypt, Drum_next_encrypt,
#                        Drum_next_decrypt)
#
# # for n in range (0, 20):
# # 	bit = 2 ** n
# # 	print(n, " : ", bit)
#
# be1 = cre_mix_dict(8, True)
# print(be1)
#
# be2 = {}
# for key, value in be1.items():
# 	be2[value] = key
#
# print(be2)
test = [1, 2]
i = 2
x = 0
while i:
	x = x + 1
	i = x ** 50
	
	print("Number of combinations: ", format(i, '.3E'), "   ", i)
	