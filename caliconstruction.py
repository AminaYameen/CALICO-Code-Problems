from collections import Counter

def min_calico_sets(S):
    # Define the available letters from one CALICO block
    calico_letters = Counter("CALICO")
    calico_letters["C"] += 1  # Account for rotated C creating another C, N, and U
    calico_letters["N"] += 1
    calico_letters["U"] += 1

    # Count the frequency of letters in the target string S
    target_count = Counter(S)

    # Check if any letter in S cannot be formed using CALICO blocks
    for letter in target_count:
        if letter not in calico_letters:
            return -1

    # Calculate the number of blocks needed for each letter
    max_blocks = 0
    for letter, count in target_count.items():
        blocks_needed = (count + calico_letters[letter] - 1) // calico_letters[letter]  # Ceiling division
        max_blocks = max(max_blocks, blocks_needed)

    return max_blocks

# Input and Output Handling
test_cases = [
    "COIL", 
    "LOL", 
    "A", 
    "UNCCCCC", 
    "CALICONSTRUCTION", 
    "Q", 
    "NONALCOHOLIC"
]

results = [min_calico_sets(S) for S in test_cases]
print("\n".join(map(str, results)))
