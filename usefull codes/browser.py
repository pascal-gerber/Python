import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar()
        self.addToolBar(navbar)
        prevBtn = QAction('Prev',self)
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)
        nextBtn = QAction('Next',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)
        refreshBtn = QAction('Refresh',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)
        homeBtn = QAction('Home',self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)
    def home(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))
    def updateUrl(self, url):
        self.searchBar.setText(url.toString())
MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Pybrowser')
window = Window()
MyApp.exec_()
