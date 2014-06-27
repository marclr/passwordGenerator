'''
Created on 03/02/2014

@author: Marc Lopez Roca
@version: 0.8

Conversio d'interficie a py: pyuic4 -x Multipass.ui -o Multipass.py
'''

# -*- coding: utf-8 -*-
import sys, hashlib, base64
from PyQt4 import QtGui
from Multipass import Ui_Multipass

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Multipass()
        self.ui.setupUi(self)

    
    def generatePassword(self):
        #Take de parameters
        username = str(self.ui.username.text())
        domain = str(self.ui.domain.text())
        master_password = str(self.ui.master_password.text())
        
        #Check if any is empty
        if username == "" or domain == "" or master_password =="":
            self.ui.generated_password.setText("Please, complete all fields");
        else:
            text = username +':'+ domain + '@' + master_password
            gen = hashlib.sha256(text)
            text_cod = gen.hexdigest()
            
            
            if self.ui.ascii85.isChecked():
                #print "ASCI85"#:J3Y'P6M
                text_cod = ascii85(text_cod)
            else:
                #print "BASE64"#omKEW8js
                text_cod = base64(text_cod)
            value = self.ui.selected_size.value()
            text_cod = text_cod[:value]
            self.ui.generated_password.setText("")
            self.ui.generated_password.setText(text_cod)
            
   
def base64(string):
    #===========================================================================
    # base = ""
    # table = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    #          "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    #          "0","1","2","3","4","5","6","7","8","9",
    #          "+","/"]
    # string = str(string[0:-4]) #Delete two bytes, and we have a string of 60 bytes
    # for x in xrange(10):
    #     word = string[x*6:x*6+6]
    #     print word
    #     value = bin(int(word, 16))[2:].zfill(24)
    #     print value
    #     decimal = int(value,2)
    #     print decimal
    #     for y in xrange(0,4):
    #         base = base + table[decimal%64]
    #         decimal= decimal // 64
    #         ####
    #         #decimal = value[y:y+6]
    #         #print "\t"+decimal+" :"+table[ int(decimal,2)]
    #         #decimal = int(decimal,2)
    #         #base = base + table[decimal]
    #         
    #===========================================================================
    string = str(string[0:-4]) #Delete two bytes, and we have a string of 60 bytes
    import base64
    s = base64.b64encode(string)
    return s

'''
@see: http://tenminutetutor.com/binary-encoding/ascii85-encoding
'''
def ascii85(string):
    #Hex string of length 64
    ascii85 = ""
    for x in xrange(8):
        word = string[x*8:x*8+8]
        value = int(word,16)
        for y in xrange(5):
            ascii85 = ascii85 + chr(33+(value%85))
            value = value//85
    return ascii85        
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())