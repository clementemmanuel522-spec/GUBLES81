def my_function(fname, lname):
  print("hey", fname, lname)

person = {"fname": "George", "lname": "Moses"}
my_function(**person)