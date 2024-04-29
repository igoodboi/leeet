def revese_the_str(s: str) -> str:
    l = ""
    for i in range(len(s)):
        l = l + s[-1 - i]
    return l


if __name__ == '__main__':
    while True:
        s = input('please type in a string for those who are to dumb type multiple numbers\n')
        reversed = revese_the_str(s)
        print(f"you typed {s} i print {reversed}:")
