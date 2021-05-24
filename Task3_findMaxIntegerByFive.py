# Ref:https://www.tutorialspoint.com/insert-5-to-make-number-largest-in-python

""" This is original anwser that only score 40% on test. """

def findMaxIntegerByFive(integer):

    s_int = str(integer)

    buffer = []
    # Deal with positive.
    if not integer<0:
        for i in range(len(s_int)):
            new_int = s_int[:i] + "5" + s_int[i:]
            buffer.append(int(new_int))
        return max(buffer)
    else:
        s_int = s_int[1:]
        for i in range(len(s_int)):
            new_int = s_int[:i] + "5" + s_int[i:]
            buffer.append(int(new_int))
        return (-1)*min(buffer)


example_cases = [
    826,
    -156,
    0,
    100,
    1,
    # Fail case
    -100,
    99,
    -1,
    
]

for case in example_cases:
    print("Input: %d, Output: %d" % (case, findMaxIntegerByFive(case)))