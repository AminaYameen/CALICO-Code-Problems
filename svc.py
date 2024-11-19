def identify_shapes(T, test_cases):
    results = []
    for case in test_cases:
        N, M, grid = case
        # Find the top-left and bottom-right corners of the shape
        points = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == '#']
        top_left = min(points)
        bottom_right = max(points)
        
        # Determine if it's a rectangle
        is_rectangle = all((x, bottom_right[1]) in points and (bottom_right[0], y) in points for x, y in points)
        
        if is_rectangle:
            results.append("ferb")
        else:
            results.append("phineas")
    return results

# Reading Input
T = 6
test_cases = [
    (5, 5, [
        ".....",
        ".....",
        "..#..",
        "..##.",
        "....."
    ]),
    (5, 5, [
        "#####",
        "#####",
        "#####",
        "#####",
        "#####"
    ]),
    (3, 5, [
        "###..",
        ".##..",
        "..#.."
    ]),
    (8, 20, [
        "....................",
        "....................",
        "....................",
        "....................",
        "....................",
        "####################",
        "####################",
        "####################"
    ]),
    (2, 2, [
        "##",
        "#."
    ]),
    (5, 5, [
        "####.",
        ".###.",
        "..##.",
        "...#.",
        "....."
    ])
]

# Output Results
output = identify_shapes(T, test_cases)
print("\n".join(output))
