#!/bin/bash
export PATH=$PATH:~/workspace/Simnigma

#for _ in {1..100..1}
#do
#    echo -n "a" >> test_100.txt
#done
#echo "" >> test_100.txt
#echo "--- Bash ---> Generate and save test_100.txt"
#
#for _ in {1..1000..1}
#do
#    echo -n "a" >> test_1k.txt
#done
#echo "" >> test_1k.txt
#echo "--- Bash ---> Generate and save test_1k.txt"
#
#for _ in {1..10000..1}
#do
#    echo -n "a" >> test_10k.txt
#done
#echo "" >> test_10k.txt
#echo "--- Bash ---> Generate and save test_10k.txt"
#
#for _ in {1..100000..1}
#do
#    echo -n "a" >> test_100k.txt
#done
#echo "" >> test_100k.txt
#echo "--- Bash ---> Generate and save test_100k.txt"
#
#for _ in {1..1000000..1}
#do
#    echo -n "a" >> test_1M.txt
#done
#echo "" >> test_1M.txt
#echo "--- Bash ---> Generate and save test_1M.txt"
#
#for _ in {1..5000000..1}
#do
#echo -n "a" >> test_5M.txt
#done
#echo "" >> test_5M.txt
#echo "--- Bash ---> Generate and save test_5M.txt"


#simnigma.py -K for_test_1024 1024 -v
#simnigma.py -K for_test_2048 2048
#simnigma.py -R for_test_10 10
#simnigma.py -R for_test_100 100
#
#simnigma.py -c test_10k.txt -v
#simnigma.py -d test_10k.txt.enc -v
#diff -sq test_10k.txt test_10k.txt.enc.dec |grep 'różnią się'

simnigma.py -c test_s.txt -s
simnigma.py -d test_s.txt.enc -s





#simnigma.py -c test_1M.txt -k for_test_2048
#simnigma.py -d test_1M.txt.enc -k for_test_2048
#diff -sq test_1M.txt test_1M.txt.enc.dec |grep 'różnią się'
#
#simnigma.py -c test_5M.txt -k for_test_2048 -v
#simnigma.py -d test_5M.txt.enc -k for_test_2048 -v
#diff -sq test_5M.txt test_5M.txt.enc.dec |grep 'różnią się'

#rm keys/for_test_*
#rm rotors/for_test_10*
#rm *test_*
rm *enc*




#simnigma.py -c enigma.py
#simnigma.py -d enigma.py
#diff enigma.py enigma.py.enc.dec -v
#simnigma.py -c enigma.py -k /home/bq666/workspace/test2/nowy_klucz2.key -v
#simnigma.py -c enigma.py -k do_txt.key -v
#simnigma.py -c enigma.py -r set_drum_8b -v
#simnigma.py -c enigma.py -r for_file -v
#simnigma.py -c enigma.py -r ~/workspace/test2/set_drum_8b_3.pkl -v
#
#simnigma.py -d enigma.py.enc -v
#simnigma.py -d enigma.py.enc -k /home/bq666/workspace/test2/nowy_klucz2.key -v


#simnigma.py -K nowy_testuje 1024 -v
#simnigma.py -R nowy_testuje 3 -v

#simnigma.py -c *
#rm *enc*




#-c sadf
#-d asdf
#-c sdaf -k asdf
#-d asdf -k asdf
#-c asdf -k asdf -r sadf
#-d asdf -k asdf -r asdf
#....... -v
#....... -s
#....... -v -s
#
#-K sadf 1234
#-R asdf 12
#-K asdf 1234 -R asdf 12
#....... -v
#
#-h --help
#-V --version
