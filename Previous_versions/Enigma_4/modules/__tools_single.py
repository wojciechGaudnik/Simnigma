# only functions for generating tools for individual elements

from random import shuffle, randint
import pickle

class bcolors:
	WARNING = '\033[91m'
	BOLD = '\033[1m'
	ENDC = '\033[0m'

def __cre_drum(size_in_max, mix):
	dic = {}
	for i in range(0, size_in_max):
		dic[i] = i;
	if mix:
		shuffle(dic)
	return dic


def __save_drum(obj, name):
	with open(name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def __load_drum(name):
	with open(name + '.pkl', 'rb') as f:
		return pickle.load(f)


def __check_rand_drum(drum): #, debug):
	list_k = []
	list_v = []
	test = True #todo usuń i samo return zrób
	for key, values in drum.items():
		list_k.append(key)
		list_v.append(values)
	test_i = 0
	for i in range(0, len(drum)):
		if list_v == list_k:
			test_i += 1
	if test_i == len(drum):
		test = False
	list_k.sort()
	list_v.sort()
	for i in range(0, len(drum)):
		if list_v != list_k:
			test = False
			break
	return test
	

# todo I know what you mean :) but it's only to see if it's possible.
# todo In any case, how to find "statement with out any effect"
def gen_text(char_max, ran, size_double, drum_for_gen, *char_size):
	x = []
	if len(char_size) == 1:
		char = char_size[0]
		size = 1
	else:
		if len(char_size) == 2:
			char = char_size[0]
			size = char_size[1]
		else:
			char = 0
			size = 1
			
	drum_for_gen = dict(drum_for_gen)
	[[[x.append(randint(0, len(drum_for_gen) - 1) if ran else char) for _ in range(2 * len(drum_for_gen))]
	  if not char_max else [x.append(len(drum_for_gen) - 1) for _ in range(2 * len(drum_for_gen))]]
	 if size_double else [[x.append(randint(0, len(drum_for_gen) - 1) if ran else char) for _ in range(size)]
	                      if not char_max else [x.append(len(drum_for_gen) - 1) for _ in range(size)]]]
	return x

	