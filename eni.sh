#!/bin/bash
export PATH=$PATH:~/workspace/Simnigma

for _ in {1..100..1}
do
    echo -n "a" >> test_100.txt
done
echo "" >> test_100.txt
echo "--- Bash ---> Generate and save test_100.txt"

for _ in {1..1000..1}
do
    echo -n "a" >> test_1k.txt
done
echo "" >> test_1k.txt
echo "--- Bash ---> Generate and save test_1k.txt"

for _ in {1..10000..1}
do
    echo -n "a" >> test_10k.txt
done
echo "" >> test_10k.txt
echo "--- Bash ---> Generate and save test_10k.txt"

for _ in {1..100000..1}
do
    echo -n "a" >> test_100k.txt
done
echo "" >> test_100k.txt
echo "--- Bash ---> Generate and save test_100k.txt"

for _ in {1..1000000..1}
do
    echo -n "a" >> test_1M.txt
done
echo "" >> test_1M.txt
echo "--- Bash ---> Generate and save test_1M.txt"


simnigma.py -c test_10k.txt
simnigma.py -d test_10k.txt.enc
diff -sq test_10k.txt test_10k.txt.enc.dec


rm *test_*
#rm *enc*




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
