#!/usr/bin/python3


# todo simnigma
# todo dorób rekurenje do wychodzenia w katalogu ponad ../
# todo rotors rozzezenie na rot zroó” !!
# todo zrób mozliwość szyfrowania ponad 8b rotors https://docs.python.org/2/library/struct.html
# todo zrób to na https://stormpath.com/blog/building-simple-cli-interfaces-in-python
# todo dorób obsługę wyjątków
# todo przenieś z generatorów kluczy funkcje zmieniaja ce 64b na DEC itp do __Tools_single
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



import sys
import os
import glob

from modules.__tools_single import bcolors

from modules.tools import load_key, save_key, load_rotors, load_file, encrypt, decrypt, create_rotors, save_rotors,\
	save_file, create_random_64b_key, print_long, show_help
from modules.test_print import test_print


# rotors = create_rotors(8, True, 6)
# save_rotors(rotors,"./rotors/for_file")

version = '5.0.0'
options = sys.argv
options_all = ('-c', '-d', '-k', '-K', '-R', '-r', '-v', '--verbose', '-t', '--tests', '-h', '--help', '-V' ,'--version')
max_print_length = 110
min_print_length = 15

options_current = list(filter(lambda opt: opt in options_all , options))
for opt in options_current:
	if options_current.count(opt) > 1:
		show_help()
		print('---- początek')
		exit()
options_param = list(filter(lambda opt: opt not in options_all, options))
options_param = options_param[1:]


show = False
if (('-v') or ('--verbose')) in options_current:
	show = True
	options_current.remove('-v') if ('-v') in options_current else options_current.remove('--verbose')

if ('-c' in options_current) or ('-d' in options_current):
	
	key = ''
	if '-k' in options_current:
		options_current.remove('-k')
		key_in_dir =''
		# if key full path
		if options[options.index('-k') + 1][0] == '/':
			key_in_dir = options[options.index('-k') + 1]
			key = load_key(key_in_dir)
			options_param.remove(options[options.index('-k') + 1])
		# if key path with '..'
		elif options[options.index('-k') + 1][0:2] == '..':
			key_in_dir = os.getcwd()[:os.getcwd().rfind('/')] + options[options.index('-k') + 1][2:]
			key = load_key(key_in_dir)
			options_param.remove(options[options.index('-k') + 1])
		# if key path with './'
		elif options[options.index('-k') + 1][0:2] == './':
			key_in_dir = os.getcwd() + options[options.index('-k') + 1][1:]
			key = load_key(key_in_dir)
			options_param.remove(options[options.index('-k') + 1])
		# if current directrory with .key
		elif options[options.index('-k') + 1][-4:] == '.key':
			key_in_dir = os.getcwd() + '/' + options[options.index('-k') + 1]
			key = load_key(key_in_dir)
			options_param.remove(options[options.index('-k') + 1])
		# if key only name
		else:
			key_in_dir = options[0][:options[0].rfind('/')] + '/keys/' + options[options.index('-k') + 1]
			options_param.remove(options[options.index('-k') + 1])
			key = load_key(key_in_dir)
		print('Loaded key:   ', key_in_dir)
	# if no -k then latest
	else:
		last_key_in_dir = max(glob.glob(options[0][:options[0].rfind('/') + 1] + 'keys/*'), key=os.path.getatime)
		key = load_key(last_key_in_dir)
		print('Loaded key:   ', last_key_in_dir)
	
	rotors = []
	name_of_rotors_in_dir = ''
	last_rotors_in_dir = ''
	if '-r' in options_current:
		options_current.remove('-r')
		# if rotor full path
		if options[options.index('-r') + 1][0] == '/':
			name_of_rotors_in_dir = options[options.index('-r') + 1][:options[options.index('-r') + 1].rfind('_')]
			number_of_rotors = len(glob.glob(name_of_rotors_in_dir + '*'))
			rotors = load_rotors(name_of_rotors_in_dir, number_of_rotors)
			while (options[options.index('-r') + 1]) in options_param:
				options_param.remove(options[options.index('-r') + 1])
		# if rotor path with '..'
		elif options[options.index('-r') + 1][0:2] == '..':
			name_of_rotors_in_dir = os.getcwd()[:os.getcwd().rfind('/')] + options[options.index('-r') + 1][
			                                                        2:options[options.index('-r') + 1].rfind('_')]
			number_of_rotors = len(glob.glob(name_of_rotors_in_dir + '*'))
			rotors = load_rotors(name_of_rotors_in_dir, number_of_rotors)
			while (options[options.index('-r') + 1]) in options_param:
				options_param.remove(options[options.index('-r') + 1])
		# if rotor path with './'
		elif options[options.index('-r') + 1][0:2] == './':
			name_of_rotors_in_dir = os.getcwd() + '/' + options[options.index('-r') + 1][2:options[options.index('-r') + 1].rfind('_')]
			number_of_rotors = len(glob.glob(name_of_rotors_in_dir + '*'))
			rotors = load_rotors(name_of_rotors_in_dir, number_of_rotors)
			while (options[options.index('-r') + 1]) in options_param:
				options_param.remove(options[options.index('-r') + 1])
		# if current directrory with .pkl
		elif options[options.index('-r') + 1][-4:] == '.pkl':
			name_of_rotors_in_dir = os.getcwd() + '/' + options[options.index('-r') + 1][:options[options.index('-r') + 1].rfind('_')]
			number_of_rotors = len(glob.glob(name_of_rotors_in_dir + '*'))
			rotors = load_rotors(name_of_rotors_in_dir, number_of_rotors)
			while (options[options.index('-r') + 1]) in options_param:
				options_param.remove(options[options.index('-r') + 1])
		# if only name
		else:
			name_of_rotors_in_dir = options[0][0:options[0].rfind('/')] + '/rotors/' + options[options.index('-r') + 1]
			number_of_rotors = len(glob.glob(options[0][0:options[0].rfind('/')] + '/rotors/' + options[options.index('-r') + 1] + '*'))
			rotors = load_rotors(name_of_rotors_in_dir, number_of_rotors)
			
			while (options[options.index('-r') + 1]) in options_param:
				options_param.remove(options[options.index('-r') + 1])
	# if no -r then latest
	else:
		last_rotors_in_dir = max(glob.glob(options[0][:options[0].rfind('/')] + '/rotors/*'), key = os.path.getatime)[:max(glob.glob(options[0][:options[0].rfind('/')] + '/rotors/*'), key = os.path.getatime).rfind('_')]
		number_of_rotors = len(glob.glob(last_rotors_in_dir + '*'))
		rotors = load_rotors(last_rotors_in_dir, number_of_rotors)
	if name_of_rotors_in_dir: print('Loaded rotors:', name_of_rotors_in_dir)
	if last_rotors_in_dir: print('Loaded rotors:', last_rotors_in_dir)

	
	files_to_crypt = []
	number_of_files = 0
	for file_my in options_param[:]: # todo sprawdź from -c do next in options_all
		if os.path.isfile(file_my):
			files_to_crypt.append(os.path.abspath('') + '/' + file_my)
			options_param.pop(options_param.index(file_my))
		elif os.path.isdir(file_my):
			options_param.pop(options_param.index(file_my))
		else:
			print(bcolors.BOLD + bcolors.WARNING + '"{}" this isn\'t a file'.format(file_my[file_my.rfind('/') + 1:]) + bcolors.ENDC)
	
	if ('-c' in options_current):
		options_current.remove('-c')
		if options_current:
			show_help()
			print('----176')
		for file in files_to_crypt:
			text_before = load_file(file)
			if(text_before) == []:
				continue
			print('Encrypt file: ', file)
			text_encrypt = encrypt(rotors, key, text_before)
			save_file(file + ".enc", text_encrypt)
			if show: test_print(rotors=rotors, key_enc=key, text_before=text_before, text_encrypt=text_encrypt, show_all=True, show_uni=True)
	
	
	# def test_print(rotors, key_enc=[], key_dec=[], text_before=[], text_encrypt=[], text_decrypt=[],
	#                show_all=False, show_first=False, show_short=False, show_calc=False, show_uni=False):
	
	if ('-d' in options_current):
		options_current.remove('-d')
		if options_current:
			show_help()
			print('----194')
		for file_my in files_to_crypt:
			if file_my[-4:] != '.enc':
				print(bcolors.BOLD + bcolors.WARNING + '"{}" this isn\'t a .enc file'.format(file_my[file_my.rfind('/') + 1:]) + bcolors.ENDC)
				continue
			text_before = load_file(file_my)
			if(text_before) == []:
				continue
			print('Decrypt file: ', file_my)
			text_decrypt = decrypt(rotors, key, text_before)
			save_file(file_my + ".dec", text_decrypt)
			if show: test_print(rotors=rotors, key_dec=key, text_encrypt=text_before, text_decrypt=text_decrypt, show_all=True, show_uni=True)

	
elif ('-R' in options_current) or ('-K' in options_current):
	if ('-K' in options_current):
		name_of_key = options[0][:options[0].rfind('/')] + '/keys/' + options[options.index('-K') + 1]
		key_size = 	options[options.index('-K') + 2]
		options_current.remove('-K')
		options_param.remove(options[options.index('-K') + 1])
		options_param.remove(options[options.index('-K') + 2])
		if options_current:
			show_help()
			print('----217')
		key = create_random_64b_key(int(key_size))
		save_key(name_of_key, key)
		print('Key created:    ', name_of_key + '.key')
		if show: print_long("Key", '[' + key + ']', min_print_length, max_print_length, True)
	if ('-R' in options_current):
		options_current.remove('-R')
		name_of_rotors_in_dir = options[options.index('-R') + 1]
		options_param.remove(name_of_rotors_in_dir)
		number_of_rotors = int(options[options.index('-R') + 2])
		options_param.remove(str(number_of_rotors))
		if options_current:
			show_help()
			print('----230')
		rotors = create_rotors(8, True, number_of_rotors)
		name_of_rotors_in_dir = options[0][:options[0].rfind('/')] + '/rotors/' + name_of_rotors_in_dir
		save_rotors(rotors, name_of_rotors_in_dir)
		for r in range(1, number_of_rotors + 1):
			print('Rotor {} created:'.format(r), name_of_rotors_in_dir + '_' + str(r) + '.pkl')
		if show: print_long("Rotor", rotors, min_print_length, max_print_length, False)

elif ('-t' in options_current) or ('--tests' in options_current):
	pass
elif ('-h' in options_current) or ('--help' in options_current):
	show_help()
elif ('-V' in options_current) or ('--version' in options_current):
	print("Enigma version", version)
else:
	show_help()
	print('----na koncu')


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
