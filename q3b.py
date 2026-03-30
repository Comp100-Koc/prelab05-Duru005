def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    if a.startswith("0b"):
        a = a[2:]
    if b.startswith("0b"):
        b = b[2:]
  
    count = 0
    res = ""
    
    while a or b or count:
        if a :
            count += int(a[-1])
            a = a[:-1]
            
        if b : 
            count += int(b[-1])
            b = b[:-1]
            
        res = str(count % 2) + res
        count //= 2
    
    res = res.lstrip("0")
    
    return "0b" + res
        
        