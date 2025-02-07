from collections import defaultdict
'''
I want to break a cipher text. 
I use python library. 
We will follow Kerchof's law. 
Here are the details - 
First is, it is encrypted in Affine Cipher. 
M = CT = Z26, 
K = Zx26(whose mod. multipplicative inverse exist) * Z26. 
	a       *      b

Gen () a belowngs to Zx26(whose multipplicative inverse exist) . 
'
Only once key got generated : k = (a, b)
Enc(k, m) -> ct = a*m + b mod 26
Dec(k, ct) -> a^(-1) * (ct - b) mod 26

only capital letters : both M and cipherText

Techniques -
# brute force
# frequency analysis

'''
ct = "FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH"
#            ``        ---        ---           ``         ~~
#                        ---        ---						---
#					 DKR                          RKD

# XYX 		: RXR, RSR, RXRSR, 
# XX  		: ~~
# XY and XY : ``
# XYZ n ZYX : (DKR, RKD)m ORU, PRK, LRH, HRH
# Bigrams
# FM, FE, EF, UFE, 
# AP, AP
# ER, KR, XR, SR, OR, PR, LR, HR => R might be a vowel.
# ED, ND, 

# Note : VE and EV, DK and KD
														     
def dec(ct):
	# all a^-1 (ct - all b) mod 26 
	for a in [1,3,5,7,9,11,15,17,19,21,23,25]:
		for b in range(1, 27):
			res = ""
			for letter in ct:
				cur = (pow(a, -1, 26) * (ord(letter) - 65 - b) % 26)% 26
				res += chr(cur+65)
			# print(res)
			# print("\n")
	return

def dec(ct, a, b):
	res = ""
	for letter in ct:
		cur = (pow(a, -1, 26) * (ord(letter) - 65 - b) % 26)% 26
		res += chr(cur+65)
	print(res)
	return

def findKeyAffine(ct, ct_letter, pt_letter):
	for a in [1,3,5,7,9,11,15,17,19,21,23,25]:
		for b in range(1, 27):
			cur = (pow(a, -1, 26) * (ord(ct_letter) - 65 - b) % 26)% 26
			if chr(cur+65) == pt_letter:
				dec(ct, a, b)
				


freq = defaultdict(int)
for i in ct:
	freq[i] += 1
# print(freq)

for ct_letter, val in freq.items():
	if val >= 5: 
		for pt_letter in ['A', 'E', 'I', 'O', 'U']:
			findKeyAffine(ct, ct_letter, pt_letter)


























