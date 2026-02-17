# def myfunc():
#   x = 300
#   #print(x + y)


# y = 5
# #print (x + y)
# myfunc()

# x = 300 + 100

# #def myfunc():
#   #print(x)

# myfunc()

# #print(x)

# def myfunc2():
#   x = "Jane"
#   def myfunc3():
#     nonlocal x
#     x = "hello"
#   myfunc3()
#   return x

# print(myfunc2())

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)