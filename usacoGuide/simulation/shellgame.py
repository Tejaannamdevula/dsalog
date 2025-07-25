N = int(input())

"""
first simulation iterate over the possible pebble positon and take simulate swaps

keep the count of the correct guesses for each pebble position and print max

"""

pebble_counter = [0, 0, 0]

moves = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(3):
    position = i
    for a, b, g in moves:
        # swapping pebble
        if position == a:
            position = b
        elif position == b:
            position = a
        if g == position:
            pebble_counter[i] += 1

print(max(pebble_counter))


# Time Complexity :- O(3*N) = O(N)
# Space Complexity :- O(3*N) = O(N)

"""
    USACO OFFICIAL SOLUTION

"""
