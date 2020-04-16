In [9]: def outer(): 
   ...:     def inner(): 
   ...:         print('This is inner') 
   ...:     print('This is outer, returning inner') 
   ...:     return inner 
   ...:                                                                 

In [10]: i = outer()                                                    
This is outer, returning inner

In [11]: i()                                                            
This is inner

In [12]: i()                                                            
This is inner

In [13]:                                                                

In [13]:                                                                
