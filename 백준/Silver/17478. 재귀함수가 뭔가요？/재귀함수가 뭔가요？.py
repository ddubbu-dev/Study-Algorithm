
INDENT_KEYWORD = "____"

PROFESSOR_N_STUDENT_MENT = [
    "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.",
    '"재귀함수가 뭔가요?"',
    # (HERE) STORY_MENT 재귀 필요함
    # CLOSE_MENT 마무리 필요
]

CLOSE_MENT = "라고 답변하였지."


# Q. indent 앞에 어떻게 넣어줌? 우선 함수로 처리함
def print_story_body_with_indent(times):
    print(f'{INDENT_KEYWORD*times}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print(f'{INDENT_KEYWORD*times}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print(f'{INDENT_KEYWORD*times}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    print(f'{INDENT_KEYWORD*(times+1)}"재귀함수가 뭔가요?"')

STORY_CLOSE_MENT = f'"재귀함수는 자기 자신을 호출하는 함수라네"'


T = int(input())


def tell_story(times):

    print_story_body_with_indent(times)

    if times + 1 == T:  # 탈출
        print(f"{INDENT_KEYWORD*(times+1)}{STORY_CLOSE_MENT}")
        print(f"{INDENT_KEYWORD*(times+1)}{CLOSE_MENT}")
        return

    tell_story(times + 1)
    
    # 본문 다 말하고, CLOSE_MENT 언급 필요함
    print(f"{INDENT_KEYWORD*(times+1)}{CLOSE_MENT}")


for line in PROFESSOR_N_STUDENT_MENT:
    print(line)

tell_story(0)

print(CLOSE_MENT)
