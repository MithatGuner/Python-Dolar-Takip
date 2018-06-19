#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
import urllib2
from time import sleep
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def yenile_al():
	cls()
	while(1):
		sleep(1)
		cls()
		istek = urllib2.Request('https://canlidoviz.com/')
		donus = urllib2.urlopen(istek)
		data = BeautifulSoup(donus, 'html.parser')
		usdalis = data.find_all('span',attrs={'id':'USD_renk'})
		usdsatis = data.find_all('span',attrs={'id':'USD_renk2'})
		print("| ALIS : %s | SATIS : %s |") % (usdalis[0].text, usdsatis[0].text)
		

def yenileme_al():
	cls()
	while(1):
		istek = urllib2.Request('https://canlidoviz.com/')
		donus = urllib2.urlopen(istek)
		data = BeautifulSoup(donus, 'html.parser')
		usdalis = data.find_all('span',attrs={'id':'USD_renk'})
		usdsatis = data.find_all('span',attrs={'id':'USD_renk2'})
		print("| ALIS : %s | SATIS : %s |") % (usdalis[0].text, usdsatis[0].text)
		sleep(1)
		

cls()
print("USD Takip Programına Hoş Geldiniz")
try:
	secenek = input("1 - Yenilemede Ekran Temizlensin\n2 - Yenilemede Ekran Temizlenmesin\nLütfen Seçim Yapın : ")

	if secenek == 1:
		yenile_al()
	else:
		yenileme_al()
except:
	print("\nHata : Lutfen Gecersiz Deger Girmeyin!")



