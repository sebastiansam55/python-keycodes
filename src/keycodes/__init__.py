
# from keys import keys_to_byte
from keycodes.keys import keys as k


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

def item_to_evdev(c: str):
    return k[c]['evdev']

def str_to_evdev(s: str):
    ret_list = []
    for i in s:
        ret_list.append(k[i]['evdev'])
    return ret_list

def hotkey_to_evdev(l: list):
    ret_list = []
    mod_list = []
    for i in l[0]:
        mod_list.append(k[i]['evdev'])
    ret_list.append(mod_list)
    for i in l[1:]:
        ret_list.append(k[i]['evdev'])

    return ret_list


def evdev_to_str(i: int):
    pass

def list_to_evdev(l: list):
    """
    This method has to be used if you are sending stuff other than typable characters, like home/end or arrows. Etc.

    @param l: List of single characters to be translated.
    """
    ret_list = []
    for item in l:
        ret_list.append(item_to_evdev(item))
        # print(char_to_evdev(item))
    return ret_list

