# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:01:32 2022

@author: alfarizqi wira anadyar
"""

#input
print('program perhitungan')
A = int(input('angka pertama (A): '))
B= int(input('angka kedua (B): '))

#processing & output
import math as m
A += B
print()
print('jumlah: ',A)
A -= B
selisih = B-A
kali = A*B
sisa_bagi = A%B
bagi = A/B
log= m.log10(A)
pangkat = A**B
Sisa2 = B%A
print('selisih: ',selisih)
print('perkalian: ',kali)
print('sisa bagi A ke B: ',sisa_bagi)
print('pembagian: ',bagi)
print('logaritma: ', log)
print('pangkat: ',pangkat)
print('sisa bagi B ke A: ', Sisa2)
