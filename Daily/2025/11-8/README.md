## today we doing the Transformation
### The question is form picoCtf

![pico](pic/picoStart.png)
<br>

first I saw the menu have the code and a file<br>

![enc](pic/encShow.png)
<br>
when I downloads the enc file, I open it and saw some random text.So I was think this is a ciphertext<br>
but let's figit out what means the code<br> 

![organ](pic/organ.png)
<br>
It's have two part for bulid the ciphertext and the **for** I think It's use for the make hold flag.<br>
before that I go to learn some things.<br>

![unicode](pic/Knowchr.png)
![google](pic/char.png)
![ord](pic/ord.png)
![forex](pic/for.png)
<br>

This is made of canva I use this to think about how to write the code<br>
![canva](pic/canva.png)
<br>

![flag](pic/getFlag.png)
<br>

about the code
i make encode string for save the cipher.<br>

first we get the unicode<br>
and reverse function is use for solve the "chrs"<br>
char one is hight byte so we need to move to 8<br>
and chr two is the low byte I search about it and found the answer that is add *& 0xFF*<br>
<br>
after that i make the for loop to bulid full sentence.<br>
print out the flag

