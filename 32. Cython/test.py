import timeit

# setup=import -> imports code first so it doesn't time the import time
cy = timeit.timeit("example_cy.test(500)", setup="import example_cy", number=1000)
py = timeit.timeit("example_py.test(500)", setup="import example_py", number=1000)

print(cy, py)
print(f"Cython is {round(py / cy, 2)}x faster")