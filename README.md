# CMPT 470 Project Group 12 CS Teclog

## Features
- User is able to sign up for an account and login. Able to reset password.
- Functions that do not require login
    - View homepage and posts, contact us page.
    - Search for posted articles, leave comments, read tech news posted by the web crawler.
- Functions that require login
    - Create and manage blog posts.
    - Assign a cateogory to blog posts.
    - Join a chat room.
- Functions that not achieved
    - Multilingual support.


## Installation and deployment
```sh
$ vagrant up
```

http://localhost:8080

http://localhost:8080/admin


## User accounts
User
>Username: test1

>Password: test123456

Admin
>Username: admin

>Password: admin123456

## References
The following files use the base chat code from the Django Channels tutorial linked below

http://channels.readthedocs.io/en/latest/tutorial/index.html

>/prj/chat/consumers.py (Part 3)

>/prj/chat/templates/chat/index.html (Part 1)

>/prj/chat/templates/chat/room.html (Part 2)