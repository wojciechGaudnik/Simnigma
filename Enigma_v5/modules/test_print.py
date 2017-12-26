from Enigma_all.Enigma_v5.modules.__tools_single import bcolors
from Enigma_all.Enigma_v5.modules.tools import check_text_const, check_rand_rotors, create_key, check_patterns, \
	check_all_patterns, key_in_dec

import decimal
from math import log


def test_print(rotors, key_enc, key_dec, text_before, text_encrypt, text_decrypt,
               show_all=True, show_first=False, show_short=False, show_calc=False):
	print("----------------------------------------------------------------------------------------------------")
	
	# Checked length of the pattern
	cal_pattern_length = 0
	for i in range(len(rotors), 0, -1):
		if len(create_key(key_enc, rotors)) % i == 0:
			cal_pattern_length = (len(rotors[0]) ** i) ** (len(create_key(key_enc, rotors)) // i)
			break
			
	if show_all or show_first:
		# Print rotors
		rotor_number = 1
		for rotor in rotors:
			name_rotor = str("Rotor " + str(rotor_number) + ":")
			name_rotor = name_rotor + (17 - len(name_rotor)) * " "
			if len(name_rotor + str(rotor)) > 82:
				print(name_rotor + str(rotor)[:40] + "  +...+  " + str(rotor)[-34:])
			else:
				print(name_rotor + str(rotor))
			rotor_number += 1
		
		# Print keys
		if len("Encrypt key:" + " " * 5 + "[" + str(", ".join(map(str ,key_enc))) + "]") > 82:
			print("Encrypt key:" + " " * 5 + "[" + str(", ".join(map(str ,key_enc)))[:38].upper(),
			      ("  +...+  " + str(", ".join(map(str ,key_enc)).upper())[-33:] + "]"))
		else:
			print("Encrypt key:" + " " * 4, "[" + str(", ".join(map(str ,key_enc)).upper()) + "]")
		
		if len("Decrypt key:" + " " * 5 + "[" + str(", ".join(map(str ,key_dec))) + "]") > 82:
			print("Decrypt key:" + " " * 5 + "[" + str(", ".join(map(str ,key_dec)))[:38].upper(),
			      ("  +...+  " + str(", ".join(map(str ,key_dec)).upper())[-33:] + "]"))
		else:
			print("Decrypt key:" + " " * 4, "[" + str(", ".join(map(str ,key_dec)).upper()) + "]")
		
		if len("Int. enc. key:" + " " * 3 + str(create_key(key_enc, rotors))) > 82:
			print("Int. enc. key:" + " " * 3 + str(create_key(key_enc, rotors))[:39],
			      ("  +...+  " + str(create_key(key_enc, rotors))[-34:]))
		else:
			print("Int. enc. key:" + " " * 3 + str(create_key(key_enc, rotors)))
		
		if len("Int. dec. key:" + " " * 3 + str(create_key(key_dec, rotors))) > 82:
			print("Int. dec. key:" + " " * 3 + str(create_key(key_dec, rotors))[:39],
			      ("  +...+  " + str(create_key(key_dec, rotors))[-34:]))
		else:
			print("Int. enc. key:" + " " * 3 + str(create_key(key_dec, rotors)))
		
		
		# Print texts before, encrypt and decrypt
		if len(str(text_before)) > 82:
			print("Text before: \t", str(text_before)[:39],("  +...+  " + str(text_before)[-34:]))
		else:
			print("Text before: \t", text_before)
		if len(str(text_encrypt)) > 82:
			print("Text encrypt: \t", str(text_encrypt)[:39],("  +...+  " + str(text_encrypt)[-34:]))
		else:
			print("Text encrypt: \t", text_encrypt)
		if len(str(text_decrypt)) > 82:
			print("Text decrypt: \t", str(text_decrypt)[:39],("  +...+  " + str(text_decrypt)[-34:]))
		else:
			print("Text decrypt: \t", text_decrypt)
		
	if show_all or show_short:
		# Print short rotors info
		print("Rotors, number of key-val:" + " " * 21, "[" + format(decimal.Decimal(len(rotors[0])), '.2E') + "]")
		print("Rotors size in bit:" + " " * 28, "[" + str(int(log(len(rotors[0])) / log(2))) + " bit]")
		print("Rotors, number existing:" + " " * 23, "[" + str(len(rotors)) + " rotors]")  # number of exists rotors
		for i in range(len(rotors), 0, -1):
			if len(key_dec) % i == 0:
				print("Rotors, number used:" + " " * 27, "[" + str(i) + " rotors]")
				print("Number of passes:" + " " * 30, "[" + str(len(key_dec) // i) + " passes]")
				break
		if check_rand_rotors(rotors)[0]:
			print("Minimum value in the rotor:\t\t\t\t\t\t" + "[" + str(min(rotors[0])) + " min]")
			print("Maximum value in the rorot:\t\t\t\t\t\t" + "[" + str(max(rotors[0])) + " max]")
			print("Equality test of rotors:\t\t\t\t\t\t" + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
			if check_rand_rotors(rotors)[1]:
				print("Randomness and integrity rotor test:\t\t\t" + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
			else:
				print("Randomness and integrity rotor test:\t\t\t" + "[" + bcolors.WARNING + bcolors.BOLD + "FAIL" + bcolors.ENDC + "]")
		else:
			print("Minimum value in the rotor:\t\t\t\t\t\t" + "[" + str(min(rotors[0])) + " min]")
			print("Maximum value in the rotor:\t\t\t\t\t\t" + "[" + str(max(rotors[0])) + " max]")
			print("Equality test of rotors:\t\t\t\t\t\t" + "[" + bcolors.BOLD + bcolors.ORANGE + "FAIL" + bcolors.ENDC + "[")
		
		
		# Print short keys info
		print("Key enc. len. in num. el.:" + " " * 21, "[" + format(decimal.Decimal(len(key_enc)), '.2E') + "]")
		print("Key int. enc. len. in num. el.:" + " " * 16, "[" + format(decimal.Decimal(len(create_key(key_enc, rotors))), '.2E') + "]")
		if isinstance(key_enc, str): print("Key size in bit of num. in dec.:" + " " * 15, "[" + str(int(log(key_in_dec(key_enc)) / log(2) + 1)) + " bit]")
		print("Key test the same:" + " " * 29, "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]") if key_enc == key_dec else \
			print("Key test the same:" + " " * 29, "[" + bcolors.ORANGE + "FAIL" + bcolors.ENDC + "]")
		
			
		# Print short text info
		print("Text before length:" + " " * 28, "[" + format(decimal.Decimal(len(text_before)), '.2E') + "]")
		print("Text before constant:" + " " * 26, "[{}]".format("Yes" if check_text_const(text_before) else "No"))
	
	if show_all or show_calc:
		if check_text_const(text_before):
			check_name_length = "Checked length of the pattern:\t\t\t\t\t"
			if len(text_encrypt) > cal_pattern_length * 3:
				patterns_over = check_patterns(text_encrypt, cal_pattern_length // 2)
				print("Patterns over, max 3:" + " " * 26, [x for x in patterns_over[0: 3]])
				patterns_all = check_all_patterns(4, cal_pattern_length, 3, text_encrypt, check_patterns(text_encrypt))
				print("Patterns 3 shorter:" + " " * 28, patterns_all)
				name = "Calculated and checked pattern test:"
				if cal_pattern_length == patterns_over[0][0]:
					print(name + " " * 11, "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
				else:
					print(name + " " * 11, "[" + bcolors.BOLD + bcolors.WARNING + "FAIL" + bcolors.ENDC + "]")
			else:
				print("Patterns over:" + " " * 33, "[text to short]")
			
			
	# Calculated variations with repetitions
	cal_name_length = "Calculated variations with repetitions:\t\t\t"
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

