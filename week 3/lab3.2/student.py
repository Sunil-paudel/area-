class Student(object):
    def __init__(self, name, number):
        #There are 2 under score before and after init
        """Constructor creates a Student with the given name
        and number of scores and sets all scores to 0."""
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)
    def setName(self, name):
        self._name = name
    def getName(self): #Return the student's name.
        return self._name

    def setScore(self, i, score): #Set the ith score.
        self._scores[i - 1] = score

    def getScore(self, i):  #Return the ith score.
        return self._scores[i - 1]

    def getAverage(self): #Returns the average scores.
        return sum(self._scores) / len(self._scores)

    def getHighScore(self): #Returns the highest score.
        return max(self._scores)

    def __str__(self): #There are 2 under score before and after str
     #Returns the string representation of the student
        return "Name:" + self._name + "\nScores: " + \
               " ".join(map(str, self._scores))



