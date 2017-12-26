from Enigma_all.Enigma_v5.modules.core import (EncryptFirstDrum, EncryptNextRotor,
                                               DecryptFirstDrum, DecryptNextRotor,
                                               )
from Enigma_all.Enigma_v5.modules.tools import save_rotors, load_rotors
from Enigma_all.Enigma_v5.modules.tests_def import sdfasdf



# todo generate drum wyeliminuj dic losowe w kolejności przypadkiem zrobione
# todo przeszukiwanie wzorców max i min albo podział łancucha albo dzielenie przez więcej niż 2
# todo popraw gen_text
# todo key przenieś do metody -1i zamien z hex na liste
# todo timingi dorub
# todo timingi zrób dekoratorami ?
# todo ogranicz wielkosc slownika do tłumaczenia
# todo printowanie przebiegu procesu
# todo print_all true or false
# todo auto_generate if change bit
# todo generate or load new dict
# todo komentarze
# todo ostatnie wartosci kluczy mogą być wieksze niż max z dic !!!
# todo dlaczego jeśli podaję do metody listę def bleble(self, cos_tam)
# todo      to nie mogę pracować na coś tam i jej zwrucić ?
# todo cycles w kluczu zrób tak żeby 1 znaczyło 1 cykl 2 dwa itd chyba juz jest ?!
# karetkę bardziej widoczną zrób
# dorub sprwadzanie max i min słownika czy jest OK i print
# print only 2 decimals
# how to division with out decimal
# drums ---> rotors drum ---> drum


# todo ---------- this part is our playground :)----------






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
