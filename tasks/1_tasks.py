import string

def is_pangram(s):
    alphabet = list(string.ascii_lowercase)
    new_lst = [alphabet.remove(i.lower()) for i in s if str(i).lower() in alphabet]
    return True if len(new_lst) == 26 else False


# def is_pangram(s):
    # alphabet = list(string.ascii_lowercase)
    # for i in s:
    #     if str(i).lower() in alphabet:
    #         alphabet.remove(i.lower())
    # print(alphabet)
    # if len(alphabet) != 0:
    #     return False
    # else: 
    #     return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))