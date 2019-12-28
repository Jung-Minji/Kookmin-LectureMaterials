import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()


    # UI 생성 함수
    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        # 위젯 생성
        self.lbl_name = QLabel("Name: ")
        self.lbl_age = QLabel("Age: ")
        self.lbl_score = QLabel("Score: ")
        self.btn_add = QPushButton("Add")
        self.btn_del = QPushButton("Del")
        self.btn_find = QPushButton("Find")
        self.btn_inc = QPushButton("Inc")
        self.btn_show = QPushButton("show")
        self.lbl_amount = QLabel("Amount: ")
        self.lbl_key = QLabel("Key: ")
        self.lbl_result = QLabel("Result")
        self.txt_name = QLineEdit()
        self.txt_age = QLineEdit()
        self.txt_score = QLineEdit()
        self.txt_amount = QLineEdit()
        self.txt_result = QTextEdit()
        self.combo_key = QComboBox()

        # 수평 박스1
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.lbl_name)
        hbox1.addWidget(self.txt_name)
        hbox1.addWidget(self.lbl_age)
        hbox1.addWidget(self.txt_age)
        hbox1.addWidget(self.lbl_score)
        hbox1.addWidget(self.txt_score)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)

        # 수평 박스2
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)

        hbox2.addWidget(self.lbl_amount)
        hbox2.addWidget(self.txt_amount)
        hbox2.addWidget(self.lbl_key)
        hbox2.addWidget(self.combo_key)
        self.combo_key.addItem("Name")
        self.combo_key.addItem("Age")
        self.combo_key.addItem("Score")

        vbox.addLayout(hbox2)

        # 수평 박스3
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.btn_add)
        hbox3.addWidget(self.btn_del)
        hbox3.addWidget(self.btn_find)
        hbox3.addWidget(self.btn_inc)
        hbox3.addWidget(self.btn_show)
        vbox.addLayout(hbox3)

        vbox.addWidget(self.lbl_result)
        vbox.addWidget(self.txt_result)
        self.setLayout(vbox)

        # 각각의 버튼을 각각의 메서드(슬롯)와 연결한다.
        self.btn_add.clicked.connect(self.clicked_add)
        self.btn_del.clicked.connect(self.clicked_del)
        self.btn_find.clicked.connect(self.clicked_find)
        self.btn_inc.clicked.connect(self.clicked_inc)
        self.btn_show.clicked.connect(self.clicked_show)

        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    # 데이터 불러오기
    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.readScoreDB()
        for dic in self.scoredb:
            self.txt_result.append(str(dic))

    def clicked_add(self):
        add_dic = {'Name': self.txt_name.text(), 'Age': int(self.txt_age.text()), 'Score': int(self.txt_score.text())}
        self.scoredb.append(add_dic)
        self.writeScoreDB()
        self.txt_result.clear()
        self.showScoreDB()
        self.txt_name.clear()
        self.txt_age.clear()
        self.txt_score.clear()

    def clicked_del(self):
        self.readScoreDB()
        del_readScoreDB = []

        for dic in self.scoredb:
            if dic['Name'] != self.txt_name.text():
                del_readScoreDB.append(dic)

        self.scoredb = del_readScoreDB
        self.writeScoreDB()
        self.txt_result.clear()
        self.showScoreDB()

    def clicked_find(self):
        self.readScoreDB()
        self.txt_result.clear()
        for dic in self.scoredb:
            if dic['Name'] == self.txt_name.text():
                self.txt_result.append(str(dic))

    def clicked_inc(self):
        self.readScoreDB()
        for dic in self.scoredb:
            if dic['Name'] == self.txt_name.text():
                dic['Score'] += int(self.txt_amount.text())
        self.writeScoreDB()
        self.txt_result.clear()
        self.showScoreDB()

    def clicked_show(self):
        self.readScoreDB()
        sorted_scoredb = sorted(self.scoredb, key=lambda person: person[self.combo_key.currentText()])
        self.scoredb = sorted_scoredb
        self.txt_result.clear()
        for dic in self.scoredb:
            self.txt_result.append(str(dic))


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

