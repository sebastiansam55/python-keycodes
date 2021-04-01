#!/usr/bin/python3
import re

pat_hut = r'(Keyboard|Keypad|Reserved) ((.) and (.).*?|.*?)[,|\n]'
pat_input = r'KEY_(.*?)\w*?(\d*)\n'

with open('tabula-hut1_12v2.csv', 'r') as f:
    print("#!/usr/bin/python3")
    print("keys = {")
    f.readline() #get rid of header
    # header:
    # decimal, hexadecimal, plaintext, evdev, javascript
    for count, line in enumerate(f):
        items = line.split(",")
        # print(items)
        # plaintext = items[2]
        try:
            javascript = items[4].strip()
            if javascript=="":
                javascript = "-1"
        except:
            javascript = "-1"
        matches = re.findall(pat_hut, line)
        if matches and len(matches[0])>=3:
            # print(line, matches[0])
            if matches[0][2]!="" and matches[0][3]!="":
                plaintext = matches[0][2].strip()
                shifted = matches[0][3].strip()
            else:
                plaintext = matches[0][1].strip()
                shifted = ""
            plain = plaintext
            if matches[0][0] == "Keypad":
                plaintext = "KP"+plaintext
        else:
            plaintext = ""
            shifted = ""
        # print()
        dec = items[0].strip()
        hexdec = items[1].strip()
        if len(items)>=4:
            if plaintext.isalpha() and len(plaintext) == 1:
                # evdev = str(int(items[3].strip())-1)
                evdev = items[3].strip()
            elif plaintext.isnumeric() and len(plaintext) == 1:
                evdev = items[3].strip()
            else:
                evdev = items[3].strip()
                minimap = {
                    ",": 51,
                    "Power": 116,
                    "KP=": 117,
                }
                if plaintext in minimap:
                    evdev = str(minimap[plaintext])
                else:
                    try:
                        evdev = items[3].strip()
                    except:
                        evdev = "-2"
                    if evdev == "":
                        evdev = "-3"
        else:
            evdev = "-1"
        # print(plaintext, shifted)
        plaintext_map = {
            "comma and <": ",",
            "Spacebar": " ",
        }
        if plaintext == "":
            continue
        elif plaintext == "comma and <":
            plaintext = ","
            plain = ","
        elif plaintext == "Spacebar":
            plaintext = " "
            plain = " "
        elif plaintext == "'":
            shifted = "\\\""
        else:
            plaintext = plaintext.replace("\\", "\\\\")
            plain = plain.replace("\\", "\\\\")
        print("""    \""""+plaintext+"""\": {
            "plaintext": \""""+plain+"""\", "shifted": \""""+shifted+"""\",
            "evdev": """+evdev+""", "decimal": """+dec+""", "hex": 0x"""+hexdec+""",
            "javascript": """+javascript+"""},""")
        if count==84:
            # break
            pass
    print("}")


print("keys['<'] = keys[',']")
print("keys['>'] = keys['.']")
print("keys['\"'] = keys['\\\'']")
print("keys[':'] = keys[';']")
print("keys['!'] = keys['1']")
print("keys['@'] = keys['2']")
print("keys['#'] = keys['3']")
print("keys['$'] = keys['4']")
print("keys['%'] = keys['5']")
print("keys['^'] = keys['6']")
print("keys['&'] = keys['7']")
print("keys['*'] = keys['8']")
print("keys['('] = keys['9']")
print("keys[')'] = keys['0']")
print("keys['{'] = keys['[']")
print("keys['}'] = keys[']']")
print("keys['?'] = keys['/']")
print("keys['~'] = keys['`']")
print("keys['_'] = keys['-']")
print("keys['+'] = keys['=']")
print("keys['|'] = keys['\\\\']")
print("\n")
