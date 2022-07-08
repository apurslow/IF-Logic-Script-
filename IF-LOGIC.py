#!/usr/bin/env python3
import time
#question prompts 
questionSets ={"You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "You walk into a bar. What is the first thing you are most likely to do?":{"1. Order an ale, ask about quests.":"Lawful Good","2. Order cheesecake and milk":"Chaotic Good","3. Steal someone's drink and frame someone for it":"Chaotic Evil","4. Order an apple cider":"Lawful Evil"},
                "You are traveling to another town and on the road an injured man runs up to you and asks for your help with bandits ahead. What do you do?":{"1. Answer the mans call for aid":"Lawful Good","2. Hand the man a banana and tell him everything will be ok":"Chaotic Good","3. Demand to be paid by the man and then brutalize the bandits":"Chaotic Evil","4. Mind control the man and use him as bait for the bandits":"Lawful Evil"},
                "2You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "3You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "4You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "5You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "6You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "7You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "8You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "9You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "01You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "02You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "03You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "04You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "05You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "06You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "07You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "08You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "09You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"},
                "000You come across a rabbit while wandering in the woods. What are you most likely to do?":{"1. Kill it for food":"Lawful Good","2. Try and pet it":"Chaotic Good","3. Send it to the shadow realm":"Chaotic Evil","4. Use to trap goblins":"Lawful Evil"}
}

alignment ={"Lawful Good":0,"Chaotic Good":0,"Lawful Evil":0,"Chaotic Evil":0}

def initialPrompt():
    print("DnD Alignment quiz!")
    time.sleep(0.5)
    print("Use this quiz to get an idea about your player character's alignment!")
    time.sleep(0.5)
    print("Only enter the corresponding question's number when answering.")
    time.sleep(0.5)
    print("Quiz starting....")
    time.sleep(1)

def handleInput():
    global alignment
    try:
        theInput = input()
        if theInput!= "1" and theInput!= "2" and theInput!= "3" and theInput!= "4":
            print("wrong input received. Only enter the digit 1, 2, 3, or 4")
            handleInput()
        if theInput== "1":
            alignment["Lawful Good"]+=1
        elif theInput== "2":
            alignment["Chaotic Good"]+=1
        elif theInput== "3":
            alignment["Lawful Evil"]+=1
        elif theInput== "4":
            alignment["Chaotic Evil"]+=1
    except:
        print("you broke this shit somehow")

def promptQuestions(questions):

    for x in questions:
        time.sleep(0.5)
        print(x)
        for y in questions[x]:
            print(y)
        handleInput()
        print()
    print("Questions finished calculating score....")
    time.sleep(1)

def calculateAlignment(alignment):
    #assumption of 20 total questions
    #arbitrary calculation could be adjusted
    lawfulGood = alignment["Lawful Good"]
    lawfulEvil = alignment["Lawful Evil"]
    ChaoticGood = alignment["Chaotic Good"]
    ChaoticEvil = alignment["Chaotic Evil"]

    if lawfulGood + lawfulEvil > 11:
        if lawfulGood - lawfulEvil > 2:
            print("You align more closely with Lawful Good")
        elif lawfulEvil - lawfulGood > 2:
            print("You align more closely with Lawful Evil")
        else:
            print("You align more closely with Lawful neutral")
    elif ChaoticEvil + ChaoticGood > 11:
        if ChaoticEvil - ChaoticGood > 2:
            print("You align more closely with Chaotic Good")
        elif ChaoticGood - ChaoticEvil > 2:
            print("You align more closely with Chaotic Evil")
        else:
            print("You align more closely with Chaotic neutral")
    elif ChaoticEvil + lawfulEvil > 11:
        if ChaoticEvil - lawfulEvil > 2:
            print("You align more closely with Chaotic Evil")
        elif lawfulEvil - ChaoticEvil > 2:
            print("You align more closely with Lawful Evil")
        else:
            print("You align more closely with Neutral Evil")
    elif ChaoticGood + lawfulGood > 11:
        if ChaoticGood - lawfulGood > 2:
            print("You align more closely with Chaotic Evil")
        elif lawfulGood - ChaoticGood > 2:
            print("You align more closely with Lawful Evil")
        else:
            print("You align more closely with Neutral Evil")
    else:
        print("You align more closely with True Neutral")

initialPrompt()
promptQuestions(questionSets)
calculateAlignment(alignment)
