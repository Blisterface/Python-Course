def highest_even(li):
    even = []
    for x in li:
        if x % 2==0:
            even.append(x)
    return max(even)

if __name__=='__main__':
    nums=[1,3,8,13,14,27,6,53]
    print(highest_even(nums))

x = int(5)
print(type(x))