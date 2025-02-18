# substitution cipher
from collections import defaultdict
ct = "VFCNCJWOTNCVSBZCJAWMZSJOWTKJAWSBGYQUZAARJGKAFCBCJAWZAJNWHZBVCZGJVOKZTGZPWOBUZEWRKJUWKWRZAOGUVVPJOQJBVFCWTAVSWSVCWRJOWZOTKWAWGGUWTDZEPJOKJAEKZJCNZEWGJUGWTFBGVRZCTAGKWAFO"

'''
VFCNCJWOTNCVSBZCJAWMZSJOWTKJAWSBGYQUZAARJGKAFCBCJAWZAJNWHZBVCZGJVOKZTGZPWOBUZEWRKJUWKWRZAOGUVVPJOQJB
  ---     --   --    --   --         
    --         --    --   --           --      --   --        --                --            -- --   
     
VFCWTAVSWSVCWRJOWZOTKWAWGGUWTDZEPJOKJAEKZJCNZEWGJUGWTFBGVRZCTAGKWAFO
   -   ```  ``
             --                 -- --   --     --                                      
   VFC - twice
   WT - 
   AA - ZAAR
   VV -  UVV
   GG - WGG, GGU 
   WOT -
   ZOT -
   CJ, CJ, SJ, KJ, RJ, CJ, AJ, GJ, KJ, KJ, PJ, QJ, RJ, PJ, KJ, ZJ, GJ -
   WAW, WAF
   

   ZS - 3 times                      
---
'''
decodedTexts = []
def dec_subs(ct, k):
    resA = ""
    resB = ""
    for i in ct:
        resA += chr(ord(i) + k)
        resB += chr(ord(i) - k)
    print("A :::: " , resA)
    print("B", resB)
    decodedTexts += [resA, resB]
    return decodedTexts


freq = defaultdict(int)
for i in ct:
    freq[i] += 1
print(freq)

'''
{'V': 10, 'F': 5, 'C': 11, 'N': 4, 
'J': 16, 'W': 20, 'O': 10, 'T': 8, 
'S': 5, 'B': 7, 'Z': 15, 'A': 13, 
'M': 1, 'K': 9, 'G': 11, 'Y': 1, 
'Q': 2, 'U': 6, 'R': 5, 'H': 1, 
'P': 3, 'E': 4, 'D': 1})

W, Z -> E or A

J is T

'''

# for k, val in freq.items():
#     if val >= 10:
#         for cur in ['A', 'E', 'I', 'O', 'U']:
            
#             dec_subs(ct, abs(ord(cur) - ord(k)))

# with open('decoded.txt', 'w') as f:
#     for line in decodedTexts:
#         f.write(f"{line}\n")

for i in range(len(ct)-2):
    if ct[i] == ct[i+2]:
        print(ct[i:i+3])
        ''' CNC, CBC, WKW, SWS, WAW'''
ctw = ct.replace('W', ' ')
print(ctw)

freq_di = defaultdict(int)
for i in range(len(ct)-1):
    freq_di[ct[i:i+2]] += 1
# print(freq_di)

'''
1. th (92535489, 3.882543%)
2. he (87741289, 3.681391%)
3. in (54433847, 2.283899%)
4. er (51910883, 2.178042%)
5. an (51015163, 2.140460%)
6. re (41694599, 1.749394%)
7. nd (37466077, 1.571977%)
8. on (33802063, 1.418244%)
9. en (32967758, 1.383239%)
10. at (31830493, 1.335523%)
11. ou (30637892, 1.285484%)
12. ed (30406590, 1.275779%)

{'VF': 2, 'FC': 3, 'CN': 2, 'NC': 2, 'CJ': 3, 'JW': 1, 'WO': 2, 'OT': 2, 'TN': 1, 
'CV': 1, 'VS': 2, 'SB': 2, 'BZ': 1, 'ZC': 2, 'JA': 4, 'AW': 4, 'WM': 1, 'MZ': 1, 
'ZS': 1, 'SJ': 1, 'JO': 4, 'OW': 2, 'WT': 4, 'TK': 2, 'KJ': 3, 'WS': 2, 'BG': 2, 
'GY': 1, 'YQ': 1, 'QU': 1, 'UZ': 2, 'ZA': 3, 'AA': 1, 'AR': 1, 'RJ': 2, 'JG': 1, 
'GK': 2, 'KA': 1, 'AF': 2, 'CB': 1, 'BC': 1, 'WZ': 2, 'AJ': 1, 'JN': 1, 'NW': 1, 
'WH': 1, 'HZ': 1, 'ZB': 1, 'BV': 2, 'VC': 2, 'CZ': 1, 'ZG': 1, 'GJ': 2, 'JV': 1, 
'VO': 1, 'OK': 2, 'KZ': 2, 'ZT': 1, 'TG': 1, 'GZ': 1, 'ZP': 1, 'PW': 1, 'OB': 1, 
'BU': 1, 'ZE': 3, 'EW': 2, 'WR': 3, 'RK': 1, 'JU': 2, 'UW': 2, 'WK': 1, 'KW': 3, 
'RZ': 2, 'AO': 1, 'OG': 1, 'GU': 2, 'UV': 1, 'VV': 1, 'VP': 1, 'PJ': 2, 'OQ': 1, 
'QJ': 1, 'JB': 1, 'CW': 2, 'TA': 2, 'AV': 1, 'SW': 1, 'SV': 1, 'ZO': 1, 'WA': 2, 
'WG': 2, 'GG': 1, 'TD': 1, 'DZ': 1, 'EP': 1, 'AE': 1, 'EK': 1, 'ZJ': 1, 'JC': 1, 
'NZ': 1, 'UG': 1, 'GW': 1, 'TF': 1, 'FB': 1, 'GV': 1, 'VR': 1, 'CT': 1, 'AG': 1, 'FO': 1})

JA : 4 times
AW : 4 times
JO : 4
WT : 4
ZE : 3
ZA : 3
AA : 1
WR : 3 times
KW : 3
FC : 3
KJ : 3
CJ : 3

A - AW, JA, ZA, AA, 
W - AW, WT, WR, KW, --- _E, E_ , E_ , _E
J - JA, JO, KJ, CJ --- 
Z - 

K can be H

[[10, 'V'], [11, 'C'], [16, 'J'], [20, 'W'], [10, 'O'], [15, 'Z'], [13, 'A'], [9, 'K'], [11, 'G'],



'''
freq_tri = defaultdict(int)
for i in range(len(ct)-2):
    freq_tri[ct[i:i+3]] += 1
# print(freq_tri)
'''


{'VFC': 2, 'FCN': 1, 'CNC': 1, 'NCJ': 1, 'CJW': 1, 'JWO': 1, 'WOT': 1, 'OTN': 1, 'TNC': 1, 'NCV': 1, 
'CVS': 1, 'VSB': 1, 'SBZ': 1, 'BZC': 1, 'ZCJ': 1, 'CJA': 2, 'JAW': 3, 'AWM': 1, 'WMZ': 1, 'MZS': 1, 
'ZSJ': 1, 'SJO': 1, 'JOW': 2, 'OWT': 1, 'WTK': 1, 'TKJ': 1, 'KJA': 2, 'AWS': 1, 'WSB': 1, 'SBG': 1, 
'BGY': 1, 'GYQ': 1, 'YQU': 1, 'QUZ': 1, 'UZA': 1, 'ZAA': 1, 'AAR': 1, 'ARJ': 1, 'RJG': 1, 'JGK': 1, 
'GKA': 1, 'KAF': 1, 'AFC': 1, 'FCB': 1, 'CBC': 1, 'BCJ': 1, 'AWZ': 1, 'WZA': 1, 'ZAJ': 1, 'AJN': 1, 
'JNW': 1, 'NWH': 1, 'WHZ': 1, 'HZB': 1, 'ZBV': 1, 'BVC': 1, 'VCZ': 1, 'CZG': 1, 'ZGJ': 1, 'GJV': 1, 
'JVO': 1, 'VOK': 1, 'OKZ': 1, 'KZT': 1, 'ZTG': 1, 'TGZ': 1, 'GZP': 1, 'ZPW': 1, 'PWO': 1, 'WOB': 1, 
'OBU': 1, 'BUZ': 1, 'UZE': 1, 'ZEW': 2, 'EWR': 1, 'WRK': 1, 'RKJ': 1, 'KJU': 1, 'JUW': 1, 'UWK': 1, 
'WKW': 1, 'KWR': 1, 'WRZ': 1, 'RZA': 1, 'ZAO': 1, 'AOG': 1, 'OGU': 1, 'GUV': 1, 'UVV': 1, 'VVP': 1,
'VPJ': 1, 'PJO': 2, 'JOQ': 1, 'OQJ': 1, 'QJB': 1, 'JBV': 1, 'BVF': 1, 'FCW': 1, 'CWT': 1, 'WTA': 1, 
'TAV': 1, 'AVS': 1, 'VSW': 1, 'SWS': 1, 'WSV': 1, 'SVC': 1, 'VCW': 1, 'CWR': 1, 'WRJ': 1, 'RJO': 1, 
'OWZ': 1, 'WZO': 1, 'ZOT': 1, 'OTK': 1, 'TKW': 1, 'KWA': 2, 'WAW': 1, 'AWG': 1, 'WGG': 1, 'GGU': 1, 
'GUW': 1, 'UWT': 1, 'WTD': 1, 'TDZ': 1, 'DZE': 1, 'ZEP': 1, 'EPJ': 1, 'JOK': 1, 'OKJ': 1, 'JAE': 1, 
'AEK': 1, 'EKZ': 1, 'KZJ': 1, 'ZJC': 1, 'JCN': 1, 'CNZ': 1, 'NZE': 1, 'EWG': 1, 'WGJ': 1, 'GJU': 1, 
'JUG': 1, 'UGW': 1, 'GWT': 1, 'WTF': 1, 'TFB': 1, 'FBG': 1, 'BGV': 1, 'GVR': 1, 'VRZ': 1, 'RZC': 1, 
'ZCT': 1, 'CTA': 1, 'TAG': 1, 'AGK': 1, 'GKW': 1, 'WAF': 1, 'AFO': 1})

1. the (59623899, 3.508232%)
2. and (27088636, 1.593878%)
3. ing (19494469, 1.147042%)
4. her (13977786, 0.822444%)
5. hat (11059185, 0.650715%)
6. his (10141992, 0.596748%)
7. tha (10088372, 0.593593%)
8. ere (9527535, 0.560594%)    xyx
9. for (9438784, 0.555372%)
10. ent (9020688, 0.530771%)
11. ion (8607405, 0.506454%)
12. ter (7836576, 0.461099%)
13. was (7826182, 0.460487%)
14. you (7430619, 0.437213%)
15. ith (7329285, 0.431250%)
16. ver (7320472, 0.430732%)
17. all (7184955, 0.422758%)   xyy
18. wit (6752112, 0.397290%)
19. thi (6709729, 0.394796%)
20. tio (6425262, 0.378058%)

JAW - 3  t_e
PJO - 2   
JOW - 2  the
KWA - 2  her
CJA - 2
KJA - 2
ZEW - 2
VFC - 2


ZE, ZA , ZEW, ZOT -- cipher
         

WAWGG

JAW - 

JNW - 1



J - first and second in trigram and not with W(which I think is E)  
    - can be T
If VFC is THE

'''

print(ctw)


'''
W is E
J is T


'''
arr = []
for k, v in freq.items():
    if v > 8:
        arr.append([v, k])
        print(k, v)

for k, v in freq_di.items():
    if v > 1:
        arr.append([v, k])
        print(k, v)

for k, v in freq_tri.items():
    if v > 1:
        arr.append([v, k])
        print(k)

print(arr)
'''
[[10, 'V'], [11, 'C'], [16, 'J'], [20, 'W'], [10, 'O'], [15, 'Z'], [13, 'A'], [9, 'K'], [11, 'G'], 


[2, 'VF'], [3, 'FC'], [2, 'CN'], [2, 'NC'], [3, 'CJ'], [2, 'WO'], [2, 'OT'], [2, 'VS'],
[2, 'SB'], [2, 'ZC'], [4, 'JA'], [4, 'AW'], [4, 'JO'], [2, 'OW'], [4, 'WT'], [2, 'TK'], 
[3, 'KJ'], [2, 'WS'], [2, 'BG'], [2, 'UZ'], [3, 'ZA'], [2, 'RJ'], [2, 'GK'], [2, 'AF'], 
[2, 'WZ'], [2, 'BV'], [2, 'VC'], [2, 'GJ'], [2, 'OK'], [2, 'KZ'], [3, 'ZE'], [2, 'EW'], 
[3, 'WR'], [2, 'JU'], [2, 'UW'], [3, 'KW'], [2, 'RZ'], [2, 'GU'], [2, 'PJ'], [2, 'CW'],
 [2, 'TA'], [2, 'WA'], [2, 'WG'],
  
[2, 'VFC'], [2, 'CJA'], [3, 'JAW'], [2, 'JOW'], [2, 'KJA'],
   [2, 'ZEW'], [2, 'PJO'], [2, 'KWA']]


'''
for i in range(len(arr)):
    arr[i][1] = arr[i][1].replace('J', 'T')
    arr[i][1] = arr[i][1].replace('W', 'E')
print(arr)

'''
[[10, 'V'], [11, 'C'], [16, 'T'], [20, 'E'], [10, 'O'], [15, 'Z'], [13, 'A'], [9, 'K'], [11, 'G'],


 [2, 'VF'], [3, 'FC'], [2, 'CN'], [2, 'NC'], [3, 'CT'], [2, 'EO'], [2, 'OT'], [2, 'VS'], [2, 'SB'],
   [2, 'ZC'], [4, 'TA'], [4, 'AE'], [4, 'TO'], [2, 'OE'], [4, 'ET'], [2, 'TK'], [3, 'KT'], [2, 'ES'],
     [2, 'BG'], [2, 'UZ'], [3, 'ZA'], [2, 'RT'], [2, 'GK'], [2, 'AF'], [2, 'EZ'], [2, 'BV'], [2, 'VC'],
       [2, 'GT'], [2, 'OK'], [2, 'KZ'], [3, 'ZE'], [2, 'EE'], [3, 'ER'], [2, 'TU'], [2, 'UE'], [3, 'KE'], 
       [2, 'RZ'], [2, 'GU'], [2, 'PT'], [2, 'CE'], [2, 'TA'], [2, 'EA'], [2, 'EG'], 
       
[2, 'VFC'], [2, 'CTA'], [3, 'TAE'], [2, 'TOE'], [2, 'KTA'], [2, 'ZEE'], [2, 'PTO'], [2, 'KEA']]



Z, U, W - chances are they are vowels...
T - J most probably

'''

