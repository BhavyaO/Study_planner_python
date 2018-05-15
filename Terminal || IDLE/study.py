import time


class studyPlanner:
    def __init__(self):
        fh = open('hourlog.txt', 'r')
        fc = open('chapterlog.txt', 'r')
        self.numberHours = int(fh.read(1))
        self.numberChapters = int(fc.read(1))
        fh.close()
        fc.close()

    def addHr(self):
        numberOfHours = int(input("How many Hours to add?"))
        self.numberHours += numberOfHours
        self.display()
        with open("hourlog.txt", 'a', encoding='utf-8') as f:
            f.write("Hour Studied:- {}\n".format(self.numberHours))
            f.write("Time: {}\n\n".format(
                time.strftime('%H:%M%p %Z on %b %d, %Y')))
        with open('hourlog.txt', 'r') as original:
            data = original.read()
        with open('hourlog.txt', 'w') as modified:
            modified.write(str(self.numberHours) + "\n" + data)

    def addChapter(self):
        numberOfChapters = int(input("How many Chapters to add?"))
        self.numberChapters += numberOfChapters
        self.display()
        with open("chapterlog.txt", 'a', encoding='utf-8') as f:
            f.write("Chapter Done:- {}\n".format(self.numberChapters))
            f.write("Time: {}\n\n".format(
                time.strftime('%H:%M%p %Z on %b %d, %Y')))
        with open('chapterlog.txt', 'r') as original:
            data = original.read()
        with open('chapterlog.txt', 'w') as modified:
            modified.write(str(self.numberHours) + "\n" + data)

    def display(self):
        print('No. of hrs = {}'.format(self.numberHours))
        print('No. of chapters = {}'.format(self.numberChapters))
        print(time.strftime('%H:%M%p %Z on %b %d, %Y'))
        print("  ")

    def rest(self):
        if(self.numberHours >= 4):
            print("You can take a break")
        else:
            print("No Shit!!")
            self.display()


StudyPlanner = studyPlanner()


print("Welcome to the planner")

while(1):
    print('======================================')
    option = input("[1]Display\n[2]Add hr\n[3]Add chapter\n[4]Break?\n")
    print(option)
    if(option == '1'):
        StudyPlanner.display()
    elif(option == '2'):
        StudyPlanner.addHr()
    elif(option == '3'):
        StudyPlanner.addChapter()
    elif(option == '4'):
        StudyPlanner.rest()
    elif(option == '9'):
        exit
