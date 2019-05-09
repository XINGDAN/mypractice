import random
import pytest
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return random.choice([nums,None,10])#nums

'''
@pytest.mark.parametrize("x,y,z",[
    ([12,23,11],None,10),
])
def test_bubble_sort(x,y,z):
    assert bubble_sort(x,y,z) == random.choice(x,y,z)

'''

lis = [12,21,13,99,6]
print(bubble_sort(lis))
