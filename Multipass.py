# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Multipass.ui'
#
# Created: Tue Feb 04 23:58:25 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Multipass(object):
    def setupUi(self, Multipass):
        Multipass.setObjectName(_fromUtf8("Multipass"))
        Multipass.resize(465, 281)
        self.widget = QtGui.QWidget(Multipass)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.ascii85 = QtGui.QRadioButton(self.widget)
        self.ascii85.setGeometry(QtCore.QRect(230, 160, 82, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.ascii85.setFont(font)
        self.ascii85.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ascii85.setChecked(True)
        self.ascii85.setObjectName(_fromUtf8("ascii85"))
        self.base64 = QtGui.QRadioButton(self.widget)
        self.base64.setGeometry(QtCore.QRect(350, 160, 82, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.base64.setFont(font)
        self.base64.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.base64.setObjectName(_fromUtf8("base64"))
        self.username = QtGui.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(20, 40, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.username.setObjectName(_fromUtf8("username"))
        self.domain = QtGui.QLineEdit(self.widget)
        self.domain.setGeometry(QtCore.QRect(210, 40, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.domain.setFont(font)
        self.domain.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.domain.setObjectName(_fromUtf8("domain"))
        self.master_password = QtGui.QLineEdit(self.widget)
        self.master_password.setGeometry(QtCore.QRect(20, 110, 411, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.master_password.setFont(font)
        self.master_password.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.master_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.master_password.setEchoMode(QtGui.QLineEdit.Password)
        self.master_password.setObjectName(_fromUtf8("master_password"))
        self.selected_size = QtGui.QSlider(self.widget)
        self.selected_size.setGeometry(QtCore.QRect(90, 220, 341, 20))
        self.selected_size.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.selected_size.setMinimum(8)
        self.selected_size.setMaximum(40)
        self.selected_size.setOrientation(QtCore.Qt.Horizontal)
        self.selected_size.setObjectName(_fromUtf8("selected_size"))
        self.username_label = QtGui.QLabel(self.widget)
        self.username_label.setGeometry(QtCore.QRect(20, 16, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.username_label.setFont(font)
        self.username_label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.username_label.setObjectName(_fromUtf8("username_label"))
        self.domain_label = QtGui.QLabel(self.widget)
        self.domain_label.setGeometry(QtCore.QRect(210, 16, 161, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.domain_label.setFont(font)
        self.domain_label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.domain_label.setObjectName(_fromUtf8("domain_label"))
        self.masterPass_label = QtGui.QLabel(self.widget)
        self.masterPass_label.setGeometry(QtCore.QRect(20, 86, 351, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.masterPass_label.setFont(font)
        self.masterPass_label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.masterPass_label.setObjectName(_fromUtf8("masterPass_label"))
        self.generatedPass_label = QtGui.QLabel(self.widget)
        self.generatedPass_label.setGeometry(QtCore.QRect(20, 160, 181, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.generatedPass_label.setFont(font)
        self.generatedPass_label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.generatedPass_label.setObjectName(_fromUtf8("generatedPass_label"))
        self.length_label = QtGui.QLabel(self.widget)
        self.length_label.setGeometry(QtCore.QRect(20, 220, 71, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.length_label.setFont(font)
        self.length_label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.length_label.setObjectName(_fromUtf8("length_label"))
        self.generated_password = QtGui.QTextBrowser(self.widget)
        self.generated_password.setGeometry(QtCore.QRect(20, 180, 411, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        self.generated_password.setFont(font)
        self.generated_password.setObjectName(_fromUtf8("generated_password"))
        Multipass.setCentralWidget(self.widget)
        self.menubar = QtGui.QMenuBar(Multipass)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Multipass.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Multipass)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Multipass.setStatusBar(self.statusbar)

        self.retranslateUi(Multipass)
        QtCore.QObject.connect(self.username, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Multipass.generatePassword)
        QtCore.QObject.connect(self.domain, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Multipass.generatePassword)
        QtCore.QObject.connect(self.master_password, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Multipass.generatePassword)
        QtCore.QObject.connect(self.ascii85, QtCore.SIGNAL(_fromUtf8("clicked()")), Multipass.generatePassword)
        QtCore.QObject.connect(self.base64, QtCore.SIGNAL(_fromUtf8("clicked()")), Multipass.generatePassword)
        QtCore.QObject.connect(self.selected_size, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), Multipass.generatePassword)
        QtCore.QMetaObject.connectSlotsByName(Multipass)

    def retranslateUi(self, Multipass):
        Multipass.setWindowTitle(_translate("Multipass", "MainWindow", None))
        self.ascii85.setText(_translate("Multipass", "Ascii85", None))
        self.base64.setText(_translate("Multipass", "Base64", None))
        self.username_label.setText(_translate("Multipass", "Username:", None))
        self.domain_label.setText(_translate("Multipass", "Domain:", None))
        self.masterPass_label.setText(_translate("Multipass", "Master Password:", None))
        self.generatedPass_label.setText(_translate("Multipass", "Generated Password:", None))
        self.length_label.setText(_translate("Multipass", "Length:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Multipass = QtGui.QMainWindow()
    ui = Ui_Multipass()
    ui.setupUi(Multipass)
    Multipass.show()
    sys.exit(app.exec_())

