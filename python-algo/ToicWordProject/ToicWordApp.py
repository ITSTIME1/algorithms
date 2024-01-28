import sys
import requests
import time
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QLabel, QDesktopWidget, QAction, qApp
from PyQt5.QtCore import Qt, QTimer

class ToicWordApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_internet_connect = False
        self.initUI()
        
    def tryInternetConnection(self):
        try:
            # Google의 서버에 요청을 보내 응답을 받음
            response = requests.get("https://www.google.com", timeout=5)
            if response.status_code == 200:
                self.is_internet_connect = True
                print("인터넷 연결 성공")
                ex.show()
                return True
        except requests.ConnectionError:
            self.is_internet_connect = False
            print("인터넷 연결 실패")
        return False
    
    def createMenuBar(self):
        # 종료
        exitAction = QAction('종료', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()  # Use self.menuBar() instead of menubar = self.menuBar()
        # 메뉴바라는 객체를 만들고, 아 아까는 이름이 중복되서 메소드랑.
        menubar.setNativeMenuBar(False)  # window와 동일한 환경을 갖추기 위해서
        settingMenu = menubar.addMenu('&설정')
        settingMenu.addAction(exitAction)
    
    # 화면 중앙.
    def adjustCenterScreen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    # 그리드 레이아웃 생성.
    def createLayout(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # 레이블 생성후 상단, 가운데
        self.result_label = QLabel("Test Label")
        self.result_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        central_widget.setLayout(layout)
    
    # def display_text(self):
    #     entered_text = self.text_edit.text()
    #     self.result_label.setText(f"Input Text : {entered_text}")
        
    def createStatusBar(self):
        self.statusBar().showMessage('Connecting...')  # 상태
        
    
    def checkInternetConnection(self):
        # 인터넷 연결 확인
        print("인터넷 연결을 확인합니다.")
        if self.tryInternetConnection():
            self.statusBar().showMessage("Successful Internet Connection.")
        else:
            self.statusBar().showMessage("Failed Internet Connection.")
            
    def initUI(self):
        self.createLayout()
        self.setWindowTitle("ToicWordApplication")
        self.createMenuBar()  # 메뉴바
        self.createStatusBar() # 상태바
        self.setGeometry(300, 300, 800, 600)  # 창의 크기, x, y, width, height
        self.adjustCenterScreen()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    ex = ToicWordApp()
    # QTimer를 사용하여 1분에 한 번씩 checkInternetConnection 함수 호출
    timer = QTimer(ex)
    timer.timeout.connect(ex.checkInternetConnection)
    timer.start(10000)  # 60000 밀리초 (1분)마다 timeout 시그널 발생
    sys.exit(app.exec_())
