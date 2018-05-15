import time

import requests
from flask import Flask, request, jsonify


class studyPlanner:
    def __init__(self):
        fh = open('hourlog.txt', 'r')
        fc = open('chapterlog.txt', 'r')
        self.numberHours = int(fh.read(1))
        self.numberChapters = int(fc.read(1))
        fh.close()
        fc.close()

    def addHr(self, numberOfHours):
        # numberOfHours = int(input("How many Hours to add?"))
        self.numberHours += numberOfHours
        # self.display()
        with open("hourlog.txt", 'a', encoding='utf-8') as f:
            f.write("Hour Studied:- {}\n".format(self.numberHours))
            f.write("Time: {}\n\n".format(
                time.strftime('%H:%M%p %Z on %b %d, %Y')))
        with open('hourlog.txt', 'r') as original:
            data = original.read()
        with open('hourlog.txt', 'w') as modified:
            modified.write(str(self.numberHours) + "\n" + data)

    def addChapter(self, numberOfChapters):
        # numberOfChapters = int(input("How many Chapters to add?"))
        self.numberChapters += numberOfChapters
        # self.display()
        with open("chapterlog.txt", 'a', encoding='utf-8') as f:
            f.write("Chapter Done:- {}\n".format(self.numberChapters))
            f.write("Time: {}\n\n".format(
                time.strftime('%H:%M%p %Z on %b %d, %Y')))
        with open('chapterlog.txt', 'r') as original:
            data = original.read()
        with open('chapterlog.txt', 'w') as modified:
            modified.write(str(self.numberHours) + "\n" + data)

    # def display(self):
    #     print('No. of hrs = {}'.format(self.numberHours))
    #     print('No. of chapters = {}'.format(self.numberChapters))
    #     print(time.strftime('%H:%M%p %Z on %b %d, %Y'))
    #     print("  ")

    # def rest(self):
    #     if(self.numberHours >= 4):
    #         print("You can take a break")
    #     else:
    #         print("No Shit!!")
    #         self.display()


app = Flask(__name__)

StudyPlanner = studyPlanner()


@app.route('/display', methods=['GET'])
def Api_display():
    response = {
        'no. of hours': StudyPlanner.numberHours,
        'no. of chapters': StudyPlanner.numberChapters
    }
    return jsonify(response), 200


@app.route('/add/hours', methods=['POST'])
def Api_addHours():
    values = request.get_json()
    numberAdd = int(values['#'])
    StudyPlanner.addHr(numberAdd)
    response = {'message': f'Added {numberAdd} hours'}
    return jsonify(response), 201


@app.route('/add/chapters', methods=['POST'])
def Api_addChapters():
    values = request.get_json()
    numberAdd = int(values['#'])
    StudyPlanner.addChapter(numberAdd)
    response = {'message': f'Added {numberAdd} chapters'}
    return jsonify(response), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
