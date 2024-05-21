"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


def contains_duplicate(nums: list) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Example usage
nums = [1, 2, 3, 1]
print(contains_duplicate(nums))  # Output: True

nums = [1, 2, 3, 4]
print(contains_duplicate(nums))  # Output: False

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(contains_duplicate(nums))  # Output: True

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(contains_duplicate(nums))  # Output: False
