
def fact(n):

    if n==1:
        return 1

    else:
        return n*fact(n-1)


def main():

    print(fact(5))

main()