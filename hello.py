import sys

def hello(a,b):
    print("hello and that's your sum:", a + b)

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    hello(a, b)
# If you type : py main.py 1 5
# It should give you "hello and that's your sum:6"