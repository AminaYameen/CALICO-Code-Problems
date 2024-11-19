def draw_cookie(test_cases):
    for S in test_cases:
        i = 0
        while i < len(S):
            # Handle "RE" token
            if S[i:i+2] == "RE":
                print(" [--------] ")
                i += 2
            # Handle "O" token
            elif S[i] == "O":
                print("[###OREO###]")
                i += 1
            # Handle "&" token
            elif S[i] == "&":
                print("")  # Print an empty line
                i += 1
            else:
                print(f"Invalid token: {S[i]}")
                i += 1

# Test Cases
test_cases = [
    "OREO",        # Test case #1
    "O&REO",       # Test case #2
    "OREOREREREORE"  # Test case #8
]

# Call the function with the test cases
draw_cookie(test_cases)
