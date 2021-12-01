from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *
from PyQt4 import QtNetwork
from PyQt4 import QtGui
from PyQt4.QtGui import QGridLayout, QLineEdit, QWidget
import Tkinter, tkFileDialog
import sys
import os

class UrlInput(QLineEdit):

    def __init__(self, browser):

        super(UrlInput, self).__init__()
        self.browser = browser
        self.returnPressed.connect(self._return_pressed)
        self.browser.page().setForwardUnsupportedContent(True)
        self.browser.page().unsupportedContent.connect(self.download)
        self.manager = QtNetwork.QNetworkAccessManager()
        self.manager.finished.connect(self.finished)

    def _return_pressed(self):
        data = self.text()
        url = QUrl(data)
        browser.load(url)

    def download(self, reply):
        self.request = QtNetwork.QNetworkRequest(reply.url())
        self.reply = self.manager.get(self.request)

    def finished(self):
        filename = str(self.reply.url().path()).split('/')[-1]

        root = Tkinter.Tk()
        root.withdraw()

        dirname = tkFileDialog.askdirectory(parent=root,initialdir="/Desktop",title='You are downloading a file, please select a directory to place the file. Close the window to cancel')
        if dirname.strip() != '':
            dirname = dirname.replace('/','\\')
            f = open(dirname+'\\'+filename,'wb')
            f.write(str(self.reply.readAll()))
            f.close()
        else:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    grid = QGridLayout()
    browser = QWebView()
    url_input = UrlInput(browser)
    grid.addWidget(url_input, 1, 0)
    grid.addWidget(browser, 2, 0)
    main_frame = QWidget()
    main_frame.setLayout(grid)
    main_frame.show()
    sys.exit(app.exec_())
