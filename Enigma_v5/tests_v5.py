from Enigma_all.Enigma_v5.modules.tests_def import test_3d_2b




key_enc = [1, 2, 2, 0, 1, 2, 3, 3, 3]
key_test =[1, 0, 0, 0, True]

key_test[1:4] = key_enc[-6: -3]
# print(key_test)



test_3d_2b()



# from Enigma_all.Enigma_v5.modules.tools import load_drums
#
# drum1, drum2, drum3 = load_drums("./drums/set_drum_2b_", 3)
#
#
# __len_key = len(key_enc)
# __max_i = len(drum1)
#
#
#
# enc = [9 ,0, 0, 0, True]
# __len_key_block = 3
#
# for __cycles_finished in range (0, 3):
# 	enc[1:__len_key_block + 1] = key_enc[__len_key_block * __cycles_finished: (__len_key_block * __cycles_finished) + __len_key_block]
# 	print(enc)

# for x in range(0, 100):
# 	key_enc[0] += 1
# 	i = 0
# 	for i in range(0, __len_key):
# 		if key_enc[i] == __max_i:
# 			key_enc[i] = 0
# 			key_enc[i + 1] += 1
# 			if key_enc[-1] == __max_i:
# 				key_enc[-1] = 0
# 		else:
# 			break
# 	print(key_enc)

