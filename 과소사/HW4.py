# Tic-Tac-Toe 게임
# 학번 : 20191662
# 이름 : 정민지

import random
def game():
    board = [[' ' for x in range(3)] for y in range(3)]
    start = True
    while start:
        # 게임 보드 그리기
        for r in range(3):
            print("  " + board[r][0] + '|  ' + board[r][1] + "| " + board[r][2])
            if (r != 2):
                print("---|---|---")

        # 사용자로부터 좌표 입력을 받는다.
        x = int(input("다음 수의 x좌표를 입력하시오(0~2): "))
        y = int(input("다음 수의 y좌표를 입력하시오(0~2): "))

        # 사용자가 선택한 좌표 표시하기
        usr_done = False
        while not usr_done:
            if board[x][y] != " ":
                print("잘못된 위치입니다. 다시 입력하세요")
                x = int(input("다음 수의 x좌표를 입력하시오(0~2): "))
                y = int(input("다음 수의 y좌표를 입력하시오(0~2): "))

            else:
                board[x][y] = 'X'
                usr_done = True

        # 컴퓨터가 랜덤으로 좌표 고르기
        com_done = False
        com_x = random.randint(0, 2)
        com_y = random.randint(0, 2)

        while not com_done:
            if board[com_x][com_y] == " ":
                board[com_x][com_y] = 'O'
                com_done = True
            else:
                com_x = random.randint(0, 2)
                com_y = random.randint(0, 2)

        # 게임 종료
        # 좌 대각선 방향 빙고
        if board[0][0] == board[1][1] == board[2][2] == 'X':
            print("사용자가 이겼습니다!")
            start = False
        elif board[0][0] == board[1][1] == board[2][2] == 'O':
            print("컴퓨터가 이겼습니다.")
            start = False

        # 우 대각선 방향 빙고
        elif board[0][2] == board[1][1] == board[2][0] == 'X':
            print("사용자가 이겼습니다!")
            start = False
        elif board[0][2] == board[1][1] == board[2][0] == 'O':
            print("컴퓨터가 이겼습니다.")
            start = False

        # 정방향 빙고
        # else:
        #     for i in range(len(board)):
        # 가로
        elif board[0][0] == board[0][1] == board[0][2] == 'X':
            print("사용자가 이겼습니다!")
            start = False
        elif board[0][0] == board[0][1] == board[0][2] == 'O':
            print("컴퓨터가 이겼습니다.")
            start = False
        elif board[1][0] == board[1][1] == board[1][2] == 'X':
            print("사용자가 이겼습니다!")
            start = False
        elif board[1][0] == board[1][1] == board[1][2] == 'O':
            print("컴퓨터가 이겼습니다.")
            start = False
        elif board[2][0] == board[2][1] == board[2][2] == 'X':
            print("사용자가 이겼습니다!")
            start = False
        elif board[2][0] == board[2][1] == board[2][2] == 'O':
            print("컴퓨터가 이겼습니다.")
            start = False
        # 세로
        elif board[0][0] == board[1][0] == board[2][0] == 'X':
            print("사용자가 이겼습니다!")
            start = False
        elif board[0][0] == board[1][0] == board[2][0] == 'O':
                print("컴퓨터가 이겼습니다.")
                start = False
        elif board[0][1] == board[1][1] == board[2][1] == 'X':
            print("사용자가 이겼습니다!")
            start = False
        elif board[0][1] == board[1][1] == board[2][1] == 'O':
                print("컴퓨터가 이겼습니다.")
                start = False
        elif board[0][2] == board[1][2] == board[2][2] == 'X':
            print("사용자가 이겼습니다!")
            start = False
        elif board[0][2] == board[1][2] == board[2][2] == 'O':
                print("컴퓨터가 이겼습니다.")
                start = False
        # else:
        #     print("비겼습니다.")
        #     start = False

        # 게임이 끝난 후 다시 시작할지 결정
        user_check = False
        if not start:
            print("게임이 종료 되었습니다.")
            user_check = input("계속 진행하려면 start를, 종료하려면 quit를 입력하세요: ")

        if user_check == "start":
            start = True
            board = [[' ' for x in range(3)] for y in range(3)]

        elif user_check == "quit":
            start = False


if __name__ == '__main__':
    choice = 0
    while choice != 2:
        print("Tic-Tac-Toe 게임")
        print("1. 게임 시작")
        print("2. 게임 종료")

        choice = int(input("메뉴를 선택하세요: "))
        if choice == 1:
            game()


# 비기는 경우와 이겼을 경우 게임판이 나오지 않는 경우를 처리하지 못했습니다.
