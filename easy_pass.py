import hashlib

class Password():
    def __init__(self, password, salt = "", iters = 1):

        self.itersleft = iters
        self.iters2 = iters
        
        self.password = salt + password

        self.hash = hashlib.sha256(self.password.encode())
        self.itersleft = self.itersleft - 1
        
        
        while self.itersleft != 0:
            self.hash = self.hash.hexdigest()
            self.hash = hashlib.sha256(self.hash.encode())
            self.itersleft = self.itersleft - 1

        self.password = None

        del self.password

        self.hash = self.hash.hexdigest()

        

def validate(hash1, password, salt = "", iters2 = 1):

    password = salt + password
    
    hash2 = hash1

    var1 = hashlib.sha256(password.encode())
    iters2 = iters2 - 1
  
    while iters2 != 0:
        var1 = var1.hexdigest()
        var1 = hashlib.sha256(var1.encode())
        iters2 = iters2 - 1
    
    var1 = var1.hexdigest()
    if var1 == hash1:
        return True
    else:
        return False 
