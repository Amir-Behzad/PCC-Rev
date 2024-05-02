"""
3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.
"""
tourism_cities = [
    'Isfahan',
    'Vinland',
    'Sidney',
    'Paris',
    'Atlanta'
    
]

print(
    "len of cities' list:",
    len(tourism_cities),
    '\n',
    "the last city Atlanta:",
    tourism_cities[len(tourism_cities) - 1]
)