"""
PROBLEM: Given an inputted string, create a new string as follows:
1. Change uppercase letters to lowercase and eliminate all non-letters.
2. Find all first occurrences of each distinct letter and arrange them in sorted order.
3. Append these sorted letters to the end of a new string and remove those distinct letters from the
original string.
4. Repeat steps 2 and 3 until the original string is empty.
5. Before outputting the new string, remove adjacent duplicate letters (e.g. "bboooo" becomes "bo").
For example, the string “A good sorting algorithm.” would arrange as follows:
1st pass: New string: adghilmnorst Rest of string: oogagorit
2nd pass: New string: adghilmnorstagiort Rest of string: ogo
3rd pass: New string: adghilmnorstagiortgo Rest of string: o
4th pass: New string: adghilmnorstagiortgoo Rest of string:
Output: adghilmnorstagiortgo
INPUT: There will be 5 lines of data, each containing a single string that is fewer than 100 characters in
length.
OUTPUT: The new string as specified above.

SAMPLE INPUT: SAMPLE OUTPUT:
A good sorting algorithm. 1. adghilmnorstagiortgo
Tennessee is the volunteer state. 2. aehilnorstuvenstenstestete
Einstein was a genius. 3. aeginstuwaeinseins
Tom Sawyer & the Mississippi River 4. aehimoprstvwyeimprsteirsisis
She sells seashells by the seashore. 5. abehlorstyaehlsehlsehlseseses

2020-2021 ● Contest 2: Lex Strings ● Junior Division

TEST INPUT:
Peter Piper picked a peck of pickled peppers.
Computer Science Teachers Association had a virtual Conference in
2020.
HackerRank.com was used for the ACSL Finals this past year.
Programming languages include Java, Python, C++, BASIC, and Scratch.
COVID-19 is a global pandemic and a virus that changed everything.

TEST OUTPUT:
1. acdefikloprstcdeikprceikprepepepepep
2. acdefhilmnoprstuvacehinorstuaceinorstaceinorstaceinacece
3. acdefhiklmnoprstuwyacefhiklnorstacehrstaersasasa
4. abcdeghijlmnoprstuvyacdeghilmnoprstuacginrsacgnacna
5. abcdeghilmnoprstuvyacdeghilnorstvacdeghintvadeinaia
"""


class Solution:
    def lex_str(self, org: str):
        new_string = ""
        while org:
            pass
            ## Change uppercase letters to lowercase
            ## eliminate all non-letters.
            lst = [l.lower() for l in org if l.isalpha()]
            ## Find all first occurrences of each distinct letter and arrange them in sorted order.
            set1 = set(lst)
            str2 = ''.join(sorted(set1))
            ## Append these sorted letters to the end of a new string
            new_string = new_string + str2
            ## remove those distinct letters from the original string

            for l in set1:
                lst.remove(l)
            org = ''.join(lst)

        ## Before outputting the new string, remove adjacent duplicate letters (e.g. "bboooo" becomes "bo").
        new_lst = []
        for i in range(len(new_string)):
            if i + 1 == len(new_string) or new_string[i] != new_string[i + 1]:
                new_lst.append(new_string[i])
        return ''.join(new_lst)


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    tests = ["Peter Piper picked a peck of pickled peppers."
        , "Computer Science Teachers Association had a virtual Conference in 2020."
        , "HackerRank.com was used for the ACSL Finals this past year."
        , "Programming languages include Java, Python, C++, BASIC, and Scratch."
        , "COVID-19 is a global pandemic and a virus that changed everything."]
    outputs = ["acdefikloprstcdeikprceikprepepepepep"
        , "acdefhilmnoprstuvacehinorstuaceinorstaceinorstaceinacece"
        , "acdefhiklmnoprstuwyacefhiklnorstacehrstaersasasa"
        , "abcdeghijlmnoprstuvyacdeghilmnoprstuacginrsacgnacna"
        , "abcdeghilmnoprstuvyacdeghilnorstvacdeghintvadeinaia"]
    for i in range(len(tests)):
        test = tests[i]
        answer = sol.lex_str(test)
        if answer == outputs[i]:
            print("👍👏Yippeee")
        elif answer != outputs[i]:
            print("BOOOOOOOOOOOOO >:( 🤮😱🤮😱🤮😱🤮😱🤮😱🤮😱")
