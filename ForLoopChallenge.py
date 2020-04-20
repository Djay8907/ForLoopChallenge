#ForLoopChallenge
#A Python challenge algorithm that uses a for-loop to convert an array of integers into the string "x" in order to form a letter.
numbers = [2, 2, 2, 2, 6]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
