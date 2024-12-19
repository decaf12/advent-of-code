def a(filename: str):
    nums1 = []
    nums2 = []
    with open(filename) as file:
        while line := file.readline():
            num1, num2 = map(int, line.split())
            nums1.append(num1)
            nums2.append(num2)
    nums1.sort()
    nums2.sort()
    return sum(abs(a - b) for a, b in zip(nums1, nums2))

print(a('./example.txt'))
print(a('./input.txt'))