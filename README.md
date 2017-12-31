# Spammer
Python script to send mails to a list(.CSV) of Mail IDs having 2 feilds (Data feild(Used as the Subject of the Mail), Mail ID).

# NOTE 
# You need to enable Access for less secure apps for the Gmail account from which you intend to send mail.
**This can be done by going [here](https://myaccount.google.com/lesssecureapps?pli=1) after signing in to your account.**

# Usage
`mySpammer('YOUR MAIL ID', 'MAIL CONTENT', 'YOUR USER NAME', 'YOUR PASSWORD')`  -   Line 23 of spammer.py

> - YOUR MAIL ID - Mail ID from which mail needs to be send.
> - MAIL CONTENT - Content of the mail; can be given as plai text. Header(Subject) is taken as the value of first feild in the .CSV file(here company name).
> - YOUR USER NAME - User name of the Mail ID from which mail needs to be send.
> - YOUR PASSWORD - Password of the Mail ID from which mail needs to be send.

**Run `python spammer.py`**
