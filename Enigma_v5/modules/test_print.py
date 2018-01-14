from Enigma_all.Enigma_v5.modules.__tools_single import bcolors, generate_from_64b_inter_key
from Enigma_all.Enigma_v5.modules.tools import check_text_const, check_rand_rotors, create_key, check_patterns, \
	check_all_patterns, key_from_64b_to_dec, calc_number_comb, print_long

import decimal
from math import log


def test_print(rotors, key_enc = [], key_dec = [], text_before = [], text_encrypt = [], text_decrypt = [],
               show_all=False, show_first=False, show_short=False, show_calc=False, show_uni=False):
			
	key_enc_before = key_enc[:]
	key_dec_before = key_dec[:]
	if isinstance(key_enc, str):
		key_enc = generate_from_64b_inter_key(key_enc, rotors)
	if isinstance(key_dec, str):
		key_dec = generate_from_64b_inter_key(key_dec, rotors)
		
		
	# Checked length of the pattern
	cal_pattern_length = calc_number_comb(rotors, key_enc)
	
	max_print_length = 110
	min_print_length = 15
	if show_all or show_first:
		# Print rotors
		print_long("Rotor", rotors, min_print_length, max_print_length)
		
		# Print keys
		if key_enc_before and isinstance(key_enc_before, list): print_long("Encrypt key", key_enc, min_print_length, max_print_length, False)
		if key_enc_before and isinstance(key_enc_before, str): print_long("Enc. key in Uni", '[' + key_enc_before + ']', min_print_length, max_print_length, False)
		if key_dec_before and isinstance(key_dec_before, list): print_long("Decrypt key", key_dec, min_print_length, max_print_length, False)
		if key_dec_before and isinstance(key_dec_before, str): print_long("Dec. key in Uni", '[' + key_dec_before + ']', min_print_length, max_print_length, False)
		print_long("Int. enc. key", key_enc, min_print_length, max_print_length, False)
		print_long("Int. dec. key", key_dec, min_print_length, max_print_length, False)
		
		# Print texts before, encrypt and decrypt
		if (show_uni == False): print_long("Text before", text_before, min_print_length, max_print_length, False)
		if (show_uni == True): print_long("Text be. in Uni", [chr(a) for a in text_before ], 15, max_print_length, False)
		if (show_uni == False): print_long("Text encrypt", text_encrypt, min_print_length, max_print_length, False)
		if (show_uni == True): print_long("Text en. in Uni", [chr(a) for a in text_encrypt], 15, max_print_length, False)
		if (show_uni == False): print_long("Text decrypt", text_decrypt, min_print_length, max_print_length, False)
		if (show_uni == True): print_long("Text de. in Uni", [chr(a) for a in text_decrypt], 15, max_print_length, False)
	
	if show_all or show_short:
		# Print short rotors info
		print("Rotors, number of key-val:" + " " * 21, "[" + format(decimal.Decimal(len(rotors[0])), '.2E') + "]")
		print("Rotors size in bit:" + " " * 28, "[" + str(int(log(len(rotors[0]), 2))) + " bit]")
		print("Rotors, number existing:" + " " * 23, "[" + str(len(rotors)) + " rotors]")  # number of exists rotors
		for i in range(len(rotors), 0, -1):
			if len(key_dec) % i == 0:
				print("Rotors, number used:" + " " * 27, "[" + str(i) + " rotors]")
				print("Number of passes:" + " " * 30, "[" + str(len(key_dec) // i) + " passes]")
				break
		if check_rand_rotors(rotors)[0]:
			print("Minimum value in rotor:\t\t\t\t\t\t\t" + "[" + str(min(rotors[0])) + " min]")
			print("Maximum value in rotor:\t\t\t\t\t\t\t" + "[" + str(max(rotors[0])) + " max]")
			print("Equality test of rotors:\t\t\t\t\t\t" + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
			if check_rand_rotors(rotors)[1]:
				print("Randomness and integrity rotor test:\t\t\t" + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
			else:
				print("Randomness and integrity rotor test:\t\t\t" + "[" + bcolors.WARNING + bcolors.BOLD + "FAIL" + bcolors.ENDC + "]")
		else:
			print("Minimum value in rotor:\t\t\t\t\t\t\t" + "[" + str(min(rotors[0])) + " min]")
			print("Maximum value in rotor:\t\t\t\t\t\t\t" + "[" + str(max(rotors[0])) + " max]")
			print("Equality test of rotors:\t\t\t\t\t\t" + "[" + bcolors.BOLD + bcolors.ORANGE + "FAIL" + bcolors.ENDC + "[")
		
		
		# Print short keys info
		print("Key enc. len. in num. el.:" + " " * 21, "[" + format(decimal.Decimal(len(key_enc_before)), '.2E') + "]")
		print("Key int. enc. len. in num. el.:" + " " * 16, "[" + format(decimal.Decimal(len(create_key(key_enc, rotors))), '.2E') + "]")
		if isinstance(key_enc, str): print("Key size in bit of num. in dec.:" + " " * 15, "[" + str(int(log(key_from_64b_to_dec(key_enc), 2))) + " bit]") #((log(l, 2)))
		print("Key the same:" + " " * 34, "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]") if key_enc == key_dec else \
			print("Key the same:" + " " * 34, "[" + bcolors.ORANGE + "FAIL" + bcolors.ENDC + "]")
		
		
		# Print short text info
		print("Text before length:" + " " * 28, "[" + format(decimal.Decimal(len(text_before)), '.2E') + "]")
		print("Text before constant:" + " " * 26, "[{}]".format("Yes" if check_text_const(text_before) else "No"))
	
	# # Calculated variations with repetitions
	# cal_name_length = "Calculated variations with repetitions:\t\t\t"
	# print(cal_name_length + "[" + format(decimal.Decimal(cal_pattern_length), '.2E') + "]")
	
	
	if show_all or show_calc:
		if check_text_const(text_before):
			# check_name_length = "Checked length of the pattern:\t\t\t\t\t"
			if len(text_encrypt) > cal_pattern_length * 3:
				patterns_over = check_patterns(text_encrypt, cal_pattern_length // 2, 1, True)
				# print("Patterns over, only first:" + " " * 21, [x for x in patterns_over[0: 1]])
				check_all_patterns(text_encrypt, 4, patterns_over[0][0] -1 , 3, 2, patterns_over, True)
				
				# def check_all_patterns(text_encrypt, min_pattern, max_pattern, max_num_patterns=1, del_patterns=[], show=False, mark=-1):  # todo make optimizations
				
				# patterns_all = check_all_patterns(text_encrypt, 4, cal_pattern_length, 3, check_patterns(text_encrypt))
				# print("Patterns 3 shorter:" + " " * 28, patterns_all)
				name = "Calculated and checked pattern test:"
				if cal_pattern_length == patterns_over[0][0]:
					print(name + " " * 11, "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
				else:
					print(name + " " * 11, "[" + bcolors.BOLD + bcolors.WARNING + "FAIL" + bcolors.ENDC + "]")
			else:
				print("Patterns over:" + " " * 33, "[Text to short]")
	
	
	# Calculated number of combination
	cal_name_length = "Calculated number of combination:\t\t\t\t"
	print(cal_name_length + "[" + format(decimal.Decimal(cal_pattern_length), '.2E') + "]")
	
	# Encrypt and decrypt tests
	if ((text_before != text_encrypt) and (text_before == text_decrypt) and (key_enc == key_dec)) or \
			((text_before != text_encrypt) and (text_before != text_decrypt) and (key_enc != key_dec)):
		print("Encrypt, decrypt and keys test:\t\t\t\t\t" + bcolors.BOLD + "[PASS]" + bcolors.ENDC)
	else:
		if ((text_before != text_encrypt) and (text_before != text_decrypt) and (key_enc == key_dec)):
			print("Decrypt test:\t\t\t\t\t\t\t\t\t" + bcolors.WARNING + bcolors.BOLD + "[FAIL]" + bcolors.ENDC)
		else:
			if ((text_before != text_encrypt) and (text_before == text_decrypt) and (key_enc != key_dec)):
				print("Keys test:\t\t\t\t\t\t\t\t\t\t" + bcolors.WARNING + bcolors.BOLD + "[FAIL]" + bcolors.ENDC)
			else:
				if (text_before == text_encrypt):
					print(
						"Encrypt test:\t\t\t\t\t\t\t\t\t" + bcolors.WARNING + bcolors.BOLD + "[FAIL]" + bcolors.ENDC)
	
	print("-" * max_print_length)
