def name_pyramid(height, name):
    name_length = len(name)
    for i in range(height):
        # need to select the current letter from the name based on row number
        # and calculate the number of times to repeat the selected letter in that row
        row = name[i % name_length] * (2 * i + 1)
        # centering the row to create the pyramid shape
        # need to calculate the width
        print(row.center(2 * height))
        # maybe it should have been (2 * height - 1) if zero-based indexing is taken into account but nothing visibly changed in the terminal, no extra spaces
        # print(row.center(2 * height - 1))

# asking user for the height
# looping until the user provides a valid height
while True:
    try:
        height = int(input("Enter the height of the pyramid (1-40): "))
        if 1 <= height <= 40:
            break
        else:
            print("Not this time! Height must be between 1 and 40. Try again.")
    except ValueError:
        print("Value Error – invalid data type. Enter an integer") # if user inputs a letter or something other than integers

name = "Matīss"
name_pyramid(height, name)