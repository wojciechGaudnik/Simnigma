# only functions to generate tools for ten drums encrypts

from Enigma_all.Enigma_4.modules.__tools_single \
	import (__cre_drum, __save_drum, __load_drum, __check_rand_drum)


def create_drums(size, mix, number):
	return ([__cre_drum(size, mix) for _ in range(0, number)])
	
	
def create_and_save_drums(obj_s, name, number):
	for i in range(1, number - 1):
		__save_drum(obj_s[i - 1], name + str(i))
		
		
def load_drums(name, number):
	return ([__load_drum(x) for x in (name + str(x) for x in range(1, number - 1))])
	
	
def check_rand_drums(drums):
	__key_min = min(drums[0])
	__key_max = max(drums[0])
	__value_min = min(drums[0].values())
	__value_max = max(drums[0].values())
	__len = len(drums[0])
	__random = __check_rand_drum(drums[0])
	
	for drum in drums:
		if __key_min != min(drum) or __key_max != max(drum) or __len != len(drum) or __random != __check_rand_drum(drum)\
				or __value_min != min(drum.values()) or __value_max != max(drum.values()):
			return False, __random
	return True, __random


def check_text_const(text_before):
	for i in range(1, len(text_before)):
		if text_before[0] != text_before[i]:
			return False
	return True
