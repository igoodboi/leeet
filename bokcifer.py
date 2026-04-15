
"""
PROBLEM: A book cipher is a method of encoding and decoding a message where the sender
and the receiver both use the same text. The sender’s message is encoded by replacing each
alphanumeric character in the message to be sent with the location of that character in the text
using an “s.w.c” format representing the number of the sentence in the text (s), the number of the
word in that sentence (w), and the number of the character in that word (c), all indexed starting
with 1. The receiver decodes the encoded message by locating the characters in the text
specified by each “s.w.c” string.
In this program, you will be given the text and the encoded message to be decoded. The text will
contain alphanumeric characters, spaces, and periods using the following restrictions:
● A word contains only alphanumeric characters
● All words are separated by a single space
● Sentences are terminated with a period and separated by two spaces
The encoded message will contain multiple “s.w.c” strings, each separated by a single space.
Create the decoded message by finding the characters in the text. If an “s.w.c” string doesn’t
refer to a character in the text, use a space in the decoded message.
EXAMPLE:
Input:
ACSL is an international computer science competition among more than
300 schools. With countrywide and worldwide participants it became
the American Computer Science League. It has been in continuous
existence since 1978. Each yearly competition consists of 4 regular
season contests. All students at each school may compete but the
team score is the sum of the best 3 or 5 top scores. Each contest
consists of a written section and a programming section.
1.5.4 4.2.6 1.10.1 3.2.1 6.11.6 2.9.8 4.10.3 5.18.1
Output:
python 3
Explanation:
The first encoded string “1.5.4” tells you to find the 1st sentence, the 5th word in that sentence
which is “computer”, and then the 4th character in that word which is the lowercase letter “p”.
All others are done in a similar fashion. The string “4.10.3” is a space because there are only 9
words in the 4th sentence.

2023-2024 ● Contest 2: ACSL Book ● Junior Division
INPUT: Input a string representing the text to be used in the decoding and another string
representing the encoded message to be decoded. The first string will be no more than 2000
characters and the second string will be no longer than 200 characters.
OUTPUT: Output the decoded message as a string of characters.
"""


class Solution:
    def splitbanana(self ,text, message):
        # 1 Split text into a list of sentences
        sentences = text.split(".  ")
        print(sentences, message)
        out = []
        # 2 Loop through each code (like "1.5.4")
        for code in message.split():
            parts = code.split(".")
            s = int(parts[0]) - 1  # Sentence
            w = int(parts[1]) - 1  # Word
            c = int(parts[2]) - 1  # Character
            char = " "
            if s < len(sentences):
                words = sentences[s].replace(".", "").split()

                if w < len(words):
                    target_word = words[w]

                    if c < len(target_word):
                        char = target_word[c]
            out.append(charr)
        return "".join(out)


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    tests = [(("ACSL is an international computer science competition among more than 300 schools.  With countrywide and worldwide participants it became the American Computer Science League.  It has been in continuous existence since 1978.  Each yearly competition consists of 4 regular season contests.  All students at each school may compete but the team score is the sum of the best 3 or 5 top scores.  Each contest consists of a written section and a programming section."),("1.5.4 4.2.6 1.10.1 3.2.1 6.11.6 2.9.8 4.10.3 5.18.1"))]
    outputs = [("python 3")]
    for i in range(len(tests)):
        text, message = tests[i]
        answer = sol.splitbanana(text, message)
        if answer == outputs[i]:
            print("👍👏Yippeee")
            print(answer)
            print(outputs[i])
        elif answer != outputs[i]:
            print("BOOOOOOOOOOOOO >:( 🤮😱🤮😱🤮😱🤮😱🤮😱🤮😱")
            print(answer)
            print(outputs[i])