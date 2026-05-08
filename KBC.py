# KAUN BANEGA CROREPATI:>

question = [
    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

    ["which language was used to create this project?","python","jawa","SQL","jason","None",4],

]

level = [1000,2000,3000,5000,10000,20000,30000,50000,100000,200000,300000,500000,1000000]

for i in range(0,len(question)):
    print("Question for $",level[i])
    print(question[i][0])
    print("1.",question[i][1])
    print("2.",question[i][2])
    print("3.",question[i][3])
    print("4.",question[i][4])
    answer = int(input("Enter your answer: "))
    if answer == question[i][5]:
        print("Correct! You have won $",level[i])
    else:
        print("Wrong! You have lost all your money.")
        break