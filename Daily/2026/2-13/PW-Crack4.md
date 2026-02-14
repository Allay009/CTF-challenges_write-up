```python
pos_pw_list = ["158f", "1655", "d21e", "4966", "ed69"...]
```

```python
def level_4_pw_check():
    for pws in pos_pw_list:

        user_pw_hash = hash_pw(pws)
    
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), pws)
            print(decryption)
            print(pws)
```

```python
def level_4_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```