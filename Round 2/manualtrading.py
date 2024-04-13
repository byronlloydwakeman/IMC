# Round 2
pizza_slice = [1, 0.48, 1.52, 0.71]
wasabi_root = [2.05, 1, 3.26, 1.56]
snowball = [0.64, 0.3, 1, 0.46]
shells = [1.41, 0.61, 2.08, 1]

rates = [
    pizza_slice,
    wasabi_root,
    snowball,
    shells
]

starting_shells = 2000

pizza_index = 0
wasabi_root_index = 1
snowball_index = 2
shells_index = 3

indices = [
    pizza_index,
    wasabi_root_index,
    snowball_index,
    shells_index
]

currencies = [
    "Pizza",
    "Wasabi Root",
    "Snowball",
    "Shell"
]

n1results = []
n1results_string = []
n2results = []
n2results_string = []

# Starting
for index, shell_rate in enumerate(shells):
    n1 = starting_shells * shell_rate
    n1results.append(n1 * rates[index][shells_index])
    n1results_string.append(currencies[index])
    for n2_index, n2_rate in enumerate(rates[index]):
        n2 = n1results[index] * n2_rate
        n2results.append(n2 * rates[index][indices[n2_index]])
        n2results_string.append(currencies[n2_index])

# print(n1results)
# print(n1results_string)
# print(n2results)
# print(n2results_string)

# Hamed's solution

import itertools

# Define the possible indices

# Generate combinations for arrays of size 3, 4, and 5
generated_indicies = []
for size in range(3, 7):
    for combo in itertools.product([0, 1, 2, 3], repeat=size - 2):
        # Ensure that all arrays start and end with the 3 index
        combo = (3,) + combo + (3,)
        generated_indicies.append(combo)

print(generated_indicies)

generated_results = []

for index, gen in enumerate(generated_indicies):
    temp = 1
    prev = gen[0]  # Shells array or whatever
    for el in gen:
        temp *= rates[prev][el]
        prev = el
    generated_results.append(temp)

print(max(generated_results))
print([currencies[i] for i in generated_indicies[generated_results.index(max(generated_results))]])





