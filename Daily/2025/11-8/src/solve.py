encode = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'

def reverse(All_chars):
    chars_Value = ord(All_chars)

    char_one = chr(chars_Value >> 8)
    char_two = chr(chars_Value & 0xFF)
    
    return char_one, char_two

flag = ''

for All_chars in encode:
    char_one, char_two = reverse(All_chars)
    flag = flag + char_one + char_two

print(flag)