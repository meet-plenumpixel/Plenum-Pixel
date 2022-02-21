# Local -> Enclosing -> Global -> Built-in
# in most of programming language, defined variables are accessable for it's subsidiary scope
# (i.e. variable can be accessable within the block and it's sub blockes)
# similarly variables are inaccessable for it's parent scope


# variable x is in global scope within current module
x = 'global x'

print('after x: x=', x)

def outer_fun():

  print('before y: x=', x)  

  # variable y is local for outdoor_fun, enclosing for inner_fun
  y = 'y outer_fun'

  print('after y: x=', x)  
  print('after y: y=', y)  


  def inner_fun():

    # variable z is local for inner_fun

    print('before z: x=', x)  
    print('before z: y=', y)  

    z = 'z inner_fun'

    # you can't change value of variable from it's parent scope
    
    # if you want to change value of enclosing variable then use can explicitly define variable scope by 'nonlocal' keyword
    # nonlocal y   # uncomment to test it.
    # y = 'change y from inner_fun'

    # if you want to change value of global variable then use can explicitly define variable scope by 'global' keyword
    # global x   # uncomment to test it.
    # x = 'change x from inner_fun'


    print('after z: x=', x)  
    print('after z: y=', y)  
    print('after z: z=', z)  

  print('after inner_fun: x=', x)  
  print('after inner_fun: y=', y)  
  print('after inner_fun: z=', z)  

print('after outer_fun: x=', x)  
print('after outer_fun: y=', y)  
print('after outer_fun: z=', z)  




