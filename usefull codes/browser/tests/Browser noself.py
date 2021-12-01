import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

browser = QWebEngineView()
browser.setUrl(QUrl('https://duckduckgo.com/'))
setCentralWidget(browser)
#-------------------full screen mode------------------
showMaximized()

def createWidgets():
    super(browser)    
    #----------------------navbar-------------------------
    navbar = QToolBar(browser)
    addToolBar(navbar)
    #-----------------prev Button-----------------
    prevBtn = QAction(browser, 'Prev')
    prevBtn.triggered.connect(browser.back)
    navbar.addAction(prevBtn)
    #-----------------next Button---------------
    nextBtn = QAction('Next')
    nextBtn.triggered.connect(browser.forward)
    navbar.addAction(nextBtn)
    #-----------refresh Button--------------------
    refreshBtn = QAction('Refresh')
    refreshBtn.triggered.connect(browser.reload)
    navbar.addAction(refreshBtn)
    #-----------home button----------------------
    homeBtn = QAction('Proxy')
    #when triggered call home method
    homeBtn.triggered.connect(proxy)
    navbar.addAction(homeBtn)
    #---------------------search bar---------------------------------
    searchBtn = QAction('Browse',self)
    searchBtn.triggered.connect(duckduckgo)
    navbar.addAction(searchBtn)
        
    add_new_tab(QUrl('https://duckduckgo.com/'), 'Homepage')
    searchBar = QLineEdit()
    searchBar.returnPressed.connect(loadUrl)
        
    navbar.addWidget(searchBar)
    browser.urlChanged.connect(updateUrl)



def add_new_tab(qurl = None, label ="Blank"):
    if qurl is None:
        qurl = QUrl('https://duckduckgo.com/')
        
def duckduckgo():
    browser.setUrl(QUrl('https://duckduckgo.com/'))
        
def proxy():
    browser.setUrl(QUrl('https://proxyscrape.com/web-proxy'))
        
def loadUrl():
    url = searchBar.text()
    browser.setUrl(QUrl(url))
        
def updateUrl(url):
    searchBar.setText(url.toString())
        
MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Pybrowser')
window = Window(browser)
createWidgets()
MyApp.exec_()
