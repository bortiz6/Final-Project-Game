import chapter1 #brings in all code from chapter1 -- ANY loose lines of code in that module will be run!
import chapter2
import chapter3
import chapter4
import chapter5

def grettings():
    chapter1.greetings() #ask for user name and greets them

def start():
    chapter1.greetings() #ask for user name and greets them
    chapter1.chapter_1() #calls the start() chapter
    chapter2.chapter_2()
    chapter3.chapter_3()
    chapter4.chapter_4()
    chapter5.chapter_5()


   

    


if __name__ == '__main__':#any code in this if statement will ONLY run if the file you pressed the play button on is THIS file
    #importing Start from any other file you are running will NOT call this if statement!
    start()
