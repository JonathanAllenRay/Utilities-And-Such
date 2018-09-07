
from Collatz import collatz_eval
from sys     import stdin, stdout

# For a school project (Collatz not in this repo to prevent plagiarism)
if __name__ == "__main__" :
    stdout.write('[')
    for n in range(1, 1000):
        num = collatz_eval (0 + n*1000, 1000 + 1000*n)
        stdout.write(str(num) + ',')
        if n % 10 == 0:
            stdout.write(str(num) + '\n')
    stdout.write(']')

