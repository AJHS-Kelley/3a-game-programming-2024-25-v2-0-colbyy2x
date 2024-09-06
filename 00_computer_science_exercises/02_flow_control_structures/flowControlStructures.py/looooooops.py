# Loops, JaColby Allen, v0.0

#  TWO TYPES OF LOOPS 
# for <-- Used when you kno whow many loops you'll need.
# while <-- Used when you do not know how many loops you'll need.

# for loop is like Go Fish, you search each card for what the player asked.
# while loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
# "iterate throgh the list" means use a for loop

# for loop Example -- Iterating a List
# fruits =["apple", " banana", "kiwi", "orange"]
# for eachFruit in fruits:
#     print(eachFruit)

#continue Keyword -- Skips the current iteration and then finishes the loop.
# fruits =["apple", " banana", "kiwi", "orange"]
# for eachFruit in fruits:
#     if eachFruit== "banana":
#         continue
#     print(eachFruit)

# break Keyword -- Immediately exit the loop.
fruits =["apple", " banana", "kiwi", "orange"]
for eachFruit in fruits:
    if eachFruit== "banana":
        break
    print(eachFruit)

# for loops using range().  range(x) is EXCLUSIVE, it starts at 0 and ends at x -1 
for i in range(10): # range is 0-9
    print(i)


