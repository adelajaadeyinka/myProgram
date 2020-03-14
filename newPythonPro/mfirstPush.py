
def c(firstname , lastname):
     
     return(firstname + lastname)
     
print( c(2, 3))


def f(x):
    return(x**2 + 2*x + 1)
print(f(c(2,3)))
print(c(f(2),f(2)))