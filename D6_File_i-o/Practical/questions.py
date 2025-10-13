'''
    Q1. 
'''

# q1_poem = "Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky"

# with open("D6_File_i-o/Practical/q1.txt", "w") as poem:
#     print(poem.write(q1_poem))
    

# with open("D6_File_i-o/Practical/q1.txt", "r") as poem:
#     content = poem.read()
#     if "little" in content:
#         print(True)
#     else:
#         print(False)    



'''
    Q2.
'''

# def game(score):
    
#     # Reading the current high score
#     with open("D6_File_i-o/Practical/Hi-score.txt", "r") as hi:
#         data = hi.read()
        
#         if data == "":
#             data = "0"
            
#     # Comparing and updating
#         if int(score) > int(data):
#             with open("D6_File_i-o/Practical/Hi-score.txt", "w") as new_hi:
#                 new_hi.write(score)
#                 return f"\nnew Hi-score is {score}."
#         else:
#             return f"\nBetter luck next time! \nCurrent high score is {data}"
        
# score = input("What is your score: ")
# print(game(score))



'''
    Q3.
'''

# def tables(start, end):
#     num = 1
#     for i in range(start, end+1):
#         with open(f"D6_File_i-o/Practical/Table of {i}.txt", "w") as f:
#             for  j in range(1, 11):
#                 multi = i*j
#                 f.write(f"{i} x {num} = {multi}\n")
                
        
# start = int(input("Enter the start and end: "))
# end = int(input("Enter the start and end: "))
# print(tables(start, end))

