# substitution cipher
from collections import defaultdict
ct = "VFCNCJWOTNCVSBZCJAWMZSJOWTKJAWSBGYQUZAARJGKAFCBCJAWZAJNWHZBVCZGJVOKZTGZPWOBUZEWRKJUWKWRZAOGUVVPJOQJBVFCWTAVSWSVCWRJOWZOTKWAWGGUWTDZEPJOKJAEKZJCNZEWGJUGWTFBGVRZCTAGKWAFO"

'''
VFCNCJWOTNCVSBZCJAWMZSJOWTKJAWSBGYQUZAARJGKAFCBCJAWZAJNWHZBVCZGJVOKZTGZPWOBUZEWRKJUWKWRZAOGUVVPJOQJB
  ---     --   --    --   --         
    --         --    --   --           --      --   --        --                --            -- --   

VFCWTAVSWSVCWRJOWZOTKWAWGGUWTDZEPJOKJAEKZJCNZEWGJUGWTFBGVRZCTAGKWAFO
   -   ```  ``                         
---
'''

def dec_subs(ct, k):
    resA = ""
    resB = ""
    for i in ct:
        resA += chr(ord(i) + k)
        resB += chr(ord(i) - k)
    print("A", resA)
    print("B", resB)


freq = defaultdict(int)
for i in ct:
    freq[i] += 1
print(freq)

for k, val in freq.items():
    if val >= 10:
        for cur in ['A', 'E', 'I', 'O', 'U']:
            
            dec_subs(ct, abs(ord(cur) - ord(k)))

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())