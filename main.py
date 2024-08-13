# Prompt the user for their name
name = input("Welcome to GC mini golf! What is your name?\n")
print(f"Hi, {name}!")

# Prompt the user to choose 3 or 6 holes
holes = int(input("Would you like to play 3 or 6 holes?\n"))

# Ensure the user selects either 3 or 6
while holes not in [3, 6]:
    print("Please choose either 3 or 6.")
    holes = int(input("Would you like to play 3 or 6 holes?\n"))

# Set the course par based on the number of holes
course_par = holes * 3  # Since par is 3 for each hole

# Initialize the user's total score
total_score = 0

# Loop through each hole to get the number of putts
for hole in range(1, holes + 1):
    putts = int(input(f"How many putts for hole {hole}? (par: 3)\n"))
    total_score += putts

# Calculate the difference between the course par and the user's score
total_par = total_score - course_par

# Display the result to the user
if total_par > 0:
    print(f"Nice try, {name}... Your total score was: +{total_par}.")
elif total_par < 0:
    print(f"Great job, {name}! Your total score was: {total_par}.")
else:
    print(f"Good game, {name}. Your total score was: 0.")
