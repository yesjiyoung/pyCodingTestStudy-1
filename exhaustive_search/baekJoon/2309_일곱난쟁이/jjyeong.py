# 첫번째풀이 ## sorted(li)<-★제일빨랐음 / li.sort()
import sys

li = [int(sys.stdin.readline()) for _ in range(9)]
from itertools import combinations
for com in combinations(li,2):
    if sum(li) - sum(com) == 100:
        li.remove(com[0])
        li.remove(com[1])
        break
print(*sorted(li), sep='\n')


# # 두번째풀이 : 7개로 조합하면 ?
# import sys

# li = [int(sys.stdin.readline()) for _ in range(9)]
# print(li)

# print(sum(li))
# from itertools import combinations

# print(list(combinations(li,2)))
# for com in combinations(li,7):
#     if sum(com) == 100:
#         break
# com = list(com)
# com.sort()
# print(*com, sep='\n')