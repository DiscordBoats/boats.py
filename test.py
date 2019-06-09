from boats import Boats

b = Boats("abc123")

a = b.get_bot("477594964742635531")
print(a)

c = b.get_voted("477594964742635531", "321242389106786314")
print(c)

d = b.get_user("321242389106786314")
print(d)

