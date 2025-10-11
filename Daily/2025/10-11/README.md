# Today's topic is about the hash
### this question is from the PicoCTF
[picoCTF:](https://play.picoctf.org/practice)
![image:](Daily\2025\10-11\pic\theQz.png)

---

### Problem-Solving Process

The question start, they give a Hash password:
![image](Daily\2025\10-11\pic\q1-hash.png)

and I realize this is MD5hash(MD5: Output length is 128 bits (32 hexadecimal digits)), so I am just Search on Browser and found the password:

![image](Daily\2025\10-11\pic\q1-hash.png)

second one is the SHA-1(SHA-1: Output length is 160 bits), you don't need to count this, Just feel it :D
**The answer is :**

![image](Daily\2025\10-11\pic\q2-hash.png)

Finally, We see the SHA-256(SHA-256: Output length is 256 bits), At the beginning i feel confused why i can't solve it (on webside) It wasn't until later that I learned SHA‑256 is a one‑way hash, so I looked up a few specialized password‑dictionary sites and was able to find the final answer.

![image](Daily\2025\10-11\pic\solveSha256.png)

![image](Daily\2025\10-11\pic\getFlag.png)

**something want to say:**
for this project i spend a lot time on it, reason why that becuase I spend a lot time on the how to use the git. I feel tired.but it give me lot Experience.
And I will keep doing this project.See you ! :D