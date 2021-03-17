# leetcode
# 56.合并区间

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

# Solution 1
# def merge(intervals):
#     # new interval list:
#     ls = []
#     intervals.sort(key=lambda x: x[0])
#     for i in range(len(intervals) - 1):
#         # 先把区间按第一个数字从小到大排序：
#         if intervals[i + 1][0] <= intervals[i][1]:
#             intervals[i + 1][0] = intervals[i][0]
#             intervals[i + 1][1] = max(intervals[i + 1][1], intervals[i][1])
#         else:
#             ls.append(intervals[i])
#     ls.append(intervals[-1])
#     return ls

# Solution 2
def merge(intervals):
    # new interval list:
    ls = []
    # 先把区间按第一个数字从小到大排序：
    intervals.sort(key=lambda x: x[0])

    for inter in intervals:
        if not ls or ls[-1][1] < inter[0]:
            ls.append(inter)
        else:
            ls[-1][1] = max(inter[1], ls[-1][1])
    return ls


print(merge(intervals))
