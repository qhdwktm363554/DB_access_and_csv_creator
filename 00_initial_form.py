import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QMainWindow, QAction, QMenu

#event 처리하기 위해서
from PyQt5.QtCore import QCoreApplication

#QMainWindow class를 상속받아서 class를 만든다.
class Exam (QMainWindow):
    def __init__(self):
        #상위객체를 생성한다.
        super().__init__()
        #이제 함수를 만들어 내가 할 일을 넣어준다.
        self.initUI()
    def initUI(self):
        #상태표시줄을 생성
        self.statusBar()
        #한번 더 호출하면 상태표시줄 객체를 생성
        self.statusBar().showMessage("HI_bong")

        #menu를 만들어보자. 우선 menu 생성
        menu = self.menuBar()
        #아래는 menu group을 생성
        menu_file = menu.addMenu('File')
        menu_edit = menu.addMenu('edit')

        file_exit = QAction('Exit', self)   #Menu 객체를 생성한다.
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 영원히 빠이")
        new_txt = QAction("txt file", self)
        new_py = QAction("python file", self)

        file_exit.triggered.connect(QCoreApplication.instance().quit)


        file_new = QMenu('New', self)       #sub group을 추가

        file_new.addAction(new_txt)         #sub menu를 추가
        file_new.addAction(new_py)

        menu_file.addMenu(file_new)         #주 menu 추가
        menu_file.addAction(file_exit)      #menu 등록

        #아래의 self는 나 자신에 button을 추가한다.
        btn = QPushButton('BS1', self)
        #sizeHint()는 위 글씨를 기준으로 적당히 조절한다.
        btn.setToolTip('let us get <b>placememt list from Pro<b/>')
        btn.resize(btn.sizeHint())
        btn.move(20,30)
        #button을 눌렀을 때 event 처리
        btn.clicked.connect(QCoreApplication.instance().quit)


        self.setGeometry(300,300,400,500)
        self.setWindowTitle('To get placement list')

        #보여줘야 한다.
        self.show()

    #창의 x를 눌렀을 때 이벤트 처리
    def closeEvent(self, QCloseEvent):
        #ans로 QMessageBox의 상수값을 받는다.
        ans = QMessageBox.question(self, "종료 확인", "진짜 종료할거야?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

#main code를 작성한다.

#모든 Qt5 object는 Application object를 생성하고 시작해야 한다.
#sys.argv는 python이 shell에서 실행하면 명령줄로 인수를 하는데 그 부분을 제어하는 거다..?
app = QApplication(sys.argv)
w = Exam()

#program을 종료하고 결과를 return
#app.exec_()는 event 처리를 위한 loop를 실행하는 것. main loop인 app.exec_()가 끝난 다음에 sys.exit로 종료한다.
sys.exit(app.exec_())