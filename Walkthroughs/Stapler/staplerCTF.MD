<b>This is a walkthrough of Stapler, an intentionally vulnerable machine from Vulnhub</b>

A standard port scan shows several open ports on this machine:
![Open Ports](images/ports.png)

There's a lot to dig into here, but let's grab the low hanging fruit first.

Anonymous FTP is my first choice. Can you log in anonymously? If so, what will we find stored on this server.
Let's see.

![Anymous FTP Connection](images/AnonymousFTP.png)

I found a note file on the server, which provides me with a couple of usernames (Elly and John).

The next thing I'll do is take a look at the web site. I get an error that the resource was not found. So, I'll run gobuster against this site and see if I discover any interesting files / folders.
Interestingly enough, I see 2 hidden files that typically reside in a Linux user's home folder.
![Anymous FTP Connection](images/gobuster.png)

