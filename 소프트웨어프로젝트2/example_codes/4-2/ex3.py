import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()    # 수평적인 박스(수평 정렬)
        hbox.addStretch(1)      # 자기 앞에 있는 공간을 늘린다. 우측으로 밀려난다.
        hbox.addWidget(okButton)    # 버튼을 추가한다.
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()       # 수직적 박스 (수직 정렬)
        vbox.addStretch(1)         # 위에 빈공간을 만든다.
        vbox.addLayout(hbox)


        self.setLayout(vbox)       # 이 상황(vbox가 hbox를 가지고 있는 상황)을 나의 레이아웃으로 결정하겠다.

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

