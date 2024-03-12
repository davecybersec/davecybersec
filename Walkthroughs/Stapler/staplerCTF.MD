<b>This is a walkthrough of Stapler, an intentionally vulnerable machine from Vulnhub</b>

A standard port scan shows several open ports on this machine:
21/tcp    open  ftp         vsftpd 2.0.8 or later
22/tcp    open  ssh         OpenSSH 7.2p2 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
53/tcp    open  domain      dnsmasq 2.75
80/tcp    open  http        PHP cli server 5.5 or later
139/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
666/tcp   open  doom?
3306/tcp  open  mysql       MySQL 5.7.12-0ubuntu1
12380/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))

There's a lot to dig into here, but let's grab the low hanging fruit first.

Anonymous FTP is my first choice. Can you log in anonymously? If so, what will we find stored on this server.
Let's see.

