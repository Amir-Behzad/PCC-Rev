"""
3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

stoic_figures = [
    'Seneca',
    'Zeno',
    'Goggins',
    'Ryan Holiday',
    'Ciccero',
    'Demostenis'
]

tourism_cities = [
    'Isfahan',
    'Vinland',
    'Sidney',
    'Paris',
    'Atlanta'
]

stoic_figures.sort()
tourism_cities.sort(reverse=1)

for city in tourism_cities:
    for stoic in stoic_figures:
        print(f"\n{stoic} stands for his values in {city} as always.")
        
        