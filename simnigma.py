#!/usr/bin/python3


# todo dorób obsługę wyjątków
# todo przenieś z generatorów kluczy funkcje zmieniaja ce 64b na DEC itp do __Tools_single
# todo simnigma
# todo dorób rekurenje do wychodzenia w katalogu ponad ../
# todo zrób mozliwość szyfrowania ponad 8b rotors https://docs.python.org/2/library/struct.html
# todo zrób to na https://stormpath.com/blog/building-simple-cli-interfaces-in-python
# todo przerywanie szukania paternów klawiszem ew. po czasie
# todo generate drum wyeliminuj dic losowe w kolejności przypadkiem zrobione
# todo popraw gen_text
# todo timingi dorub
# todo timingi zrób dekoratorami ?
# todo ogranicz wielkosc slownika do tłumaczenia
# todo auto_generate if change bit
# todo generate or load new dict
# todo komentarze
# todo dlaczego jeśli podaję do metody listę def bleble(self, cos_tam)
# todo      to nie mogę pracować na coś tam i jej zwrucić ?
# rotors rozzezenie na rot zroó” !!
# rotors w 1 pliku
# print_all true or false
# printowanie przebiegu procesu
# przeszukiwanie wzorców max i min albo podział łancucha albo dzielenie przez więcej niż 2
# cycles w kluczu zrób tak żeby 1 znaczyło 1 cykl 2 dwa itd chyba juz jest ?!
# ostatnie wartosci kluczy mogą być wieksze niż max z dic !!!
# key przenieś do metody -1i zamien z hex na liste
# generator klucza do ilosci przejść i bębnów zrub
# karetkę bardziej widoczną zrób
# dorub sprwadzanie max i min słownika czy jest OK i print
# print only 2 decimals
# how to division with out decimal
# drums ---> rotors drum ---> drum
import inspect
import sys
import os
import glob

from modules.tools import encrypt, decrypt, create_random_64b_key, print_long, show_help, \
	convert_str_to_list, convert_list_to_str, load_file_all, save_file_all, printd, create_rotors,\
	check_rand_rotors, check_64b_key


from modules.test_print import test_print
from modules.__tools_single import bcolors

# rotors = create_rotors(12, True, 6)
# save_file_all('for_file_bad', rotors, 'rotors_in_one_file', show=True)
# exit()
# key = create_random_64b_key(9)
# print(type(key))
# key += '?'
# save_file_all('for_file_bad', key, 'key', show=True)
# exit()





version = '5.0.0'
options = sys.argv + [' ',]
options_all = ('-c', '-d', '-k', '-K', '-R', '-r', '-v', '--verbose', '-t', '--tests', '-h', '--help', '-V' ,'--version',
               '-s', '--silent')
max_print_length = 110
min_print_length = 15


files_to_encrypt = []
files_to_decrypt = []
key_name_load = ''
rotors_name_load = ''
key_name_save = ''
key_size = 0
rotors_name_save = ''
rotors_number = 0
show = False
only_screen = False
key = ''
rotors = []
max_print_length = 120
min_print_length = 15
space = 45
debug = False


printd( options, debug=debug)
if '-c' in options:
	for file_my in options[options.index('-c') + 1:]:
		if file_my[0] != '-' and file_my[0] != ' ':
			files_to_encrypt.append(file_my)
		else:
			break
	del options[options.index('-c') + 1: options.index('-c') + len(files_to_encrypt) + 1]
	options.remove('-c')
if '-d' in options:
	for file_my in options[options.index('-d') + 1:]:
		if file_my[0] != '-' and file_my[0] != ' ':
			files_to_decrypt.append(file_my)
		else:
			break
	del options[options.index('-d') + 1: options.index('-d') + len(files_to_decrypt) + 1]
	options.remove('-d')

if '-k' in options:
	if options[options.index('-k') + 1][0] != '-':
		key_name_load += options[options.index('-k') + 1]
	del options[options.index('-k') + 1]
	options.remove('-k')

if '-r' in options:
	if options[options.index('-r') + 1][0] != '-':
		rotors_name_load += options[options.index('-r') + 1]
	del options[options.index('-r') + 1]
	options.remove('-r')

if '-v' in options or '--verbose' in options:
	show = True
	try: options.remove('-v')
	except: options.remove('--verbose')

if '-s' in options or '--silent' in options:
	only_screen = True
	try: options.remove('-s')
	except: options.remove('--silent')

if '-K' in options:
	if options[options.index('-K') + 1][0] != '-':
		key_name_save += options[options.index('-K') + 1]
	try:
		key_size = options[options.index('-K') + 2]
		key_size = int(key_size)
	except:
		show_help('Invalid size of key')
	del options[options.index('-K') + 2]
	del options[options.index('-K') + 1]
	options.remove('-K')

if '-R' in options:
	if options[options.index('-R') + 1][0] != '-':
		rotors_name_save += options[options.index('-R') + 1]
	try:
		rotors_number = options[options.index('-R') + 2]
		rotors_number = int(rotors_number)
	except:
		show_help('Invalid number of rotors')
	del options[options.index('-R') + 2]
	del options[options.index('-R') + 1]
	options.remove('-R')

if '-h' in options  or '--help' in options:
	pass

if '-V' in options or '--version' in options:
	print("Simnigma version", version)


printd( options, files_to_encrypt, files_to_decrypt, key_name_load, key_name_save, key_size,  rotors_name_load, rotors_name_save, rotors_number, only_screen, show, debug=debug)
if len(sys.argv) == 1:
	show_help("No options")
if len(options) > 2:
	show_help("Invalid options")
if '-c' in sys.argv and files_to_encrypt == []:
	show_help("File to encrypt or to save if -s")
if '-d' in sys.argv and files_to_decrypt == []:
	show_help("File to decrypt or to load if -s")
if '-k' in sys.argv and key_name_load == ' ':
	show_help("Name of key to load")
if '-r' in sys.argv and rotors_name_load == ' ':
	show_help("Name of rotors to load")
if '-c' in sys.argv and len(files_to_encrypt) != 1 and only_screen:
	show_help("Too many files to save if -s")
if '-d' in sys.argv and len(files_to_decrypt) != 1 and only_screen:
	show_help("Too many files to load if -s")
if ('-c' in sys.argv or '-d' in sys.argv) and ('-K' in sys.argv or '-R' in sys.argv):
	show_help("Too many options, at the same time you can't encrypt/decrypt and create key or rotors")
if ('-K' in sys.argv or '-R' in sys.argv) and ('-s') in sys.argv:
	show_help("Too many options, at the same time you can't create key or rotors in silent mode")

if key_name_load:
	printd(key_name_load, debug=debug)
	if key_name_load[0] == '/':
		key = load_file_all(key_name_load, 'key', True)
	elif key_name_load[0:2] == '..':
		key = load_file_all(os.getcwd()[:os.getcwd().rfind('/')] + key_name_load[2:], 'key', True)
	elif key_name_load[0:2] == './':
		key = load_file_all(os.getcwd() + key_name_load[1:], 'key', True)
	elif key_name_load[-4:] == '.key':
		key = load_file_all(os.getcwd() + '/' + key_name_load, 'key', True)
	elif key_name_load:
		key = load_file_all(options[0][:options[0].rfind('/')] + '/keys/' + key_name_load, 'key', True)
elif ('-c' in sys.argv) or ('-d' in sys.argv):
	if sys.platform == 'linux':
		if glob.glob("/media/**/*.key", recursive=True):
			key_name_load = max(glob.glob("/media/**/*.key", recursive=True), key=os.path.getatime)
			key = load_file_all(key_name_load, 'key', True)
	if (glob.glob(options[0][:options[0].rfind('/') + 1] + 'keys/*'))  and not key:
		key_name_load = max(glob.glob(options[0][:options[0].rfind('/') + 1] + 'keys/*'), key=os.path.getatime)
		key = load_file_all(key_name_load, 'key', True)
printd(key, debug=debug)
if key:
	if check_64b_key(key):
		if show==False: print("Key test:" + " " * (space - 6) + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
	else:
		show_help("Key {} are broken, make new or del broken".format(key_name_load))
else:
	show_help("You don't have any keys, make or connect USB with key")



if rotors_name_load:
	printd(rotors_name_load, debug=debug)
	if rotors_name_load[0] == '/':
		rotors = load_file_all(rotors_name_load, 'rotors_from_one_file', True)
	elif rotors_name_load[0:2] == '..':
		rotors = load_file_all(os.getcwd()[:os.getcwd().rfind('/')] + rotors_name_load[2:], 'rotors_from_one_file', True)
	elif rotors_name_load[0:2] == './':
		rotors = load_file_all(os.getcwd() + rotors_name_load[1:], 'rotors_from_one_file', True)
	elif rotors_name_load[-4:] == '.rotor':
		rotors = load_file_all(os.getcwd() + '/' + rotors_name_load, 'rotors_from_one_file', True)
	elif rotors_name_load:
		rotors = load_file_all(options[0][:options[0].rfind('/')] + '/rotors/' + rotors_name_load, 'rotors_from_one_file', True)
elif ('-c' in sys.argv) or ('-d' in sys.argv):
	if sys.platform == 'linux':
		if glob.glob("/media/**/*.rotors", recursive=True):
			rotors_name_load = max(glob.glob("/media/**/*.rotors", recursive=True), key=os.path.getatime)
			rotors = load_file_all(rotors_name_load, 'rotors_from_one_file', True)
	if (glob.glob(options[0][:options[0].rfind('/') + 1] + 'rotors/*.rotors')) and not rotors:
		rotors_name_load = max(glob.glob(options[0][:options[0].rfind('/') + 1] + 'rotors/*.rotors'), key=os.path.getatime)
		rotors = load_file_all(rotors_name_load, 'rotors_from_one_file', True)
printd(rotors, debug=debug)
if rotors:
	if check_rand_rotors(rotors):
		if min(rotors[0]) == 0 and max(rotors[0]) == 255 and min(rotors[0].values()) == 0 and max(rotors[0].values()) == 255:
			if show==False: print("Randomness and integrity rotor test:" + " " * (space - 33) + "[" + bcolors.BOLD + "PASS" + bcolors.ENDC + "]")
		else:
			show_help("Rotors {} are broken, make new or del broken".format(rotors_name_load))
else:
	show_help("You don't have any rotors, make or connect USB with rotors")




if files_to_encrypt and  not only_screen:
	printd(files_to_encrypt, debug=debug)
	for file_my in files_to_encrypt[:]:
		if os.stat(str(os.path.abspath('') + '/' + file_my)).st_size > 0:
			files_to_encrypt[files_to_encrypt.index(file_my)] = str(os.path.abspath('') + '/' + file_my)
		else:
			print(bcolors.IMPORTANT + "Warning: Empty file {}".format(file_my) + bcolors.ENDC)
			files_to_encrypt.remove(file_my)
	for file_my in files_to_encrypt[:]:
		if not os.path.isfile(file_my):
			print(bcolors.WARNING + '"{}" this isn\'t a file'.format(file_my) + bcolors.ENDC)
			files_to_encrypt.remove(file_my)
	for file_my in files_to_encrypt:
		text_before = load_file_all(file_my, 'file', True)
		text_encrypt = encrypt(rotors, key, text_before)
		save_file_all(file_my + '.enc', text_encrypt, 'file', True)
		if show: test_print(rotors=rotors, key_enc=key, text_before=text_before, text_encrypt=text_encrypt,
		                    show_all=True, show_uni=True, max_print_length=max_print_length, min_print_length=min_print_length,
		                    space=space)
if files_to_encrypt and only_screen:
	printd(files_to_encrypt, debug=debug)
	print("Enter/Paste your content. Ctrl-D or Ctrl-C to save it.")
	text_before = ''
	while True:
		try:
			if text_before: text_before += '\n'
			text_before += input('---> ')
		except KeyboardInterrupt:
			break
		except EOFError:
			break
	text_before = convert_str_to_list(text_before)
	text_encrypt = encrypt(rotors, key, text_before)
	save_file_all(files_to_encrypt[0] + '.enc', text_encrypt, 'file', True)
	if show: test_print(rotors=rotors, key_enc=key, text_before=text_before, text_encrypt=text_encrypt,
	                    show_all=True, show_uni=True)
	

if files_to_decrypt and not only_screen:
	printd(files_to_decrypt, debug=debug)
	for file_my in files_to_decrypt[:]:
		if os.stat(str(os.path.abspath('') + '/' + file_my)).st_size > 0:
			files_to_decrypt[files_to_decrypt.index(file_my)] = str(os.path.abspath('') + '/' + file_my)
		else:
			print(bcolors.IMPORTANT + "Warning: Empty file {}".format(file_my) + bcolors.ENDC)
			files_to_decrypt.remove(file_my)
	for file_my in files_to_decrypt[:]:
		if (not os.path.isfile(file_my) or (file_my[-4:] != '.enc')):
			print(bcolors.WARNING + '"{}" this isn\'t a .enc file'.format(file_my) + bcolors.ENDC)
			files_to_decrypt.remove(file_my)
	for file_my in files_to_decrypt:
		text_encrypt = load_file_all(file_my, 'file', True)
		text_decrypt = decrypt(rotors, key, text_encrypt)
		save_file_all(file_my + '.dec', text_decrypt, 'file', True)
		if show: test_print(rotors=rotors, key_enc=key, text_encrypt=text_encrypt, text_decrypt=text_decrypt,
		                    show_all=True, show_uni=True, max_print_length=max_print_length, min_print_length=min_print_length,
		                    space=space)
if files_to_decrypt and only_screen :
	printd(files_to_decrypt, debug=debug)
	for file_my in files_to_decrypt[:]:
		if os.stat(str(os.path.abspath('') + '/' + file_my)).st_size > 0:
			files_to_decrypt[files_to_decrypt.index(file_my)] = str(os.path.abspath('') + '/' + file_my)
		else:
			exit(bcolors.IMPORTANT + "Warning: Empty file {}".format(file_my) + bcolors.ENDC)
	for file_my in files_to_decrypt[:]:
		if (not os.path.isfile(file_my) or (file_my[-4:] != '.enc')):
			exit(bcolors.WARNING + '"{}" this isn\'t a .enc file'.format(file_my) + bcolors.ENDC)
	for file_my in files_to_decrypt:
		text_encrypt = load_file_all(file_my, 'file', True)
		text_decrypt = decrypt(rotors, key, text_encrypt)
		if show: test_print(rotors=rotors, key_enc=key, text_encrypt=text_encrypt, text_decrypt=text_decrypt,
		                    show_all=True, show_uni=True)
		text_decrypt = convert_list_to_str(text_decrypt[:-1])
		text_decrypt = text_decrypt.split('\n')
		for line in text_decrypt:
			print('---> ', line)


if key_name_save:
	printd(key_name_save, key_size, debug=debug)
	key = create_random_64b_key(key_size, max_print_length=max_print_length, show=show)
	print('Key created:   ', key_name_save, str(key_size) + " bit")
	key_name_save = options[0][:options[0].rfind('/')] + '/keys/' + key_name_save
	save_file_all(key_name_save, key, 'key', show=True)
	printd(key, debug=debug)
if rotors_name_save:
	printd(rotors_name_save, rotors_number, debug=debug)
	rotors = create_rotors(8, True, rotors_number)
	print('Rotors created:', rotors_name_save, str(rotors_number) + " items")
	rotors_name_save = options[0][:options[0].rfind('/')] + '/rotors/' + rotors_name_save
	save_file_all(rotors_name_save, rotors, 'rotors_in_one_file', show=True)
	printd(rotors, debug=debug)
	

	
printd(' OK ')
exit()
	

# todo ---------- this part is our playground :)----------
	# print("--files_to_encrypt:", files_to_crypt)
	#
	# print('------------------------')
	# print(rotors)
	# print(len(rotors))
	# print(key)
	# print('options_current, options_neg', options_current, options_neg)
	# exit('stop')
	
	
	
	
	
	
	# print('last------', last_rotors_in_dir)
	
	# print('1--', options)
	# print('2--', options[0])
	# print('3--', options[0][:options[0].rfind('/')])
	# print('4--', options[0][:options[0].rfind('/')] + '/rotors/')
	# print('5--', glob.glob(options[0][:options[0].rfind('/')] + '/rotors/*'))
	# print('6--', max(glob.glob(options[0][:options[0].rfind('/')] + '/rotors/*'), key = os.path.getatime))
	# last_rotors_in_dir = max(glob.glob(options[0][:options[0].rfind('/')] + '/rotors/*'), key = os.path.getatime)
	# print('7--', last_rotors_in_dir[:last_rotors_in_dir.rfind('_')])
	# print('2--', glob.glob(options[0][:options[0].rfind('/')]))
	# print(glob.glob())
	# last_rotors_in_dir = last_rotors_in_dir[:last_rotors_in_dir.rfind('_')])
	
	# last_rotor_in_dir = max(glob.glob(options[0][:-10] + 'rotors/*'), key=os.path.getatime)
	
	# print("-", options)
	# print('--', options.index('-r') + 1)
	# print('--3', os.getcwd())
	# print('--4', os.getcwd().rfind('/'))
	# print('--5', os.getcwd()[:os.getcwd().rfind('/')])
	# print('--6', options[options.index('-r') + 1][:options[options.index('-r') + 1].rfind('_')])
	# print('--8', options[options.index('-r') + 1].rfind('_'))
	# print('--9', options[options.index('-r') + 1][2:options[options.index('-r') + 1].rfind('_')])
	# print('--10', os.getcwd()[:os.getcwd().rfind('/')] + options[options.index('-r') + 1][
	#                                                      2:options[options.index('-r') + 1].rfind('_')])
	# print('--11',
	#       os.getcwd() + '/' + options[options.index('-r') + 1][2:options[options.index('-r') + 1].rfind('_')])
	#
	
	
	
	# print('--11', number_of_rotors)
	
	# print('---', options[options.index('-r') + 1])
	# print('----', options[options.index('-r') + 1].rfind('_'))
	# print('-----', options[options.index('-r') + 1][:options[options.index('-r') + 1].rfind('_')])
	# a = options[options.index('-r') + 1][:options[options.index('-r') + 1].rfind('_')]
	# print('------', glob.glob(a + '*'))
	# print('-------', len(glob.glob(a +'*')))
	
	
	
	
	
	
	# rotors_name = ''
	# last_rotor_in_dir = max(glob.glob(options[0][:-10] + 'rotors/*'), key=os.path.getatime)
	# for x in range(len(last_rotor_in_dir), 0, -1):
	# 	if last_rotor_in_dir[x - 1] == '_':
	# 		rotors_name = last_rotor_in_dir[0:x - 1]
	# 		break
	# number_of_rotors = len(glob.glob(rotors_name + "*"))
	# print('-------------', rotors_name)
	# rotors = load_rotors(rotors_name, number_of_rotors)
	
	
	
	
	
	

			
			
			
	#
	#
	# print("files_to_encrypt:", files_to_encrypt)
	#
	#
	# print('------------------------')
	# print(rotors)
	# print(len(rotors))
	# print(key)
	# print('options_current, options_neg', options_current, options_neg)
	# # exit('stop')
	
	

	
	# for file in files_to_encrypt:
	# 	# print(file)
	# 	text_before = load_file(file)
	# 	if(text_before) == []:
	# 		continue
	# 	# print("-----------------------------------------", text_before)
	# 	text_encrypt = encrypt(rotors, key, text_before)
	# 	# def save_file(name, file):
	# 	save_file(file + ".enc", text_encrypt)
# elif ("-d" in options):
# 	show = True if (("-v") or ("--verbose")) in options else False
#
# 	files_to_decrypt = []
# 	for file_my in options[options.index("-d") + 1:len(options)]:
# 		if file_my[-4:] == '.enc':
# 			print(file_my)
# 			if os.path.isfile(file_my):
# 				files_to_decrypt.append(os.path.abspath('') + '/' + file_my)
# 	# print("files_to_encrypt:", files_to_encrypt)
#
# 	key = ''
# 	if ("-k" in options):
# 		key_in_dir = options[options.index('-k') + 1]
# 		print(key_in_dir)
# 		key = load_key(key_in_dir)
# 	else:
# 		last_key_in_dir = max(glob.glob(options[0][:-10] + 'keys/*'), key=os.path.getatime)
# 		key = load_key(last_key_in_dir)
#
# 	rotors_name = ''
# 	last_rotor_in_dir = max(glob.glob(options[0][:-10] + 'rotors/*'), key=os.path.getatime)
# 	for x in range(len(last_rotor_in_dir), 0, -1):
# 		if last_rotor_in_dir[x - 1] == '_':
# 			rotors_name = last_rotor_in_dir[0:x - 1]
# 			break
# 	number_of_rotors = len(glob.glob(rotors_name + "*"))
# 	rotors = load_rotors(rotors_name, number_of_rotors)
#
# 	for file in files_to_decrypt:
# 		# print(file)
# 		text_encrypt = load_file(file)
# 		if (text_encrypt) == []:
# 			continue
# 		# print("-----------------------------------------", text_encrypt)
# 		text_decrypt = decrypt(rotors, key, text_encrypt)
# 		# def save_file(name, file):
# 		save_file(file + ".dec", text_decrypt)
#
#
# 	# print(key)
# 	# print(rotors[0])
#
	


# print("helo from:", __name__)






#
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
#
#
# encrypt_first = EncryptFirstDrum(key_enc, drum1)
# encrypt_drum1 = EncryptNextRotor(drum1)
# encrypt_drum2 = EncryptNextRotor(drum2)
# encrypt_drum3 = EncryptNextRotor(drum3)
# encrypt_drum4 = EncryptNextRotor(drum3)
# encrypt_drum5 = EncryptNextRotor(drum3)
# encrypt_drum6 = EncryptNextRotor(drum3)
# encrypt_drum7 = EncryptNextRotor(drum3)
# encrypt_drum8 = EncryptNextRotor(drum3)
# encrypt_drum9 = EncryptNextRotor(drum3)
# encrypt_drum10 = EncryptNextRotor(drum3)
#
# decrypt_first = DecryptFirstDrum(key_dec, drum1)
# decrypt_drum1 = DecryptNextRotor(drum1)
# decrypt_drum2 = DecryptNextRotor(drum2)
# decrypt_drum3 = DecryptNextRotor(drum3)
# decrypt_drum4 = DecryptNextRotor(drum3)
# decrypt_drum5 = DecryptNextRotor(drum3)
# decrypt_drum6 = DecryptNextRotor(drum3)
# decrypt_drum7 = DecryptNextRotor(drum3)
# decrypt_drum8 = DecryptNextRotor(drum3)
# decrypt_drum9 = DecryptNextRotor(drum3)
# decrypt_drum10 = DecryptNextRotor(drum3)
#
# enc = []
# while True:
#     enc = encrypt_first.set_encyc_and_i(enc, text_before[:])
#     enc = encrypt_drum1.encrypt(enc)
#     enc = encrypt_drum2.encrypt(enc)
#     enc = encrypt_drum3.encrypt(enc)
#     enc = encrypt_drum4.encrypt(enc)
#     enc = encrypt_drum5.encrypt(enc)
#     enc = encrypt_drum6.encrypt(enc)
#     enc = encrypt_drum7.encrypt(enc)
#     enc = encrypt_drum8.encrypt(enc)
#     enc = encrypt_drum9.encrypt(enc)
#     enc = encrypt_drum10.encrypt(enc)
#     # print(enc)
#     if enc[-1] == False:
#         break
# text_encrypt = encrypt_first.get_encrypt_list()
#
#
#
#
# # print("------------")
# dec = []
# while True:
#     dec = decrypt_first.set_decyc_and_i(dec, text_encrypt[:])
#     dec = decrypt_drum10.decrypt(dec)
#     dec = decrypt_drum9.decrypt(dec)
#     dec = decrypt_drum8.decrypt(dec)
#     dec = decrypt_drum7.decrypt(dec)
#     dec = decrypt_drum6.decrypt(dec)
#     dec = decrypt_drum5.decrypt(dec)
#     dec = decrypt_drum4.decrypt(dec)
#     dec = decrypt_drum3.decrypt(dec)
#     dec = decrypt_drum2.decrypt(dec)
#     dec = decrypt_drum1.decrypt(dec)
#     # print(dec)
#     if dec[-1] == False:
#         break
# text_decrypt = decrypt_first.get_encrypt_list()
#
#
#
#
#
# drums = drum1, drum2, drum3 #, drum1, drum2, drum3, drum1, drum2, drum3, drum1, drum2, drum3
#
# from Enigma_all.Enigma_4.modules.test_print import test_print
#
#
#
# # def test_print(drums, key_enc, key_dec, text_before, text_encrypt, text_decrypt, show_all = True):
# test_print(drums, key_enc, key_dec, text_before, text_encrypt, text_decrypt, True)
#
#
#
#
#
#
# # import sys
# # for i in range (0, 10000000):
# #     sys.stdout.write("Download progress: %d%%   \r" % (i) )
# #     sys.stdout.flush()
#
#
