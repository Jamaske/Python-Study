N, k, q = map(int, input().split())
heights = list(map(int, input().split()))

left, right, changes, max_length = 0, 0, 0, 0

while right < N:
    if heights[right] >= k:
        changes += 1
    while changes > q:
        if heights[left] >= k:
            changes -= 1
        left += 1
    max_length = max(max_length, right - left + 1)
    right += 1

print(max_length)
