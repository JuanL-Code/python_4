def run():
   #A list with all 4,6 and 9 multiples until 5 digits == MCM

    squares = [ i for i in range(1, 100000) if i % 36 == 0]
    
    
    print(squares)


if __name__ == "__main__":
    run()

#estructure = [element for element in iterable if condition]