import random
question={"Which God is Known as 'Gauri Nandan'? ":'Ganesha', # Agni Indra Hanuman Ganesha
          "What does not grow on tree according to popular Hindi Saying? ": "Money", # Money  Flowers Leaves Fruits
          "Which city is known as pink city in India? ": "Jaipur",     # Banglore Maysore Jaipur Kochi
          "Who wrote India's National Antheme? ": "Rabindranath Tagore" # Rabindranath Tagore Lal Bahadur Shastri Chetan Bhagat RK Narayan
          }
option=[["Agni", "Indra", "Hanuman", "Ganesha"],["Money" ,"Flowers","Leaves","Fruits"],["Banglore", "Maysore", "Jaipur", "Kochi"],["Rabindranath Tagore","Lal Bahadur Shastri","Chetan Bhagat","RK Narayan"]]
question_key=list((question.keys()))
question_value=list((question.values()))


# print(question_key)
# print(question_value)

score=0
print("----Select the best option----".center(100))
for x in range(0,len(question_key)):
    print(question_key[x])
    for k in range(0,len(option[x])):
        print(k+1,option[x][k])
    ans=int(input("Select your answer: "))
    if option[x][ans-1]==question_value[x]:
        print("\n\nCongratulations !!! Correct answer".title().center(50))
        score+=50
        print(f"Your current Score is {score}".center(50),"\n\n")
    else:
        print("Incorrect answer !!! better luck next time".center(50).title())
        if(score>0):
            score-=30
        print(f"Your current score is {score} ".center(50),"\n\n")

if(score>100):
    print(f"huge congratulations you have earned {score} points. Hope to see you next time".center(50).title())
else:
    print(f"Congrats for wining {score} points. Prepare well for next time".center(50).title())