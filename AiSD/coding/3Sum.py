
def threeSum(nums):
    nums = sorted(nums)
    while len(nums) > 1:
        fst = nums.pop(0) # pobieramy pierwszy element, do niego się odnosimy
        l = 0 # lewy pointer
        r = len(nums) - 1 # prawy pointer
        while l < r:
            if nums[l] + nums[r] + fst == 0: return True
            # brakuje nam do liczby, musimy się pozbyć tych za bardzo ujemnych
            elif nums[l] + nums[r] + fst < 0:
                l += 1
            # liczba jest za duża, zmniejszamy sumę
            elif  nums[l] + nums[r] + fst > 0:
                r -= 1
    # jak n <= 1 to nie da się dostać 3
    return False

if __name__ == "__main__":
    # t = [-1,3,2,0,3,-2,-2]
    t = [-1 ,-3 ,-2 ,2]
    print(threeSum(t))
