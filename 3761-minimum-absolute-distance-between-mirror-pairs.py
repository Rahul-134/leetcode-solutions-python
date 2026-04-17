from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        # My logic was to check for each number if its reverse is present in the remaining list and if it is then calculate the distance and store it in a list and return the minimum distance. But this approach is not efficient as it has a time complexity of O(n^2) and it also does not handle the case where there are duplicate numbers in the list.

        # d = []
        # count = 0
        # index = 1
        # for i in nums:
        #     if (int(str(i)[::-1]) == i) and (i >= 10) and (nums.count(i) == 1):
        #         continue
        #     if (int(str(i)[::-1]) in nums[index:]) and (nums.index(i) < nums[index:].index(int(str(i)[::-1])) + abs(len(nums) - len(nums[index:]))):
        #         print(index)
        #         count += 1
        #         d.append(abs(nums.index(i) - nums[index:].index(int(str(i)[::-1])) - abs(len(nums) - len(nums[index:]))))
        #     index += 1
        # return min(d) if count > 0 else -1
        
        # The above approach is not efficient and does not handle duplicates properly. A better approach is to use a dictionary to store the indices of the numbers and their reverses. We can iterate through the list from the end to the beginning and check if the reverse of the current number is already in the dictionary. If it is, we can calculate the distance and update the minimum distance. We also need to handle duplicates by storing all indices of a number in a list in the dictionary.
        
        def reverse_num(n):
            result = 0
            while n > 0:
                result = result * 10 + n % 10
                n //= 10
            return result
        
        min_distance = float('inf')
        seen_indices = {}
        
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            reversed_num = reverse_num(num)
            
            if reversed_num in seen_indices:
                distance = seen_indices[reversed_num][0] - i
                min_distance = min(min_distance, distance)
            
            if num not in seen_indices:
                seen_indices[num] = []
            seen_indices[num].insert(0, i)
        
        return min_distance if min_distance != float('inf') else -1
    

c = Solution()
print(c.minMirrorPairDistance([3,55,9,55,79,42]))