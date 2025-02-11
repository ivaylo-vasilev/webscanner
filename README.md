# WebScanner
Web scanner for existing (and/or hidden) directories.
---

**WebScanner** is a Python program intended to scan and discover existing and/or hidden directories (and web objects) on a web server using a wordlist file to perform a dictionary based enumeration.
Basically I created my own basic version of the popular [***DIRB***](https://dirb.sourceforge.net/) program.
**WebScanner** allows you to select your own (custom) *User-Agent*. Currently the program shows the result of the scanning only in the terminal window, but I am planning to add an option to export the result into a file.

*Example usage:*

`$python3 webscan.py URL -w <wordlist.txt>`

*For all the available options:*

`$python3 webscan.py --help`

---

\**The wordlist files in the **wordlists** directory are from the wordlists included with **Kali Linux**.*
