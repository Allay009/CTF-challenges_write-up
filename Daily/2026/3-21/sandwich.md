# sudo make a sandwich - pico

![](pic/qz.png)
## Problem Summary

This question is using the emacs to get the permissions
![](emac.webp)
<br>
## Key Observation

```bash
sudo -l
```
This command will allow you to see which program have permissions.
## Exploitation Strategy
1.![](pic/tip1.png)
![](pic/tip2.png)
When I see this Hint I guess we need to get the permissions from some program already have root.

2.![](pic/ll.png)
Now I know the emacs have the permissions. Let's open it.

3.![](pic/into.png)
<br>
When I open the emacs I realize I don't know how to open the shell in here. Google is practical.

![](pic/shell.png)
![](pic/flag.png)
Let's gooo
## Reflection
I learned the emacs and know how to open the shell and get the permissions.
