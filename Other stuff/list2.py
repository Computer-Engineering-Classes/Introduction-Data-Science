
import time

def count_evens(nums: list[int]) -> int:
    return sum(1 if n % 2 == 0 else 0 for n in nums)

def big_diff(nums: list[int]) -> int:
    return max(nums) - min(nums)

def centered_average(nums: list[int]) -> int:
    nums.remove(min(nums))
    nums.remove(max(nums))
    return sum(nums) // len(nums)

def sum13(nums: list[int]) -> int:
    if len(nums) == 0: return 0
    flag = False
    while not flag:
        try:
            i = nums.index(13)
            del nums[i : i + 2]
        except ValueError:
            flag = True
    return sum(nums)

def sum67(nums: list[int]) -> int:
    #nums = nums.copy()
    if len(nums) == 0: return 0
    flag = False
    while not flag:
        try:
            i = nums.index(6)
            j = nums.index(7, i)
            del nums[i:j + 1]
        except ValueError: flag = True
    return sum(nums)

def has22(nums: list[int]) -> bool:
    if len(nums) < 2: return False
    i = -1
    while i < len(nums):
        try:
            i = nums.index(2, i + 1)
            if (i < len(nums) - 1 and nums[i + 1] == 2):
                return True
        except ValueError:
            return False

if __name__ == "__main__":
    start = time.perf_counter()
    print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))
    end = time.perf_counter()
    print(end - start)
    pass