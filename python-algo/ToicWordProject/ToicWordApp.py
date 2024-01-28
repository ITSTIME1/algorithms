import sys
import requests
import time
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QLabel, QDesktopWidget, QAction, qApp
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal


# 인터넷 체크
class InternetChecker(QThread):
    internet_status_signal = pyqtSignal(bool)
    def run(self):
        while True:
            try:
                response = requests.get("https://www.google.com", timeout=5)
                internet_status = response.status_code == 200
            except requests.ConnectionError:
                internet_status = False
            self.internet_status_signal.emit(internet_status)
            time.sleep(30)  # Sleep for 60 seconds (1 minute)

class ToicWordApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_internet_connect = False
        self.connect_count = 0
        self.initUI()
        
    def createMenuBar(self):
        # 종료
        exitAction = QAction('종료', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('프로그램 종료')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()  
        
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
        self.createWordLayout(central_widget)
    
    
    def createWordLayout(self, central_widget):
        self.result_label = QLabel("Failed Internet Connection." if not self.is_internet_connect else "Successful Internet Connection.")
        self.result_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        central_widget.setLayout(layout)

    def createStatusBar(self):
        self.statusBar().showMessage('Connecting...')  # 상태
            
    def initUI(self):
        # 1. 인터넷 연결 확인
        # self.checkInternetConnection()
        self.createLayout()
        self.setWindowTitle("ToicWordApplication")
        self.createMenuBar()  # 메뉴바
        self.createStatusBar() # 상태바
        self.setGeometry(300, 300, 800, 600)  # 창의 크기, x, y, width, height
        self.adjustCenterScreen()
        self.show()
        
        # Start the internet checker thread
        self.internet_checker = InternetChecker(self)
        self.internet_checker.internet_status_signal.connect(self.handleInternetStatus)
        self.internet_checker.start()

    def handleInternetStatus(self, status):
        self.is_internet_connect = status
        if status:
            self.result_label.setText("Successful Internet Connection.")    
            self.connect_count = 0
            self.statusBar().showMessage("Successful Internet Connection.")
        else:
            self.result_label.setText("Failed Internet Connection.")
            print(f"1분뒤 자동으로 인터넷 연결을 시도 하겠습니다. ( 시도횟수 {self.connect_count} )")
            self.connect_count += 1
            self.statusBar().showMessage("Failed Internet Connection.")
        
# 메인이 진입점이니까
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    ex = ToicWordApp()
    sys.exit(app.exec_())
