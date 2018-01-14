# only functions for generating tools for individual elements
# print("Hello From __tooles_single:      ", __name__)

from random import shuffle, randint
import pickle

class bcolors:
	WARNING = '\033[91m'
	BOLD = '\033[1m'
	ORANGE = '\x1b[1;33;40m'
	ENDC = '\033[0m'

def __cre_rotor(size_in_max, mix):
	dic = {}
	for i in range(0, size_in_max):
		dic[i] = i #todo tutaj bylo ";" ale po co ?!?!?
	if mix:
		shuffle(dic)
	return dic


def __save_rotor(obj, name):
	with open(name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def __load_rotor(name):
	with open(name + '.pkl', 'rb') as f:
		return pickle.load(f)


def __check_rand_rotor(rotor): #, debug):
	list_k = []
	list_v = []
	test = True #todo usuń i samo return zrób
	for key, values in rotor.items():
		list_k.append(key)
		list_v.append(values)
	test_i = 0
	for i in range(0, len(rotor)):
		if list_v == list_k:
			test_i += 1
	if test_i == len(rotor):
		test = False
	list_k.sort()
	list_v.sort()
	for i in range(0, len(rotor)):
		if list_v != list_k:
			test = False
			break
	return test
	
# generate inter kay from 64 bit number
def generate_from_64b_inter_key(key, rotors, show=False): # todo dlaczego nie mogę tego importować jako __ ???? !!!!
	dic_64b_1 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10,
	             "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16, "h": 17, "i": 18, "j": 19, "k": 20,
	             "l": 21, "m": 22, "n": 23, "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
	             "v": 31, "w": 32, "x": 33, "y": 34, "z": 35, "A": 36, "B": 37, "C": 38, "D": 39, "E": 40,
	             "F": 41, "G": 42, "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49, "O": 50,
	             "P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56, "V": 57, "W": 58, "X": 59, "Y": 60,
	             "Z": 61, "+": 62, "/": 63}

	# 64b transformed to DEC
	num_in_DEC_from_64b = 0
	exponent = 0
	num_in_64b = key[:]
	for i in num_in_64b:
		num_in_DEC_from_64b += (dic_64b_1[i] * (64 ** exponent))
		exponent += 1
	if show:
		print("Random number in DEC from 64b: ")
		for i in range(0, len(str(num_in_DEC_from_64b)) + 60, 60):
			if str(num_in_DEC_from_64b)[i: 60 + i]:
				print(str(num_in_DEC_from_64b)[i: 60 + i])
			else:
				# print("")
				break
	# print(str(num_in_DEC_from_64b)[i: 60 + i])
	# rand_num_in_DEC_from_64b_save = num_in_DEC_from_64b

	# Generate internal key from DEC
	i = 0
	inter_key = [0, ]
	while num_in_DEC_from_64b:
		inter_key[i] = num_in_DEC_from_64b % (len(rotors[0]))
		num_in_DEC_from_64b //= (len(rotors[0]))
		i += 1
		if num_in_DEC_from_64b < (len(rotors[0])):
			inter_key += [num_in_DEC_from_64b, ]
			break
		inter_key += [0]
	# inter_key = inter_key[::-1]   # the number in the correct order, without this number, is invert
	if len(inter_key) % len(rotors) != 0:
		add_zeros = abs((len(inter_key) % len(rotors)) - len(rotors))
		for _ in range(0, add_zeros):
			inter_key.insert(0, 0)

	if show:
		print("\nInternal key: ")
		for i in range(0, len(str(inter_key)) + 60, 60):
			if str(inter_key)[i: 60 + i]:
				print(str(inter_key)[i: 60 + i])
			else:
				# print("")
				break
		print(str(inter_key)[i: 60 + i])
		if (len(inter_key) % len(rotors) != 0):
			print("\nFail")
			return False
		else:
			print("\nPass")
	return inter_key


def __test():
	print("test z __tools")