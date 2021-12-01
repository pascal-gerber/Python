import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import keyboard
import threading


class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        
        
        
        #---------------------adding browser-------------------
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        self.setCentralWidget(self.browser)
        #-------------------full screen mode------------------
        self.showMaximized()
        #----------------------navbar-------------------------
        navbar = QToolBar()
        self.addToolBar(navbar)
        #-----------------prev Button-----------------
        prevBtn = QAction('Prev',self)
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)
        #-----------------next Button---------------
        nextBtn = QAction('Next',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)
        #-----------refresh Button--------------------
        refreshBtn = QAction('Refresh',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)
        #-----------home button----------------------
        homeBtn = QAction('Proxy',self)
        #when triggered call home method
        homeBtn.triggered.connect(self.proxy)
        navbar.addAction(homeBtn)
        #---------------------search bar---------------------------------
        searchBtn = QAction('Browse',self)
        searchBtn.triggered.connect(self.duckduckgo)
        navbar.addAction(searchBtn)
        
        self.add_new_tab(QUrl('https://duckduckgo.com/'), 'Homepage')
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        
        navbar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)

    def linkClicked(url):
        print("test")
        webbrowser.open(str(url.toString()))
        self.connect(web, SIGNAL("linkClicked (const QUrl&)"), linkClicked) 

    def add_new_tab(self, qurl = None, label ="Blank"):
        if qurl is None:
            qurl = QUrl('https://duckduckgo.com/')
            
    def duckduckgo(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        
    def proxy(self):
        self.browser.setUrl(QUrl('https://proxyscrape.com/web-proxy'))
        
    def loadUrl(self):
        url = self.searchBar.text()
        print(url)
        self.browser.setUrl(QUrl(url))
        
    def updateUrl(self, url):
        print(url)
        self.searchBar.setText(url.toString())
        
MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Pybrowser')
window = Window()
MyApp.exec_()
