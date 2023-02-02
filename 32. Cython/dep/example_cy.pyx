# you only need a <name>.pyx and a setup.py to do everything

# the below code can be written in normal python as well
# but we'll be using cython cpp style

# we don't have to say cpdef int since we already declared cpdef beforehand
cpdef int test(int x): # will return an integer
    cdef int y = 0 # cdef since we'll not be accesing y anywhere outside the function
    cdef int i
    # cdef str l = "hello"
    print(l)
    for i in range(x):
        y += i
    
    return y