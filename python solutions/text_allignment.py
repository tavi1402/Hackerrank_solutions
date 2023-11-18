thickness = int(input())  # This must be an odd number
c = 'H'  # Character to use for the pattern

# Top Cone
for i in range(thickness):
    # Print the pattern for the top cone.
    # 'rjust' is used to right-justify and pad with spaces on the left side.
    # 'ljust' is used to left-justify and pad with spaces on the right side.
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    # Print the pattern for the top pillars.
    # 'center' is used to center-align the characters within a specified width.
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    # Print the pattern for the middle belt.
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    # Print the pattern for the bottom pillars.
    # 'center' is used to center-align the characters within a specified width.
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    # Print the pattern for the bottom cone.
    # 'rjust' is used to right-justify and pad with spaces on the left side.
    # 'ljust' is used to left-justify and pad with spaces on the right side.
    # 'rjust' is used again to align the pattern to the right within a larger width.
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
