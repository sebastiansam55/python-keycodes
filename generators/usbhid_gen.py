import re

pat = r'define KEY_(.*?)\w*(0x.*?) '

with open('usbhidkeybd.h', 'r') as f:
    for line in f:
        matches = re.findall(pat, line)
        # print(matches)
        if matches:
            print("\t\""+matches[0][0].strip()+"\"", ":", matches[0][1].strip()+",")