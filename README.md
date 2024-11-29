# eAsy*_*pa_ss

![This is an image](https://i.imgur.com/rdYvdFP.png)
This library I made is for managing hashes and passwords. It is hopefully easy to use and implements the SHA-256 algorithm.

# Usage
```
import easy_pass

passobject = easy_pass.Password(password="password", # hash the word "password"
                                       iters=500000) # hash it using 5000 iterations

passobject.hash # display the word "password"'s hash

validation = easy_pass.validate(hash1 = passobject.hash, # is passobject.hash the same as the hash as of "password1"
                                   password = "password1",
                                   iters2 = 500000)
```                                                                 
