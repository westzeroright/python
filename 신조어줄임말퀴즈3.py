print("Python 신조어/줄임말 퀴즈에 오신 것을 환영합니다!")

quizzes = {
    "취존" : "취향 존중",
    "솔까말" : "솔직히 까놓고 말해서",
    "케바케" : "케이스 바이 케이스" }

correct_count = 0

for quiz, answer in quizzes.items():
    user_answer = input(f"{quiz}이 어떤 문장의 줄임말인가요? ")

    if user_answer == answer:
        print("정답")
        correct_count += 1
    else:
        print("오답")

print(f"{len(quizzes)}개 퀴즈 중 {correct_count}개 정답")
