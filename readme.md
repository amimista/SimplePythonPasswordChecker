# Password Checker

# Block 2 Project [CS3090]

This tool for educational and explorational purposes only. None of the code written
for this tool was produced in malicious intent.

### Description

This project was a personal exploration project that I wanted to undertake
that showcases my skills with learning a new programming language and also
fulfilling assignment requirements.

The implementation goes as follows: you run this python script inside your
terminal of choice and the program will do the rest. It uses simple for-each loops
to check a password input by the user with the top 10,200 most common passwords
seen. This list was taken from [NordPass](https://nordpass.com/most-common-passwords-list/), a popular internet security company, and
[SecLists](https://github.com/danielmiessler/SecLists), a popular security toolkit repo on [GitHub](https://github.com).

After checking your password, it will give you some things to watch out for if you
have anything it can recommend.

After _that_ it will ask you if you want to go through creating a new password by asking a few questions. It will give you a few guidlines to follow even after
you're done using this tool.

### Q&A

1. **Does this tool store any passwords input into the script?** <br />
   A: Absolutely not. It would be a massive security and privacy concern if it did.
   The password that you input into this script only used to check against other common passwords and then is completely scrapped.

2. **How did you come up with the password creation scheme in this script?** <br />
   A: It's just some scheme that I came up with in my years of creating pointless
   accounts for pointless reasons. A name of something that's important to me, a
   couple random numbers and a special character (or a few depending on the length requirements)

### Ethical Concerns

The only ethical concern that I can see in a program like this is that it's terminal
based and some terminal environments keep a record of what is done within the terminal,
both input and output. But considering my skill level with this programming language,
I don't have the knowlege of making a user interface. So to the terminal it shall be!

Why might this be an issue? Well if someone has access to your terminal records, they could
potentially have access to the old and new passwords that you generate along the way. Obviously
no bueno.

### Requirements

Have python installed on your system, and added to the PATH environment.
Don't know how to do that? [Follow this guide](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/)

1. Clone the repository into a folder of your choosing

```bash
$ git clone https://github.com/amimista/SimplePythonPasswordChecker.git
```

2. Run the Python file

```bash
$ python main.py
```

3. Enjoy!
