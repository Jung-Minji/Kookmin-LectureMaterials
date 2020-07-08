import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()   # 사용자가 따로 메서드를 실행하지 않아도 자동적으로 메서드를 불러온다.

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)  #Label == print
        lbl1.move(15, 10)      # 절대 좌표 ; 좌표 위치가 정해져 있다, 레이블의 위치
                               # 실제 위치 : (315, 310)
        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)    # application의 위치와 크기 정함.
        self.setWindowTitle('Absolute')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()      # 내용을 만들고 있다.
    sys.exit(app.exec_())   # 이 프로그램을 나가고 exit해라.

