#include <ncurses.h>
#include <iostream>
#include <clocale>
#include <locale.h>
#include <unistd.h>
#include <vector>
#include <stdio.h>
#include <termios.h>
#include <unistd.h>
#include <fcntl.h>
using namespace std;

int kbhit(void)
{
  struct termios oldt, newt;
  int ch;
  int oldf;

  tcgetattr(STDIN_FILENO, &oldt);
  newt = oldt;
  newt.c_lflag &= ~(ICANON | ECHO);
  tcsetattr(STDIN_FILENO, TCSANOW, &newt);
  oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
  fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);

  ch = getchar();

  tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
  fcntl(STDIN_FILENO, F_SETFL, oldf);

  if(ch != EOF)
  {
    ungetc(ch, stdin);
    return 1;
  }

  return 0;
}

int headDirection[4][2] = {
  {0, -1}, {0, 1}, {-2, 0}, {2, 0}
};  // snake head가 움직이는 방향; 위, 아래, 왼, 오

class Snake{
  vector <int> xPos;
  vector <int> yPos;

public:
  void setX(int x){
    xPos.push_back(x);
  }

  void setY(int y){
    yPos.push_back(y);
  }

  int getX(){
    return xPos.back();
  }

  int getY(){
    return yPos.back();
  }

  void removeX(){
    xPos.pop_back();
  }

  void removeY(){
    yPos.pop_back();
  }
  //
  void moveSnakeHead(int& xPos, int& yPos, int direction){
    int currentX = xPos;
    int currentY = yPos;
    int newXPos, newYPos;
    mvprintw(xPos, yPos,"  ");  // 이동 전 snake 지움
    removeX();
    removeY();
    mvprintw(currentX, currentY,"  ");
    newXPos = currentX + headDirection[direction][0];
    newYPos = currentY + headDirection[direction][1];
    setX(newXPos);
    setY(newYPos);
    mvprintw(newXPos, newYPos, "+");
  }

  int setHeadDirection(int inputKey){
    int setDirect;
    switch (inputKey) {
      case 72:
        setDirect = 0;
        break;

      case 80:
        setDirect = 1;
        break;

      case 75:
        setDirect = 2;
        break;

      case 77:
        setDirect = 3;
        break;

      default:
        break;
    }
    return setDirect;
  }

};
int main(){
  initscr();
  //keypad(stdscr, TRUE);  // 키보드 입력 설정
  start_color();
  //curs_set(0);  // 커서 지우기
  noecho();  // 입력한 키 값을 화면에 보이지 않기
  init_pair(1, COLOR_RED, COLOR_WHITE);
  setlocale(LC_CTYPE, "ko_KR.utf-8");
  attron(COLOR_PAIR(1));

  Snake snake;
  setlocale(LC_ALL, "");
  snake.setX(10);
  snake.setY(15); // 초기 snake의 위치 지정
  snake.setX(11);
  snake.setY(15);
  snake.setX(12);
  snake.setY(15);
  mvprintw(snake.getX(), snake.getY(),"+"); // 화면에 ■ □ 인쇄
  attroff(COLOR_PAIR(1));

  //int inputKey;
  int preInputKey = KEY_LEFT;
  int currentHead = 2;
  int dir;
  int curX, curY;
  int inputKey;
  /* << 키보드의 입력에 따라 snake 위치 이동 >>
  // 1. 키보드의 입력에 따라 입력 전 위치를 벡터에서 삭제하고 이동한 위치의 값을 벡터에 추가한다
  // 2. 화면에 이동 전 snake를 지우기 위해 입력 전 위치에 공백을 두 번 출력한다
  */
  while (true){
    if(kbhit()){
      do { inputKey = getch();} while(inputKey == 224);
      }
      sleep(100);

    }
    switch (inputKey) {
      case 72:
      case 80:
      case 75:
      case 77:
      if((dir==75&&inputKey!=77)||(dir==77&&inputKey!=75)||(dir==72&&inputKey!=80)||
(dir==80&&inputKey!=72))//180회전이동을 방지하기 위해 필요.
          dir=inputKey;
      inputKey=0; // 키값을 저장하는 함수를 reset
      break;
    }
    curX = snake.getX();
    curY = snake.getY();
    snake.moveSnakeHead(curX, curY, dir);


    

  refresh();
  getch();
  endwin();
  return 0;
}
