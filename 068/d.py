import sys
import logging
from itertools import product
from collections import defaultdict
 
 
def ceil_div(a: int, b: int) -> int:
    """
    math.ceil(a / b)
 
    cf. https://linus-mk.hatenablog.com/entry/2019/05/26/234642
    """
    return (a + b - 1) // b
 
 
def decrease(a):
    n = len(a)
    count = 0
    while max(a) > n - 1:
        i_max = 0
        ai_max = a[0]
        for i in range(1, n):
            if a[i] > ai_max:
                i_max = i
                ai_max = a[i]
        for i in range(n):
            if i_max == i:
                a[i] -= n
            else:
                a[i] += 1
        count += 1
    return count, a
 
 
def main_experiment():
    history = defaultdict(list)
    p_max = 15
    for p1 in range(p_max):
        for p2 in range(p1, p_max):
            for p3 in range(p2, p_max):
                p = [p1, p2, p3]
                ans, p_decreased = decrease(p[:])
                logging.debug("p=%s, sum(p)=%s, sum(p_decreased)=%s, k=%s", p, sum(p), sum(p_decreased), ans)
                history[ans].append(sum(p) - sum(p_decreased))
 
    for i in range(20):
        logging.debug("%s: %s", i, sorted(history[i]))
 
 
def main():
    k = int(input())
    a = [49] * 50
    a[0] = 0
    k50 = ceil_div(k, 50)
    k_remaining = k
    for i in range(50):
        if k_remaining < k50:
            ki = k_remaining
        else:
            ki = k50
        a[i] += 51 * ki - k
        k_remaining -= ki
    print(50)
    print(*a)
 
    # k_ans, _ans = decrease(a)
    # logging.debug(k_ans)
 
 
if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--debug":
        loglevel = "debug"
    else:
        loglevel = "warning"
 
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % loglevel)
    logging.basicConfig(
        level=numeric_level, format="%(levelname)s (%(asctime)s.%(msecs)d): %(message)s", datefmt="%I:%M:%S"
    )
 
    main()