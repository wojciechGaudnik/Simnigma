# only functions to generate tools for ten drums encrypts
from random import randint

from Enigma_all.Enigma_v5.modules.__tools_single \
	import (__cre_drum, __save_drum, __load_drum, __check_rand_drum)
from Enigma_all.Enigma_v5.modules.core import EncryptNextDrum, EncryptSet, DecryptNextDrum, DecryptSet


def create_drums(size, mix, number_of_drums):
	return ([__cre_drum(size, mix) for _ in range(0, number_of_drums)])
	
	
def save_drums(drums, name):
	i = 1
	for drum in drums:
		__save_drum(drum, name + str(i))
		i += 1
		
		
def load_drums(name, number):
	return ([__load_drum(x) for x in (name + str(x) for x in range(1, number + 1))])
	
	
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


# todo I know what you mean :) but it's only to see if it's possible.
# todo In any case, how to find "statement with out any effect"
def gen_text(char_max, ran, size_triple, drum_for_gen, *char_size):
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
	[[[x.append(randint(0, len(drum_for_gen) - 1) if ran else char) for _ in range(3 * len(drum_for_gen))]
	  if not char_max else [x.append(len(drum_for_gen) - 1) for _ in range(3 * len(drum_for_gen))]]
	 if size_triple else [[x.append(randint(0, len(drum_for_gen) - 1) if ran else char) for _ in range(size)]
	                      if not char_max else [x.append(len(drum_for_gen) - 1) for _ in range(size)]]]
	return x


def check_text_const(text_before):
	for i in range(1, len(text_before)):
		if text_before[0] != text_before[i]:
			return False
	return True


def encrypt(drums, key_enc, text_before):
	encrypt_drums = [EncryptNextDrum(drum) for drum in drums]
	encrypt_first = EncryptSet(key_enc[:], text_before[:], drums[0])
	
	enc = [True]
	while True:
		enc = encrypt_first.set_enc_chain(enc)
		for encrypt_drum in encrypt_drums:
			enc = encrypt_drum.encrypt(enc)
		if not enc[-1]:
			break
	text_encrypt = encrypt_first.get_encrypt_list()
	return text_encrypt


def decrypt(drums, key_dec, text_encrypt):
	decrypt_drums = [DecryptNextDrum(drum) for drum in drums]
	decrypt_first = DecryptSet(key_dec[:], text_encrypt[:], drums[0])
	
	dec = [True]
	while True:
		dec = decrypt_first.set_dec_chain(dec)
		for decrypt_drum in reversed(decrypt_drums):
			dec = decrypt_drum.decrypt(dec)
		if not dec[-1]:
			break
	text_decrypt = decrypt_first.get_decrypt_list()
	return text_decrypt
