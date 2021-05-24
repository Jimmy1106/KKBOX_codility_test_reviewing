# Ref:https://www.tutorialspoint.com/insert-5-to-make-number-largest-in-python
#
# Suppose we have a number n, we have to find the maximum number we can make by inserting 5 anywhere in the number.
# So, if the input is like n = 826, then the output will be 8526.
# if the input is like n= -156, then the output will be -1556


""" 
'getMaxIntegerByInsertingFive' is a better solution compared to 'findMaxIntegerByFive'.

Tips: 
    - Pattern matching
    - There are (String_length+1) of Insertion positions
"""


def getMaxIntegerByInsertingFive(integer):
    """ Implemented without using additional spaces. """

    s_int = str(integer)

    if not integer<0:
        # Deal with positives and zero
        for i in range(len(s_int)):
            if int(s_int[i]) < 5:
                return int(s_int[:i] + "5" + s_int[i:])
    else:
        # Deal with negatives.
        s_int_unsigned = s_int[1:]
        for i in range(len(s_int_unsigned)):
            if int(s_int_unsigned[i]) > 5:
                return (-1)*int(s_int_unsigned[:i] + "5" + s_int_unsigned[i:])

    return int(s_int + '5')


def findMaxIntegerByFive_fixed(integer):
    """ Fixed the traversal times by plusing one. """

    s_int = str(integer)

    buffer = []
    # Deal with positive.
    if not integer<0:
        # for i in range(len(s_int)):
        for i in range(len(s_int)+1):
            new_int = s_int[:i] + "5" + s_int[i:]
            buffer.append(int(new_int))
        return max(buffer)
    else:
        s_int = s_int[1:]
        # for i in range(len(s_int)):
        for i in range(len(s_int)+1):
            new_int = s_int[:i] + "5" + s_int[i:]
            buffer.append(int(new_int))
        return (-1)*min(buffer)


example_cases = [
    826,
    -156,
    0,
    100,
    1,
    # Fail case (Fixed)
    -100,
    99,
    -1,
    
]

for case in example_cases:
    print("Input: %d, Output: %d" % (case, getMaxIntegerByInsertingFive(case)))
    # print("Input: %d, Output: %d" % (case, findMaxIntegerByFive_fixed(case)))