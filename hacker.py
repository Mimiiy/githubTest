
#challenge 1: Print the list of integers as a string, without spaces.
def main():
    x = int(input())
    y = return_sequence(x)

def return_sequence(n):
    for i in range(1,n+1):
        print(f"{i}", end="")

if __name__ == "__main__":
    main()

