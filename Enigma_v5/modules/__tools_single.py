# only functions for generating tools for individual elements

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
	



	