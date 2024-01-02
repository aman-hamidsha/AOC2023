file = open('input.txt','r')
games = file.readlines()

#PART 1 AND PART 2

invalid_games = []
p2 = 0
for game in games:
    isValid = True 
    updated_game = game[7:] # cuts out "Game x: "

    # lists to store values of each colors for each game
    reds = []
    blues = []
    greens = []

    for k in range(len(updated_game)): # appends the number of each color to corresponding list, try-catch to pass errors in edge cases
      try:
        if (updated_game[k+2] == "b"):
          if updated_game[k-1] != " ":
            blues.append(updated_game[k-1]+updated_game[k])
          else:
            blues.append(updated_game[k])
        elif (updated_game[k+2] == "g"):
          if updated_game[k-1] != " ":
            greens.append(updated_game[k-1]+updated_game[k])
          else:
            greens.append(updated_game[k])
        elif (updated_game[k+2]+updated_game[k+3]+updated_game[k+4] == "red"):
          if updated_game[k-1] != " ":
            reds.append(updated_game[k-1]+updated_game[k])
          else:
            reds.append(updated_game[k])
      except:
        pass


    # list comprehension to convert all strings to integers
    reds_nums = [int(x) for x in reds]
    blues_nums = [int(x) for x in blues]
    greens_nums = [int(x) for x in greens]
    

    # conditions based on problem specification, flag set to false
    for red in reds_nums:
      if red > 12:
        isValid = False
        break;


    for green in greens_nums:
      if green > 13:
        isValid = False
        break;

    for blue in blues_nums:
      if blue > 14:
        isValid = False
        break;
    
    if (isValid == False): # appending invalid games, conditional to deal with 1,2 and 3 digit game IDs
        if (game[5] == "1" and game[6] == "0" and game[7] == "0"):
           invalid_games.append(game[5]+game[6]+game[7])
        elif game[5+1] == ":":
           invalid_games.append(game[5])
        else:
           invalid_games.append(game[5]+game[6])
    
    p2+= max(reds_nums)*max(greens_nums)*max(blues_nums) # part 2 is just the product of the maximum of each color



p1 = 5050-sum([int(x) for x in invalid_games]) #  sum of valid games IDs
#because the sum from 1 to 100 is 5050 calculated using 0.5 * n * (n+1)

print(p1)
print(p2)
