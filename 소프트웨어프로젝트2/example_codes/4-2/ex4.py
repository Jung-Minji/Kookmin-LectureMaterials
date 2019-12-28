import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid) # QGridLayout 인스턴스가 만들어져 응용 프로그램 창의 레이아웃으로 설정된다.

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]
        print(positions)

        for position, name in zip(positions, names):    #버튼을 생성하고 배치하는 과정
            if name == '':
                continue
            button = QPushButton(name)      # 버튼의 이름을 주면 버튼이 만들어진다.
            print(*position)
            grid.addWidget(button, *position)   # (0,0)에다가 cls(버튼)을 박는다.    # * : 위치를 나타내는 문법적인 표현

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

