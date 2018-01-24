import decimal
from math import log


from modules.__tools_single import bcolors, generate_from_64b_inter_key
from modules.tools import check_text_const, check_rand_rotors, check_patterns, \
	check_all_patterns, calc_number_comb, print_long, key_from_64b_to_dec





# # bit size of drums in bits
# # drums_contents    "in order", "mixed up"
# # drums_creation    "load", "generate", "generate and save"
# # drums_check       "yes", "no"
# drums_bit = 2
# size_drums = 2 ** drums_bit
# drums_contents = "in order"
# drums_creation = "load"
# drums_check = "yes"
#
# text_length = 0
#
# # "random", "min", "max"
#
# # first is a number of cycles,
# # length is a number of drums
# key_enc = [3, 1, 2, 2]  # 262144 wariacje
# key_dec = [3, 1, 2, 2]
#
# # todo serious things happen here
# size_drums = 2 ** drums_bit
#
#
#
#
# # drum1 = {0 : 2,
# #          1 : 0,
# #          2 : 3,
# #          3 : 1}
# #
# # drum2 = {0 : 3,
# #          1 : 2,
# #          2 : 0,
# #          3 : 1}
# #
# # drum3 = {0 : 3,
# #          1 : 0,
# #          2 : 1,
# #          3 : 2}
# #
# # drums = drum1, drum2, drum3
# # print(drums)
#
# # save_rotors(drums, "./drums/set_drum_2b_")
#
# print(drum1, drum2, drum3)
#
#
# # gen_text() #todo triple size !!!
# # gen_text
# text_before = gen_text(False, False, False, drum1, 0, 1000)
# # text_before = [0, 1, 2, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0]
# # text_before = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]#, 0, 0, 0]
# # text_before = [0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]






def test_print(rotors, key_enc = [], key_dec = [], text_before = [], text_encrypt = [], text_decrypt = [],
               show_all=False, show_first=False, show_short=False, show_calc=False, show_uni=False, max_print_length = 110,
               min_print_length=15, space = 47):
			
	key_enc_before = key_enc[:]
	key_dec_before = key_dec[:]
	if isinstance(key_enc, str):
		key_enc = generate_from_64b_inter_key(key_enc, rotors)
	if isinstance(key_dec, str):
		key_dec = generate_from_64b_inter_key(key_dec, rotors)
	# if text_before == []: text_before = text_encrypt[:]
	
		
	# Checked length of the pattern
	key = key_enc if key_enc else key_dec
	cal_pattern_length = calc_number_comb(rotors, key)
	
	
	
	
	if show_all or show_first:
		# Print rotors
		print_long("Rotor", rotors, min_print_length, max_print_length)
		
		# Print keys
		if key_enc_before and isinstance(key_enc_before, list): print_long("Encrypt key", key_enc, min_print_length, max_print_length, False)
		if key_enc_before and isinstance(key_enc_before, str): print_long("Enc. key in Uni", '[' + key_enc_before + ']', min_print_length, max_print_length, False)
		if key_dec_before and isinstance(key_dec_before, list): print_long("Decrypt key", key_dec, min_print_length, max_print_length, False)
		if key_dec_before and isinstance(key_dec_before, str): print_long("Dec. key in Uni", '[' + key_dec_before + ']', min_print_length, max_print_length, False)
		if key_enc_before: print_long("Enc. int. key", key_enc, min_print_length, max_print_length, False)
		if key_dec_before: print_long("Dec. int. key", key_dec, min_print_length, max_print_length, False)
		
		# Print texts before, encrypt and decrypt
		if text_before:
			if (show_uni == False): print_long("Text before", text_before, min_print_length, max_print_length, False)
			if (show_uni == True): print_long("Text be. in Uni", [chr(a) for a in text_before ], 15, max_print_length, False)
		if text_encrypt:
			if (show_uni == False): print_long("Text encrypt", text_encrypt, min_print_length, max_print_length, False)
			if (show_uni == True): print_long("Text en. in Uni", [chr(a) for a in text_encrypt], 15, max_print_length, False)
		if text_decrypt:
			if (show_uni == False): print_long("Text decrypt", text_decrypt, min_print_length, max_print_length, False)
			if (show_uni == True): print_long("Text de. in Uni", [chr(a) for a in text_decrypt], 15, max_print_length, False)
	
	if show_all or show_short:
		# Print short rotors info
		print("Rotors size in bit:" + " " * (space - 19), "[" + str(int(log(len(rotors[0]), 2))) + " bit]")
		print("Rotors, number existing:" + " " * (space - 24), "[" + str(len(rotors)) + " rotors]")  # number of exists rotors
		key_len = len(key_enc) if key_enc else len(key_dec)
		for i in range(len(rotors), 0, -1):
			if key_len % i == 0:
				print("Rotors, number used:" + " " * (space - 20), "[" + str(i) + " rotors]")
				print("Number of passes:" + " " * (space - 17), "[" + str(key_len // i) + " passes]")
				break
		print("Rotors, number of key-val:" + " " * (space - 26), "[" + format(decimal.Decimal(len(rotors[0])), '.2E') + "]")
		if check_rand_rotors(rotors): # był wybrany tylko 1 DLACZEGO !?
			print("Minimum value in rotor:" + " " * (space - 22) + "[" + str(min(rotors[0])) + " min]")
			print("Maximum value in rotor:" + " " * (space - 22) + "[" + str(max(rotors[0])) + " max]")
			print("Equality test of rotors:" + " " * (space - 23) + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
			if check_rand_rotors(rotors): # był wybrany tylko 1 i do tego kolejny a nie 0 jak poprzednio DLACZEGO !?
				print("Randomness and integrity rotor test:" + " " * (space - 35) + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
			else:
				print("Randomness and integrity rotor test:" + " " * (space - 35) + "[" + bcolors.WARNING + bcolors.BOLD + "FAIL" + bcolors.ENDC + "]")
		else:
			print("Minimum value in rotor:" + " " * (space - 22) + "[" + str(min(rotors[0])) + " min]")
			print("Maximum value in rotor:" + " " * (space - 22) + "[" + str(max(rotors[0])) + " max]")
			print("Equality test of rotors:" + " " * (space - 23) + "[" + bcolors.BOLD + bcolors.ORANGE + "FAIL" + bcolors.ENDC + "[")
		
		
		# Print short keys info
		key_len_before = len(key_enc_before) if key_enc_before else len(key_dec_before)
		key = key_enc_before if key_enc_before else key_dec_before
		print("Key len. in bit:" + " " * (space - 15) + "[" + str(int(log(key_from_64b_to_dec(key), 2))) + " bit]")
		print("Key len. in num. el.:" + " " * (space - 20) + "[" + format(decimal.Decimal(key_len_before), '.2E') + "]")
		print("Key int. len. in num. el.:" + " " * (space - 25) + "[" + format(decimal.Decimal(key_len), '.2E') + "]")
		if (key_enc) and (key_dec):
			print("Key the same:" + " " * (space - 12) + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]") if (key_enc == key_dec)  else \
				print("Key the same:" + " " * (space - 12) + "[" + bcolors.ORANGE + "FAIL" + bcolors.ENDC + "]")
		
		
		# Print short text info
		print("Text before length:" + " " * (space - 18) + "[" + format(decimal.Decimal(len(text_before or text_encrypt)), '.2E') + "]")
		print("Text before constant:" + " " * (space - 20) + "[{}]".format("Yes" if check_text_const(text_before or text_encrypt) else "No"))
	
	# # Calculated variations with repetitions
	# cal_name_length = "Calculated variations with repetitions:\t\t\t"
	# print(cal_name_length + "[" + format(decimal.Decimal(cal_pattern_length), '.2E') + "]")
	
	
	if show_all or show_calc:
		if text_before != [] and check_text_const(text_before):
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
					print(name + " " * (space - 35) + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
				else:
					print(name + " " * (space - 35) + "[" + bcolors.BOLD + bcolors.WARNING + "FAIL" + bcolors.ENDC + "]")
			else:
				print("Patterns over:" + " " * (space - 13) + "[Text to short]")
	
	
	# Calculated number of combination
	cal_name_length = "Calculated number of combination:" + " " * (space - 32)
	print(cal_name_length + "[" + format(decimal.Decimal(cal_pattern_length), '.2E') + "]")

	# Encrypt and decrypt tests
	if text_before and text_decrypt:
		if ((text_before != text_encrypt) and (text_before == text_decrypt) and (key_enc == key_dec)) or \
				((text_before != text_encrypt) and (text_before != text_decrypt) and (key_enc != key_dec)):
			print("Encrypt, decrypt and keys test:" + " " * (space - 30) + "[" +bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
		else:
			if ((text_before != text_encrypt) and (text_before != text_decrypt) and (key_enc == key_dec)):
				print("Decrypt test:" + " " * (
						space - 12) + "[" + bcolors.WARNING + bcolors.BOLD + "FAIL" + bcolors.ENDC + "]")
			else:
				if ((text_before != text_encrypt) and (text_before == text_decrypt) and (key_enc != key_dec)):
					print("Keys test:" + " " * (
							space - 9) + '[' + bcolors.WARNING + bcolors.BOLD + "FAIL" + bcolors.ENDC + "]")
				else:
					if (text_before == text_encrypt):
						print("Encrypt test:" + " " * (
								space - 12) + '[' + bcolors.WARNING + bcolors.BOLD + "FAIL" + bcolors.ENDC + "]")
	
	print("-" * max_print_length)
