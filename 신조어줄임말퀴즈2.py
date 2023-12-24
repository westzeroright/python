print("Python 신조어/줄임말 퀴즈에 오신 것을 환영합니다!")

questions = ["취존", "솔까말", "케바케"]
answers = ["취향 존중", "솔직히 까놓고 말해서", "케이스 바이 케이스"]

correct_count = 0

for i in range(len(questions)):
    user_answer = input(f"{i + 1}. {questions[i]}이 어떤 문장의 줄임말인가요? ")

    if user_answer == answers[i]:
        print("정답")
        correct_count += 1
    else:
        print("오답")

print(f"3개 퀴즈 중 {correct_count}개 정답")
