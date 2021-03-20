Setup:

- Create a .email directory in your home folder:

```
~/.email
```

- Create a file named email.conf in the .email folder: 

```
~/.email/email.conf
```

- Add the following information to email.conf:

```
email=user@domain.com
password=your_password
smtpSSL=smtp.your_domain.com:465
```

---

Usage:

```sh
python email_message.py <recipient> <subject> <path-to-message>
```

Example:

```sh
python email_message.py user@example.com "A Subject" path/to/message.txt
```
