class Question:
    def __init__(self , questionText , choices , answer):
        self.questionText = questionText
        self.choices = choices
        self.answer = answer

    def checkAnswer(self , answer):
        return self.answer == answer #soru cevabı verilen cevaba eşitse true döndür

class Quiz:
    def __init__(self , questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self): #indexe göre soruyu döndürüyor. 
        return self.questions[self.questionIndex]    

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}:{question.questionText}")

        for choice in question.choices:
            print("- " + choice)
        
        answer = input("Cevap:")
        self.guess(answer)
        self.loadQuestion()


    def guess(self, answer):
        question = self.getQuestion()

        if (question.checkAnswer(answer)):
            self.score += 1
        self.questionIndex += 1


    def loadQuestion(self) :
        if ( len(self.questions) == self.questionIndex ): # Bittiyse
            self.displayProgress()
            self.showScore()
        
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Skorunuz : {self.score} doğru , {len(self.questions) - self.score} yanlış . ")        

    def displayProgress(self): # ilerlemeyi göster
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1 

        if (questionNumber > totalQuestion):
            print("Quiz bitti !")
        else:
            print(f"    Soru {questionNumber} / {totalQuestion}     ".center(100,"*") )





q1 = Question("Türkiye'nin başkenti?" , ["Ankara","İstanbul","İzmir","Konya"] , "Ankara")
q2 = Question("Hangisi oop değildir ? " , ["Python","C","C#","Java"] , "C")


questions = [q1,q2]

quiz = Quiz(questions)

quiz.loadQuestion()
