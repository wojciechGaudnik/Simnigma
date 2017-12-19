# only functions to generate tools for ten drums tests encrypts

from Enigma_all.Enigma_4.modules.tools import (create_drums, create_and_save_dicts, load_drums,
                                                 check_rand_dicts)
from Enigma_all.Enigma_4.modules.__tools_single import gen_text

drums_bit = 8
debug = True # todo przenieś to głównego ???
random_drums = True
random_text_before = True
dir_name = ""

size_drums = 2 ** drums_bit

# drums generate and save
create_and_save_dicts(create_drums(size_drums, random_drums), ("../drums/drum2b_"))

# drums load
drum2b_1, drum2b_2, drum2b_3, drum2b_4, drum2b_5, drum2b_6, drum2b_7, \
drum2b_8, drum2b_9, drum2b_10 = load_drums("../drums/drum2b_")

# drums check
check_rand_dicts(load_drums("../drums/drum2b_"), debug) #todo FORMATOWANIE PASS!!!

# (Char_max, ran, size_double, drum_for_gen, char, size)
# todo napisz to po angielsku
# text_before = gen_text(False, False, False, drum2b_1)

# text_before = "dupa jaś"
# from Enigma_all.Enigma_4.modules.__tools_single import __save_drum, __load_drum
#
# __save_drum(text_before)


#
#
# y = load_10_dicts("../drums/drum2b_")
# print(y)
# drum2b_1, drum2b_2, drum2b_3, drum2b_4, drum2b_5, drum2b_6, drum2b_7, \
# drum2b_8, drum2b_9, drum2b_10 = y

# print("-------")
# print(drum2b_1)
# print("--------------------------------------------------------------------")
# print("Text before: \t", str(text_before[0:11]).replace("]", ", + ... ]\t"),
#       format(decimal.Decimal(len(text_before)), '.2E')) if len(str(text_before)) >= 11 else \
#     print("Text before: \t", text_encrypt)
# print("Text encrypt:\t", str(text_encrypt[0:15]).replace("]", ","), "...]")
# print("Text decrypt:\t", str(text_decrypt[0:15]).replace("]", ","), "...]")
# print("--------------------------------------------------------------------")






# def test_10d_2b_1d_1c_tk_rand
# def test_10d_2b_1d_1c_tk_min
# def test_10d_2b_1d_1c_tk_max




# def test_10d_4b_4d_300c_tk_():


# drum2b_1, drum2b_2, drum2b_3, drum2b_4, drum2b_5, drum2b_6, drum2b_7,\
# drum2b_8, drum2b_9, drum2b_10 = create_10_dicts(size_drums, True)
