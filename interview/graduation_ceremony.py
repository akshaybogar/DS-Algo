"""
Approach is to simulate possible number of ways to attend classes without missing 4 or 
more consecutive classes. This simulation follows dynamic programming (problem overlap + recursive).
Naive solution is followed below as I am not well versed with dynamic programming technique.
"""

import itertools


def ways_to_not_attend_grad_ceremony(n):
    if n <= 3:
        return 0
    arrangements = list(itertools.chain((n*(0,),), (l[0] * (0,) + sum(((1,) + (i-j-1) * (0,) for i, j in zip(l[1:], l[:-1])), ()) + (1,) + (n-l[-1]-1)*(0,) for k in range(1,n+1) for l in itertools.combinations(range(n), k))))
    ways_to_not_attend = 0
    for arrangement in arrangements:
        zeros_cnt = 0
        for i in arrangement:
            if i == 1:
                zeros_cnt = 0
            else:
                zeros_cnt += 1
            if zeros_cnt == 4:
                ways_to_not_attend += 1
                continue
    return ways_to_not_attend


if __name__ == '__main__':
    n = int(input('Enter number of days in graduation: '))
    ways_to_not_attend = ways_to_not_attend_grad_ceremony(n)
    print('Number of ways to attend graduation ceremony w/o missing 4 or more consecutive days', (2**n) - ways_to_not_attend)
    print('Probability of missing graduation ceremony {0:.3f}'.format(ways_to_not_attend/(2**n)))
