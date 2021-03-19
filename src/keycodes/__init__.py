
from keys import keys_to_byte


def str_to_byte_chr(input: list):
    ret_list = []
    for item in input:
        if len(item)>1:
            pass
        else:
            if item.islower(): #lower case
                if item.upper() in keys_to_byte:
                    ret_list.append(keys_to_byte[item.upper()])
            elif item.isupper(): #uppercase
                if item in keys_to_byte:
                    shifted = [keys_to_byte["LEFTSHIFT"], keys_to_byte[item]]
                    ret_list.append(shifted)
            else: #symbols
                if item in keys_to_byte:
                    ret_list.append(keys_to_byte[item])
                print(item)
    return ret_list


s = ["H", "e", "l", "l", "o", "1", ",", ".", " "]
for a,b in zip(s, str_to_byte_chr(s)):
    print(a,b)
