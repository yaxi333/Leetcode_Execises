# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring(s):
    # Solution 1
    # run from left
    # initalize:
    right = 1
    res = 0
    di = {}
    if len(s) == 1:
        return 1
    if len(s) == 0:
        return 0

    for left in range(len(s)):
        # Add the fist element into dictionary
        if left == 0:
            di[s[left]] = left

        # for current window(start from left point)
        # move right step by step and see if it has repeated
        while right < len(s) and right >= left:
            # if current right point char is not in dict
            # add it and its current pos (right) into dict
            if s[right] not in di:
                di[s[right]] = right
            else:
                # if lat repeated element occured pos is smaller than current windows first pos(left),
                # it means that current window does not has this element and we can just ignore this repetiton
                # if not, it means that the repetiton occurs and we should update the max_len = res
                left = max(di[s[right]] + 1, left)

                # update pos of the repeated element
                di[s[right]] = right
                # right is point to the repeated char now
            res = max(res, right - left + 1)
            right += 1

    # Solution 2
    # run from right
    # less O

    # mapSet = {}
    # start, result = 0, 0

    # for end in range(len(s)):
    # 	if s[end] in mapSet:
    # 		start = max(mapSet[s[end]], start)
    # 	result = max(result, end-start+1)
    # 	mapSet[s[end]] = end+1
    return res

s = "acbabbca"
print(lengthOfLongestSubstring(s))