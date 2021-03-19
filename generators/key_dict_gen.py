import re

pat_hut = r'(Keyboard|Keypad|Reserved) ((.) and (.).*?|.*?)[,|\n]'
pat_input = r'KEY_(.*?)\w*?(\d*)\n'

with open('tabula-hut1_12v2.csv', 'r') as f:
    print("keys = {")
    for line in f:
        items = line.split(",")
        # print(items)
        # plaintext = items[2]
        matches = re.findall(pat_hut, line)
        if matches and len(matches[0])>=3:
            # print(line, matches[0])
            if matches[0][2]!="" and matches[0][3]!="":
                plaintext = matches[0][2]
                shifted = matches[0][3]
                
            else:
                plaintext = matches[0][1]
                shifted = ""
        else:
            plaintext = ""
            shifted = ""
        # print()
        dec = items[0]
        hexdec = items[1]
        if len(items)>=4:
            evdev = items[3].strip()
        else:
            evdev = "-1"
        # print(plaintext, shifted)
        if plaintext == "":
            continue
        else:
            plaintext = plaintext.replace("\\", "\\\\")
        print("""    "<"""+plaintext+""">": {
            "plaintext": \""""+plaintext+"""\",
            "shifted": \""""+shifted+"""\",
            "evdev": -1,
            "decimal": """+dec+""",
            "hex": 0x"""+hexdec+"""
    },
""")
    print("}")