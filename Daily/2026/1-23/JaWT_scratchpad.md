## JaWT_scratchpad -- form Pico

![[CTF-challenges_write-up/Daily/2026/1-23/pic/qz.png]]
## Problem Summary

This question is about the JWT, The JWT stands for **JSON Web Token**. It looks like that:
```JWT
{
 "sub": "1234567890",
 "name": "John Doe",
 "admin": true
}
```
we need the Burpsuite to get the JWT. and payload to web while login to the important account.
## Key Observation
When I try to login to the admin, But we failed, therefore something important in here (flag) 

![[youcanadmin.png]]

## Exploitation Strategy
1.After the Failed to the input I try to use burpsuite to see what happen but ...

![[getad.png]]

It seems it doesn't work either.

So I try use other name to see what happen:

![[jwt1.png]]

I see the cookie, and  I think this is the JWT but encode by base 64, and now we founded the one of key.

2.![[CTF-challenges_write-up/Daily/2026/1-23/pic/base64.png]]

I use the decoder and I Get the Jwt.
And we saw the part of the jwt is  garbled text. In the text It's give a tips, The garbled text is SHA256. we need the john which is the tool under the web(link) https://github.com/magnumripper/JohnTheRipper

and the password.txt. The **rockyou.txt**

3.we copy the the Hash 
**pubjNE8IsfbtqahpSB3e98JyRJkEoBg3ctI4aTFHKCo**

```bash
john --format=HMAC-SHA256 /home/seia/jwt.txt --wordlist=/home/seia/rockyou.txt
```

use the 
```bash
john --show jwt.txt
```
we got the key word **ilovepico**

4.we almost go to the webside **https://www.jwt.io/**
![[jwtcode.png]]

input the key word and the account we want to login. we got a long **jwt**

![[last.png]]

![[CTF-challenges_write-up/Daily/2026/1-23/pic/flag.png]]

Let's gooooo!
## Root Cause

The problem of the webside is they over Trust. We need **Zero Trust** any input text! 

```js
function verifyToken(token) {
  
  const decoded = jwt.verify(token, PUBLIC_KEY, {
    algorithms: undefined 
  });

  
  if (decoded.role === 'admin') {
    allowAdminAccess();
  } else {
    denyAccess();
  }
}

```

I think the webside's code like this.
## Generalization

I would argue that the JWT can be use on the program was 'over Trust'.
if we want to know Is it JWT, we can check the cookie and try to in injection.

## Reflection
What I learned in this problem, the most important is the **john** . Due to John is nice password cracker tool. another one is the note of the JWT.

## Some 'Chat'
Today I go throw all the WP, I saw a lot problem, like less details. It's so suck. So I bulid a new Structure that look better more details. I hope I can keep going!