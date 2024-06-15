# Welcome message
print("Welcome in our cinema\nHow we can help you ?")

# Movie options
request = {
    1 : "Showing Movies",
    2 : "Showing Animation",
    3 : "Showing Anime"
}
print(request)

# Get user's choice
order = int(input("Please input the number of your choice here 1 or 2 or 3 ? "))

# Handle movie selection
if order == 1:
    print("You chose showing movies\nBased on your choice, we have these movies:")
    movie_options = {
        1 : "Jumanji",
        2 : "The Mask",
        3 : "Suicide Squad"
    }
    print(movie_options)
    
    # Get user's age
    age = int(input("How old are you ? "))
    
    # Handle age restrictions for movies
    if age <= 12:
        print("Based on your age, it allows you to watch these movies only \"Jumanji\".")
    elif age <= 18:
        print("Based on your age,it allows you to watch these movies only 1- \"Jumanji\" or 2- \"The Mask\".")
        wanted = int(input("What is the number of the movie you want watch? "))
        # Handle user's movie choice
        if wanted == 1:
            print("you chose the \"Jumanji\"")
        elif wanted == 2:
            print("you chose the \"The Mask\"")
        else:
            print("you chose is not found .. Please try agian")
    else:
        print("Based on your age, it allows you to watch these movies \"Jumanji\" or \"The Mask\" or \"Suicide Squad\".")
        wanted = int(input("What is the number of the movie you want watch choice here 1 or 2 or 3 ? ? "))
        # Handle user's movie choice
        if wanted == 1:
            print("you chose \"Jumanji\"")
        elif wanted == 2:
            print("you chose \"The Mask\"")
        elif wanted == 3:
            print("you chose \"Suicide Squad\"")
        else:
            print("you chose is not found")
            
    # Get user's seat preference
    seat_number = int(input("Where do you prefer to sit? Choose a seat number from 1 to 200: "))
    
    # Calculate ticket price based on age and seat location
    if 1 <= seat_number <= 66 and age > 18:
        print("Your ticket is $102 have a nice showing.")
    elif 67 <= seat_number <= 132 and age >= 18:
        print("Your ticket is $90 have a nice showing.")
    # ... (additional ticket price conditions)

# Handle animation selection
elif order == 2:
    print("You chose showing Animation\nBased on your choice, we have these Animations:")
    animation_options = {
        1 : "Toy Story",
        2 : "Batman",
        3 : "Tarazan"
    }
    print(animation_options)
    
    # Get user's age
    age = int(input("How old are you ? "))
    
    # Handle age restrictions for animations
    if age <= 12:
        print("Based on your age, it allows you to watch these movies only \"Toy Story\".")
    elif age <= 18:
        print("Based on your age,it allows you to watch these movies only 1- \"Toy Story\" or 2- \"Batman\".")
        wanted = int(input("What is the number of the movie you want watch? "))
        # Handle user's animation choice
        if wanted == 1:
            print("you chose the \"Toy Story\"")
        elif wanted == 2:
            print("you chose the \"Batman\"")
        else:
            print("you chose is not found")
    else:
        print("Based on your age, it allows you to watch these movies only \"Toy Story\" or \"Batman\" or \"Tarazan\".")
        wanted = int(input("What is the number of the movie you want watch choice here 1 or 2 or 3 ? ? "))
        # Handle user's animation choice
        if wanted == 1:
            print("you chose \"Toy Story\"")
        elif wanted == 2:
            print("you chose \"Batman\"")
        elif wanted == 3:
            print("you chose \"Tarazan\"")
        else:
            print("you chose is not found")
            
    # Get user's seat preference
    seat_number = int(input("Where do you prefer to sit? Choose a seat number from 1 to 200: "))
    
    # Calculate ticket price based on age and seat location
    if 1 <= seat_number <= 66 and age >= 18:
        print("Your ticket is $70 have a nice showing.")
    # ... (additional ticket price conditions)

# Handle anime selection
elif order == 3:
    print("You chose showing Anime\nBased on your choice, we have these Anime:")
    anime_options = {
        1 : "Tom and Jerry",
        2 : "One Pice",
        3 : "Attack on Titan"
    }
    
    # Get user's age
    age = int(input("How old are you ? "))
    
    # Handle age restrictions for anime
    if age <= 12:
        print("Based on your age, it allows you to watch these movies only \"Tom and Jerry\".")
    elif age <= 18:
        print("Based on your age,it allows you to watch these movies only 1- \"Tom and Jerry\" or 2- \"One Pice\".")
        wanted = int(input("What is the number of the movie you want watch? "))
        # Handle user's anime choice
        if wanted == 1:
            print("you chose the \"Tom and Jerry\"")
        elif wanted == 2:
            print("you chose the \"One Pice\"")
        else:
            print("you chose is not found")
    else:
        print("Based on your age, it allows you to watch these movies only \"Tom and Jerry\" or \"One Pice\" or \"Attack on Titan\".")
        wanted = int(input("What is the number of the movie you want watch choice here 1 or 2 or 3 ? ? "))
        # Handle user's anime choice
        if wanted == 1:
            print("you chose \"Tom and Jerry\"")
        elif wanted == 2:
            print("you chose \"One Pice\"")
        elif wanted == 3:
            print("you chose \"Attack on Titan\"")
        else:
            print("you chose is not found")
            
    # Get user's seat preference
    seat_number = int(input("Where do you prefer to sit? Choose a seat number from 1 to 200: "))
    
    # Calculate ticket price based on age and seat location
    if 1 <= seat_number <= 66 and age >= 18:
        print("Your ticket is $50 have a nice showing.")
    # ... (additional ticket price conditions)
    
# Handle incorrect input
else:
    print("An error occurred. The number you entered is incorrect, please try again.")