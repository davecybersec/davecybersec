This script takes2 text files as input. The first file should contain a hash or list of hashes, the second file can be any wordlist of your choosing. What the script does is iterate through the hashes and discover the hash being used, it then attempts to crack the hashes via the supplied wordlist.

This tool supports the following hash types:
<ul>
<li>MD5</li>
<li>SHA1</li>
<li>SHA224</li>
<li>SHA256</li>
<li>SHA384</li>
<li>SHA512</li>
</ul>

This script requires the hashlib module. You can install it using <b>pip install hashlib</b>
