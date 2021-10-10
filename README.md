# Easy_pass

This library I made is for managing hashes and passwords. Its very easy to use and implements the SHA-256 algorithm.
I also made a blog post about this : https://sahalcode.wordpress.com/2021/02/01/easy_pass-for-easy-storage-of-passwords/

# Usage
```
passobject = easy_pass.Password(password="password",
                                       iters=500000)

validation = easy_pass.validate(hash1 = contents2,
                                   password = input1,
                                   iters2 = 500000)
```                                                                 
