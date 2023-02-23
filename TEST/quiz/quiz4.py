class Word:
    def __init__(self,word,ex1,ex2,answer):
        self.word=word
        self.ex1=ex1
        self.ex2=ex2
        self.answer=answer
    def show_question(self):
        print(f"\"{self.word}\"의 뜻은?")
        print("1. "+self.ex1)
        print("2. " + self.ex2)

    def check_answer(self,user_input):
        if user_input==self.answer:
            print("정답입니다.")
        else:
            print("오답입니다.")

word = Word("얼죽아","얼어 죽어도 아메리카노","얼굴만은 죽어도 아기피부",1)
word.show_question()
word.check_answer(int(input("=> ")))