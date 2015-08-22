#encoding:utf-8
import requests
import json
from PyQt4 import QtGui, QtCore

UpdateAPIURL = 'https://api.misskey.xyz/status/update'
TimeLineAPIURL = 'https://api.misskey.xyz/rest/status/timeline'
userkey = 
appkey = 
keys = {'sauth-app-key': appkey,'sauth-user-key': userkey ,'Content-Type': 'application/x-www-form-urlencoded'}
class MissPyMain(QtGui.QWidget):

    def __init__(self):
        super(MissPyMain,self).__init__()
        self.initUI()

    def initUI(self): 
        self.setWindowTitle('MissPy')
        self.UpdateText = QtGui.QTextEdit(self)
        self.UpdateText.move(0,650)
        self.UpdateButton = QtGui.QPushButton('update',self)
        self.UpdateButton.move(260,777)
        self.UpdateButton.clicked.connect(self.doUpdate)
        self.setGeometry(50, 50, 800,800)
        
    def doUpdate(self):
        self.updatetxt = ''
        self.updatetxt = {'text': '' + self.UpdateText.toPlainText()}
        r = requests.post(UpdateAPIURL,headers=keys,data=self.updatetxt)
        print(r.text)

    def getTimeLine(self):
        r = requests.get(TimeLineAPIURL,headers=keys)   

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MissPyMain()
    window.show()
    sys.exit(app.exec_())