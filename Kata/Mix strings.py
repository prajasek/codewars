def mix(s1, s2):
    
    """Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into 
    account the lowercase letters (a to z). First let us count the frequency of each lowercase letters in s1 and s2.
    
    s1 = "A aaaa bb c"
    s2 = "& aaa bbb c d"
    
    s1 has 4 'a', 2 'b', 1 'c'
    s2 has 3 'a', 3 'b', 1 'c', 1 'd'
    So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. 
    
    In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.
    We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands 
    for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands for string s2 and bbb 
    because the maximum for b is 3.The task is to produce a string in which each lowercase letters of s1 or s2 
    appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed 
    by the number of the string where they appear with their maximum value and :. If the maximum is in s1 as well 
    as in s2 the prefix is =:.
    
    Input : s1 ="aaabbcc" s2= "aabbbbcc"
    Output: "1:aaa/2:bbbb/=:cc"
    """

    count = []
    s1.replace(" ","")
    s2.replace(" ","")
    
    for letter_1 in s1:
        for letter_2 in s2:
            if letter_2 in letter_1:
                if s1.count(letter_1)==1 and s2.count(letter_2)==1: pass
                elif s1.count(letter_1) > s2.count(letter_2):
                    count.append("1:" + str(letter_1)*s1.count(letter_1))
                elif s1.count(letter_1) < s2.count(letter_2):
                    count.append("2:" + str(letter_2)*s2.count(letter_2))
                else:
                    count.append("=:" + str(letter_2)*s2.count(letter_2))
    count = list(set(count))
    return "/".join(count) 
