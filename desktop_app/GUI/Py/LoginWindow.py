# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/UI/LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 677)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.authenticationField = QtWidgets.QGroupBox(self.centralwidget)
        self.authenticationField.setGeometry(QtCore.QRect(190, 150, 451, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authenticationField.sizePolicy().hasHeightForWidth())
        self.authenticationField.setSizePolicy(sizePolicy)
        self.authenticationField.setTitle("")
        self.authenticationField.setAlignment(QtCore.Qt.AlignCenter)
        self.authenticationField.setObjectName("authenticationField")
        self.label = QtWidgets.QLabel(self.authenticationField)
        self.label.setGeometry(QtCore.QRect(40, 20, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.loginEdit = QtWidgets.QLineEdit(self.authenticationField)
        self.loginEdit.setGeometry(QtCore.QRect(40, 50, 350, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginEdit.sizePolicy().hasHeightForWidth())
        self.loginEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.loginEdit.setFont(font)
        self.loginEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginEdit.setText("")
        self.loginEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.loginEdit.setObjectName("loginEdit")
        self.label_2 = QtWidgets.QLabel(self.authenticationField)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.passwordEdit = QtWidgets.QLineEdit(self.authenticationField)
        self.passwordEdit.setGeometry(QtCore.QRect(40, 150, 350, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase
            | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.forgotPasswordLabel = QtWidgets.QLabel(self.authenticationField)
        self.forgotPasswordLabel.setGeometry(QtCore.QRect(200, 120, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.forgotPasswordLabel.setFont(font)
        self.forgotPasswordLabel.setTextFormat(QtCore.Qt.RichText)
        self.forgotPasswordLabel.setOpenExternalLinks(True)
        self.forgotPasswordLabel.setObjectName("forgotPasswordLabel")
        self.pushButton = QtWidgets.QPushButton(self.authenticationField)
        self.pushButton.setGeometry(QtCore.QRect(40, 250, 350, 40))
        self.pushButton.setObjectName("pushButton")
        self.incorrectData = QtWidgets.QLabel(self.authenticationField)
        self.incorrectData.setGeometry(QtCore.QRect(90, 190, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.incorrectData.setFont(font)
        self.incorrectData.setText("")
        self.incorrectData.setObjectName("incorrectData")
        self.signUpLabel = QtWidgets.QLabel(self.authenticationField)
        self.signUpLabel.setGeometry(QtCore.QRect(310, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.signUpLabel.setFont(font)
        self.signUpLabel.setTextFormat(QtCore.Qt.RichText)
        self.signUpLabel.setOpenExternalLinks(True)
        self.signUpLabel.setObjectName("signUpLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WebForces client"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.forgotPasswordLabel.setText(_translate(
            "MainWindow", "<a href=\"http://localhost:8000/accounts/password_reset/\">Forgot password?</a>"))
        self.pushButton.setText(_translate("MainWindow", "Sign in for WebForces"))
        self.signUpLabel.setText(_translate(
            "MainWindow", "<a href=\"http://localhost:8000/accounts/sign_up/\">Sign up</a>"))
