# only functions to generate tools for ten drums tests encrypts
from Enigma_all.Enigma_v5.modules.core import EncryptSet, EncryptNextDrum, DecryptSet, DecryptNextDrum
from Enigma_all.Enigma_v5.modules.tools import save_drums, load_drums


def test_3d_2b ():
    drum1, drum2, drum3 = load_drums("./drums/set_drum_2b_", 3)
    key_enc = [0, 2, 2, 0, 1, 2, 3, 3, 3, 3, 3, 3] #todo zamieniam 1 na 0 pod kątem new. algo
    key_dec = [0, 2, 2, 0, 1, 2, 3, 3, 3, 3, 3, 3]
    text_before = [0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
    text_encrypt = []
    text_decrypt = []
    
    encrypt_drum1 = EncryptNextDrum(drum1)
    encrypt_drum2 = EncryptNextDrum(drum2)
    encrypt_drum3 = EncryptNextDrum(drum3)
    encrypt_first = EncryptSet(key_enc[:], text_before[:], drum1)

    enc = [True]
    while True:
        pass
        enc = encrypt_first.set_enc_chain(enc)
        enc = encrypt_drum1.encrypt(enc)
        enc = encrypt_drum2.encrypt(enc)
        enc = encrypt_drum3.encrypt(enc)
        print(enc)
        if enc[-1] == False:
            break
    text_encrypt = encrypt_first.get_encrypt_list()
    print(text_encrypt)



    decrypt_drum1 = DecryptNextDrum(drum1)
    decrypt_drum2 = DecryptNextDrum(drum2)
    decrypt_drum3 = DecryptNextDrum(drum3)
    decrypt_first = DecryptSet(key_dec[:], text_encrypt[:], drum1)

    dec = [True]
    while True:
        pass
        dec = decrypt_first.set_dec_chain(dec)
        dec = decrypt_drum3.decrypt(dec)
        dec = decrypt_drum2.decrypt(dec)
        dec = decrypt_drum1.decrypt(dec)
        print(dec)
        if dec[-1] == False:
            break
    text_decrypt = decrypt_first.get_decrypt_list()
    print(text_decrypt)
    
    




    
    
#
# drums_bit = 8
# debug = True # todo przenieś to głównego ???
# random_drums = True
# random_text_before = True
# dir_name = ""
#
# size_drums = 2 ** drums_bit
#
# # drums generate and save
# create_and_save_dicts(create_drums(size_drums, random_drums), ("../drums/drum2b_"))
#
# # drums load
# drum2b_1, drum2b_2, drum2b_3, drum2b_4, drum2b_5, drum2b_6, drum2b_7, \
# drum2b_8, drum2b_9, drum2b_10 = load_drums("../drums/drum2b_")
#
# # drums check
# check_rand_dicts(load_drums("../drums/drum2b_"), debug) #todo FORMATOWANIE PASS!!!
#
# # (Char_max, ran, size_double, drum_for_gen, char, size)
# # todo napisz to po angielsku
# # text_before = gen_text(False, False, False, drum2b_1)
#
# # text_before = "dupa jaś"
# # from Enigma_all.Enigma_4.modules.__tools_single import __save_drum, __load_drum
# #
# # __save_drum(text_before)
#
#
# #
# #
# # y = load_10_dicts("../drums/drum2b_")
# # print(y)
# # drum2b_1, drum2b_2, drum2b_3, drum2b_4, drum2b_5, drum2b_6, drum2b_7, \
# # drum2b_8, drum2b_9, drum2b_10 = y
#
# # print("-------")
# # print(drum2b_1)
# # print("--------------------------------------------------------------------")
# # print("Text before: \t", str(text_before[0:11]).replace("]", ", + ... ]\t"),
# #       format(decimal.Decimal(len(text_before)), '.2E')) if len(str(text_before)) >= 11 else \
# #     print("Text before: \t", text_encrypt)
# # print("Text encrypt:\t", str(text_encrypt[0:15]).replace("]", ","), "...]")
# # print("Text decrypt:\t", str(text_decrypt[0:15]).replace("]", ","), "...]")
# # print("--------------------------------------------------------------------")
#
#
#
#
#
#
# # def test_10d_2b_1d_1c_tk_rand
# # def test_10d_2b_1d_1c_tk_min
# # def test_10d_2b_1d_1c_tk_max
#
#
#
#
# # def test_10d_4b_4d_300c_tk_():
#
#
# # drum2b_1, drum2b_2, drum2b_3, drum2b_4, drum2b_5, drum2b_6, drum2b_7,\
# # drum2b_8, drum2b_9, drum2b_10 = create_10_dicts(size_drums, True)
