## WELCOME

#### Welcome (10 pts)

  1. ?flag in the discord server, carlbot would DM you the flag

  FLAG: CYCTF{W3lc0m3_t0_Cyb3rY0ddh@_CTF_2020!}

## SHEBANG

#### Shebang0 (125 pts)

  1. "ssh shebang0@cyberyoddha.baycyber.net -p 1337" with password shebang0
  2. ls reveals nothing, ls -a shows .flag.txt
  3. Use cat to see flag

  FLAG: CYCTF{w3ll_1_gu3$$_b@sh_1s_e@zy}

#### Shebang1 (125 pts)

  1. "ssh shebang1@cyberyoddha.baycyber.net -p 1337" with password [previous flag]
  2.  ls reveals flag.txt, but cat flag.txt rick rolls you...
  3. "cat flag.txt | grep {" gives you the flag

  FLAG: CYCTF{w3ll_1_gu3$$_y0u_kn0w_h0w_t0_gr3p}

#### Shebang2 (150pts)

  1. "ssh shebang2@cyberyoddha.baycyber.net -p 1337" with password [previous flag]
  2. ls reveals a ton of files...
  3. "grep -r {" gets flag (grep with -r does a recursive search of all files in directory)

  FLAG: CYCTF{W0w_th@t$_@_l0t_0f_f1l3s}

#### Shebang3 (150 pts)

  1. "ssh shebang3@cyberyoddha.baycyber.net -p 1337" with password [previous flag]
  2. ls and cat reveals 2 large similar files...
  3. "diff -u file.txt file2.txt | grep -E "^\\+" | sed '2,21!d' | tr -d + | tr -d '\n'"
    1. diff gets difference of files
    2. grep gets all parts of output that is relevant
    3. sed gets the first 20 lines of output
    4. tr gets rid of + sign and the new lines

  4. THAT GOT THE FLAG :)

  FLAG: CYCTF{SPOT_TH3_D1FF}

#### Shebang4 (200 pts)

  1. Usual ssh reveals that it is a png...
  2. "scp -P 1337 shebang4@cyberyoddha.baycyber.net:flag.png ./" allows you to copy file over ssh
  3. "xdg-open flag.png" opens image to reveal FLAG

  FLAG: CYCTF{W3ll_1_gu3$$_th@t_w@s_actually_easy}

## TRIVIA

#### Trivia 1 (100 pts)

  1. Who made linux?

  FLAG: Linus Torvalds

#### Trivia 2 (150 pts)

  1. Who’s operating system was IBM going to buy before MS-DOS?

  FLAG: Gary Kildall

#### Trivia 3 (100 pts)

  1. Which company invented the original hadoop software?

  FLAG: Yahoo

#### Tirvia 4 (50 pts)

  1. Microsoft has been threatened by a secret hacker for the last couple of years. This hacker has been infiltrating their network and exposing secret information about them to the world. Microsoft is determined to catch this hacker. They set up a computer with vulnerabilities and attempt to lure this hacker into trying to hack this computer in order to reveal his origins. What is this type of system called?

  FLAG: honeypot

#### Tirvia 5 (50 pts)

  1. What is a social engineering attack in which someone watches someone else enter private information such as a password called?

  FLAG: Shoulder surfing

#### Trivia 6 (100 pts)

  1. A Hacker infiltrated one of Microsoft's servers and set up malware inside. The malware laid dormant for months, being unnoticed by the server admins. On Thanksgiving Day, the malware was activated, and it crashed all of the servers and the entire network. What is this type of malware called?

  FLAG: Logic bomb

#### Trivia 7 (50 pts)

  1. What built-in Windows tool can you use to repair corrupted files?

  FLAG: sfc

#### Trivia 8 (50 pts)

  1. What programming language has this logo

  FLAG: HASKELL

## WEB

#### Look Closely (50 pts)

  1. Go to [this page](https://inspect.cyberyoddha.team/)
  2. Inspect and the flag is in the comment

  FLAG:  CYCTF{1nSp3t_eL3M3nt?}

#### Disallow (100 pts)

  1. Go to [given page](https://crawlies.cyberyoddha.team) and the /robots.txt
  2. The given page there (/n0r0b0tsh3r3/flag.html) has the FLAG
  3. Clicking on flag rick rolls you

  FLAG: CYCTF{d33r0b0t$_r_sUp3r10r}

#### Data Store (175 pts)

  1. Go to [give page](https://cyberyoddha.baycyber.net:33002/)
  2. Use "' or 1=1--" for username and anything for password to get logged in

  FLAG: CYCTF{1_l0v3_$q1i}

#### Data Store 2 (225 pts)

  1. Go to [given page](https://cyberyoddha.baycyber.net:33003)
  2. Use "admin" as username, "'or 1=1--" for password to login

  CYCTF{S@n1t1ze_@11_U$3R_1npu7$}

## CRYPTO

#### Beware the Idles of March (50 pts)

  1. Rot 19 the text: JFJAM{j@3$@y_j!wo3y}

  FLAG: CYCTF{c@3$@r_c!ph3r}

#### Home Base (125 pts)

  1. Run the given string through [hex > base 32 > base 64 > base 85](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')From_Base32('A-Z2-7%3D',true)From_Base64('A-Za-z0-9%2B/%3D',true)From_Base85('!-u')&input=NGE1YTU3NDc0OTM0MzI1YTQ3NDY0YjU0NDc1NjMyNDY0ZjQyNTk0NzQzMzY1MzRhNGY1NjQ2NDc1OTU2NTM1NzRhMzU0MzQ1NTMzNDU0NDM0YjUyNTg1MzM2NTY0YTUyNGY0MjU1NTY0MzU1MzM1NTRlNDI1MTU3NGY1MDRhMzU)

  FLAG: CYCTF{it5_@_H0m3_2un!}

#### Sus (200 pts)

  1. Go to [this site](https://www.dcode.fr/vigenere-cipher)
  2. Key is SALAD but you can just do auto decryption to get "wouldyoulikesomevinegarwiththat"

  FLAG: CYCTF{wouldyoulikesomevinegarwiththat}

## MISC

#### Lorem Ipsum (125 pts)

  1. Use the LoremSolve.py that compares the given text to the real Lorem ipsum
  2. Returns cyctflatiniscool, add curly brackets

  FLAG: cyctf{latiniscool}

## Forensics

#### Image Viewer (125 pts)

  1. Use [Metadata2go](https://www.metadata2go.com) and view metadata
  2. Flag should be the lens serial number

  FLAG: CYCTF{h3h3h3_1m@g3_M3t@d@t@_v13w3r_ICU}

#### The row beneath (150 pts)

  1. "strings plan.png | grep CYC" should give the flag

  FLAG: CYCTF{L00k_1n_th3_h3x_13h54d56}

#### What's the password? (175 pts)

  1. Use steghide with options --extract -p sudo -sf sudo.jpg to get FLAG

  FLAG: CYCTF{U$3_sud0_t0_achi3v3_y0ur_dr3@m$!}

#### Flag delivery (225 pts)

  1. Replace characters with .  and - since it is morse code, use some decoder online to get FLAG

  FLAG: CYCTFR3@D_B3TW33N_TH3_L1N3S

#### Steg 2 (300 pts)

  1. Use [this site](https://incoherency.co.uk/image-steganography/#unhide) with given image, bits set to 2

  FLAG: CYCTF{l$b_st3g@n0gr@phy_f0r_th3_w1n}

## REV

#### Password 1 (125 pts)

  1. Run p1_solve.py

  FLAG: CYCTF{pu771ng_th3_ch@r@ct3r$_t0g3th3r_1337}

#### Password 2 (175 pts)

  1. Run p2_solve.py

  FLAG: CYCTF{ju$t_@_l177l3_scr@mAl3_f0r_y0u_t0_d3c0d3}

#### Password 3 (225 pts)

  1. Run p3_solve.py

  FLAG: CYCTF{B0th_x0r_@nd_b@s3_64?_th@ts_g0dly}

## PASSWORD CRACKING

#### secure (I think?) (150 pts)

  PRESTEP: I used cyberchef hash analysis tool to find out it is MD5, also, you can just google the hash to find the unhashed version...
  1. [This link](https://md5.gromweb.com/?md5=b0439fae31f8cbba6294af86234d5a28) reverses the MD5 hash

  FLAG: securepassword

#### Crack the Zip! (200 pts)

  1. Install fcrackzip with "sudo apt-get install fcrackzip"
  2. Run "fcrackzip -D -p /usr/share/wordlists/rockyou.txt -u flag.zip" to find password for Zip
  3. Cat the txt in the Zip

  FLAG: cyctf{y0u_cr@ck3d_th3_z!p...}

#### supa secure (225 pts)

  1. "hashcat -m 20 -a 0 -o cracked.txt crackme.txt /usr/share/wordlists/rockyou.txt --force" with [given hash]:[given salt (cyctf)] in the crackme.txt gets the FLAG

  FLAG: cyctf{ilovesalt}

#### Me, Myself, and I (225 pts)

  1. Use [crackstation](https://crackstation.net/) on the given hash

  FLAG: CYCTF{whoami}
