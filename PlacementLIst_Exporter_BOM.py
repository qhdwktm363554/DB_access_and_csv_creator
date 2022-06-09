# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '01_line_selection.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymssql, os
import pandas as pd
import math

class Ui_Bong_1st_win(object):
    def setupUi(self, Bong_1st_win):
        Bong_1st_win.setObjectName("Bong_1st_win")
        Bong_1st_win.resize(600, 750)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Bong_1st_win.setFont(font)
        Bong_1st_win.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Bong_1st_win)
        font = QtGui.QFont()
        font.setFamily("72")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("background-color: rgb(97, 97, 97);\n"
"font: italic 10pt \"72\";")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 551, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BS1_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BS1_BUTTON.setStyleSheet("background-color: rgb(251, 239, 255);")
        self.BS1_BUTTON.setObjectName("BS1_BUTTON")
        self.BS1_BUTTON.clicked.connect(self.goto2nd_page_from_BS1)
        # self.line = self.BS1_BUTTON.text()
        self.verticalLayout.addWidget(self.BS1_BUTTON)
        self.BS2_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BS2_BUTTON.setStyleSheet("background-color: rgb(251, 239, 255);")
        self.BS2_BUTTON.setObjectName("BS2_BUTTON")
        self.BS2_BUTTON.clicked.connect(self.goto2nd_page_from_BS2)
        self.verticalLayout.addWidget(self.BS2_BUTTON)
        self.BS3_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BS3_BUTTON.setStyleSheet("background-color: rgb(251, 239, 255);")
        self.BS3_BUTTON.setObjectName("BS3_BUTTON")
        self.BS3_BUTTON.clicked.connect(self.goto2nd_page_from_BS3)
        self.verticalLayout.addWidget(self.BS3_BUTTON)
        self.BS4_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BS4_BUTTON.setStyleSheet("background-color: rgb(251, 239, 255);")
        self.BS4_BUTTON.setObjectName("BS4_BUTTON")
        self.BS4_BUTTON.clicked.connect(self.goto2nd_page_from_BS4)
        self.verticalLayout.addWidget(self.BS4_BUTTON)
        self.BS5_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BS5_BUTTON.setStyleSheet("background-color: rgb(251, 239, 255);")
        self.BS5_BUTTON.setObjectName("BS5_BUTTON")
        self.BS5_BUTTON.clicked.connect(self.goto2nd_page_from_BS5)
        self.verticalLayout.addWidget(self.BS5_BUTTON)
        self.ES1_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ES1_BUTTON.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.ES1_BUTTON.setObjectName("ES1_BUTTON")
        self.ES1_BUTTON.clicked.connect(self.goto2nd_page_from_ES1)
        self.verticalLayout.addWidget(self.ES1_BUTTON)
        self.ES2_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ES2_BUTTON.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.ES2_BUTTON.setObjectName("ES2_BUTTON")
        self.ES2_BUTTON.clicked.connect(self.goto2nd_page_from_ES2)
        self.verticalLayout.addWidget(self.ES2_BUTTON)
        self.ES3_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ES3_BUTTON.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.ES3_BUTTON.setObjectName("ES3_BUTTON")
        self.ES3_BUTTON.clicked.connect(self.goto2nd_page_from_ES3)
        self.verticalLayout.addWidget(self.ES3_BUTTON)
        self.ES4_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ES4_BUTTON.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.ES4_BUTTON.setObjectName("ES4_BUTTON")
        self.ES4_BUTTON.clicked.connect(self.goto2nd_page_from_ES4)
        self.verticalLayout.addWidget(self.ES4_BUTTON)
        self.ES5_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ES5_BUTTON.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.ES5_BUTTON.setObjectName("ES5_BUTTON")
        self.ES5_BUTTON.clicked.connect(self.goto2nd_page_from_ES5)
        self.verticalLayout.addWidget(self.ES5_BUTTON)
        self.TR_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.TR_BUTTON.setStyleSheet("background-color: rgb(188, 229, 255);")
        self.TR_BUTTON.setObjectName("TR_BUTTON")
        self.TR_BUTTON.clicked.connect(self.goto2nd_page_from_TR)
        self.verticalLayout.addWidget(self.TR_BUTTON)
        self.ECC1_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ECC1_BUTTON.setStyleSheet("background-color: rgb(145, 163, 195);")
        self.ECC1_BUTTON.setObjectName("ECC1_BUTTON")
        self.ECC1_BUTTON.clicked.connect(self.goto2nd_page_from_ECC1)
        self.verticalLayout.addWidget(self.ECC1_BUTTON)
        self.ECC2_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ECC2_BUTTON.setStyleSheet("background-color: rgb(145, 163, 195);")
        self.ECC2_BUTTON.setObjectName("ECC2_BUTTON")
        self.ECC2_BUTTON.clicked.connect(self.goto2nd_page_from_ECC2)
        self.verticalLayout.addWidget(self.ECC2_BUTTON)
        self.ECC3_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ECC3_BUTTON.setStyleSheet("background-color: rgb(145, 163, 195);")
        self.ECC3_BUTTON.setObjectName("ECC3_BUTTON")
        self.ECC3_BUTTON.clicked.connect(self.goto2nd_page_from_ECC3)
        self.verticalLayout.addWidget(self.ECC3_BUTTON)
        self.OSIS_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.OSIS_BUTTON.setStyleSheet("background-color: rgb(145, 163, 195);")
        self.OSIS_BUTTON.setObjectName("OSIS_BUTTON")
        self.OSIS_BUTTON.clicked.connect(self.goto2nd_page_from_OSIS)
        self.verticalLayout.addWidget(self.OSIS_BUTTON)
        self.AS_BUTTON = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.AS_BUTTON.setStyleSheet("background-color: rgb(145, 163, 195);")
        self.AS_BUTTON.setObjectName("AS_BUTTON")
        self.AS_BUTTON.clicked.connect(self.goto2nd_page_from_AS)
        self.verticalLayout.addWidget(self.AS_BUTTON)
        Bong_1st_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Bong_1st_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        Bong_1st_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Bong_1st_win)
        self.statusbar.setObjectName("statusbar")
        Bong_1st_win.setStatusBar(self.statusbar)

        self.retranslateUi(Bong_1st_win)
        QtCore.QMetaObject.connectSlotsByName(Bong_1st_win)

    def goto2nd_page_from_BS1(self): 
        global line
        line = self.BS1_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_BS2(self): 
        global line
        line = self.BS2_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_BS3(self): 
        global line
        line = self.BS3_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_BS4(self): 
        global line
        line = self.BS4_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_BS5(self): 
        global line
        line = self.BS5_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_ES1(self): 
        global line
        line = self.ES1_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_ES2(self): 
        global line
        line = self.ES2_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_ES3(self): 
        global line
        line = self.ES3_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_ES4(self): 
        global line
        line = self.ES4_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_ES5(self): 
        global line
        line = self.ES5_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_TR(self): 
        global line
        line = self.TR_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_ECC1(self): 
        global line
        line = self.ECC1_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()
    def goto2nd_page_from_ECC2(self): 
        global line
        line = self.ECC2_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show() 
    def goto2nd_page_from_ECC3(self): 
        global line
        line = self.ECC3_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show() 
    def goto2nd_page_from_OSIS(self): 
        global line
        line = self.OSIS_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show() 
    def goto2nd_page_from_AS(self): 
        global line
        line = self.AS_BUTTON.text() 
        print("line {} is selected".format(line))           
        Ui_Bong_2nd_win()
        Bong_2nd_win.show()     

    def retranslateUi(self, Bong_1st_win):
        _translate = QtCore.QCoreApplication.translate
        Bong_1st_win.setWindowTitle(_translate("Bong_1st_win", "Line selection [BOM]"))
        self.BS1_BUTTON.setText(_translate("Bong_1st_win", "BS1"))
        self.BS2_BUTTON.setText(_translate("Bong_1st_win", "BS2"))
        self.BS3_BUTTON.setText(_translate("Bong_1st_win", "BS3"))
        self.BS4_BUTTON.setText(_translate("Bong_1st_win", "BS4"))
        self.BS5_BUTTON.setText(_translate("Bong_1st_win", "BS5"))
        self.ES1_BUTTON.setText(_translate("Bong_1st_win", "ES1"))
        self.ES2_BUTTON.setText(_translate("Bong_1st_win", "ES2"))
        self.ES3_BUTTON.setText(_translate("Bong_1st_win", "ES3"))
        self.ES4_BUTTON.setText(_translate("Bong_1st_win", "ES4"))
        self.ES5_BUTTON.setText(_translate("Bong_1st_win", "ES5"))
        self.TR_BUTTON.setText(_translate("Bong_1st_win", "TR"))
        self.ECC1_BUTTON.setText(_translate("Bong_1st_win", "ECC1"))
        self.ECC2_BUTTON.setText(_translate("Bong_1st_win", "ECC2"))
        self.ECC3_BUTTON.setText(_translate("Bong_1st_win", "ECC3"))
        self.OSIS_BUTTON.setText(_translate("Bong_1st_win", "OSIS"))
        self.AS_BUTTON.setText(_translate("Bong_1st_win", "AS"))



class Ui_Bong_2nd_win(Ui_Bong_1st_win):
    def __init__(self, parent = Ui_Bong_1st_win):
        super().__init__()
    
    def setupUi_2(self, Bong_2nd_win):
        Bong_2nd_win.setObjectName("Bong_2nd_win")
        Bong_2nd_win.resize(573, 510)
        Bong_2nd_win.setStyleSheet("background-color: rgb(167, 167, 167);")
        self.Final_dir_input = QtWidgets.QLineEdit(Bong_2nd_win)
        self.Final_dir_input.setGeometry(QtCore.QRect(50, 130, 301, 31))
        self.Final_dir_input.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.Final_dir_input.setObjectName("Final_dir_input")
        self.label = QtWidgets.QLabel(Bong_2nd_win)
        self.label.setGeometry(QtCore.QRect(50, 90, 431, 41))
        font = QtGui.QFont()
        font.setFamily("72")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Bong_2nd_win)
        self.label_2.setGeometry(QtCore.QRect(50, 180, 101, 21))
        font = QtGui.QFont()
        font.setFamily("72")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"72\";")
        self.label_2.setObjectName("label_2")
        
        self.DIR_BUTTON = QtWidgets.QPushButton(Bong_2nd_win)
        self.DIR_BUTTON.setGeometry(QtCore.QRect(360, 130, 161, 31))
        self.DIR_BUTTON.setStyleSheet("color: rgb(254, 254, 254);\n"
"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: italic 12pt \"72\";")
        self.DIR_BUTTON.setObjectName("DIR_BUTTON")
        self.label_3 = QtWidgets.QLabel(Bong_2nd_win)
        self.label_3.setGeometry(QtCore.QRect(50, 220, 130, 21))
        font = QtGui.QFont()
        font.setFamily("72")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"72\";")
        self.label_3.setObjectName("label_3")

        self.label_line = QtWidgets.QLabel(Bong_2nd_win)
        self.label_line.setGeometry(QtCore.QRect(200, 170, 300, 40))
        self.label_line.setObjectName("label_line")
        self.label_dir = QtWidgets.QLabel(Bong_2nd_win)
        self.label_dir.setGeometry(QtCore.QRect(200, 210, 300, 40))
        self.label_dir.setObjectName("label_dir")
        # self.label_remark = QtWidgets.QLabel(Bong_2nd_win)
        # self.label_remark.setGeometry(QtCore.QRect(95, 35, 400, 40))
        # self.label_remark.setObjectName("label_remark")

        self.retranslateUi(Bong_2nd_win)
        QtCore.QMetaObject.connectSlotsByName(Bong_2nd_win)

        self.DIR_BUTTON.clicked.connect(self.on_clicked)
    
    def on_clicked(self):
        self.label_dir.setText(self.Final_dir_input.text())
        self.label_line.setText(line)

        self.SUBMIT_BUTTON = QtWidgets.QPushButton(Bong_2nd_win)
        self.SUBMIT_BUTTON.setGeometry(QtCore.QRect(50, 260, 471, 201))
        font = QtGui.QFont()
        font.setFamily("72")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.SUBMIT_BUTTON.setFont(font)
        self.SUBMIT_BUTTON.setText("SUBMIT")
        self.SUBMIT_BUTTON.setStyleSheet("background-color: rgb(23, 21, 27);\n"
"color: rgb(252, 252, 252);\n"
"\n"
"font: 맑은 고딕 13pt \"75\";")
        self.SUBMIT_BUTTON.setObjectName("SUBMIT_BUTTON")
        self.SUBMIT_BUTTON.show()
        self.SUBMIT_BUTTON.clicked.connect(self.submit)

        font1 = QtGui.QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.label_line.setFont(font1)
        self.label_dir.setFont(font1)
    
    def submit(self):
        print(self.Final_dir_input.text())
        server_df = pd.read_excel("00_LINE_HOST_TABLE.xlsx")

        line_name = line
        final_directory = self.Final_dir_input.text()
        host_name = server_df.loc[server_df["LINE"] == line_name,"HOST"]
        #DB 정보
        server = host_name.values[0]  # host_name이 object 형태로 값을 return 해서 value 값만 추출한거다. .item() 이것도 동일
        username = 'sa'
        password = 'Siplace%Sa.1.Pwd'
        database = 'SIPLACEPro'

        #RECIPE 이름 추출
        CURRENT_DIR = os.getcwd()
        list = os.path.join(CURRENT_DIR,'00_BOM_LIST.xlsx')
        df = pd.read_excel(list)
        # final_directory = "IBU1.0_NSMK"

        for i in df['MLFB'].index:
            # recipe_name과 final_directory 입력
            recipe_name = df.loc[i, 'MLFB']

            sql_query1 = 'SELECT DISTINCT f.ObjectName, d.ObjectName, b.bstrRefDesignator,b.dOffsetX, b.dOffsetY, b.dAngle, b.bOmit FROM CPanel a\n\t\tLeft Outer Join CComponentPlacement as b ON a.spPlacementListRef = b.PID\n\t\tLeft Outer Join CComponent as c ON b.spComponentRef = c.OID\n\t\tLeft Outer Join AliasName as d ON c.OID = d.PID\n\t\tLeft Outer Join CFolder as e ON d.FolderID = e.OID\n\t\tLeft Outer Join AliasName as f ON a.spPlacementListRef = f.PID\nWHERE a.PID in (SELECT spPanelMatrix FROM CPanelLink WHERE PID IN (SELECT  a.PID FROM AliasName a LEFT OUTER JOIN CFolder b ON a.FolderID = b.OID WHERE a.ObjectName = \'A2C_PART#\' and b.bstrDisplayName= \'DIRECTORY\')) ORDER BY b.bstrRefDesignator'
            sql_query2 = sql_query1.replace("A2C_PART#", recipe_name)
            sql_query = sql_query2.replace("DIRECTORY", final_directory)

                # mssql 접속하고 connection으로부터 cursor를 생성
            cnxn = pymssql.connect(server, username, password, database)
            curs = cnxn.cursor()
                # sql문 실행문
            curs.execute(sql_query)
            row = curs.fetchall()
                # dataframe column 이름 설정
            Column_names = ['SMD#', 'Part#', 'Ref#', 'x', 'y', 'angle', 'omit']
            df2 = pd.DataFrame(row, columns=Column_names)
            df2['Angle_degree'] = df2['angle'] * 180/math.pi
            df2 = df2[['SMD#', 'Part#', 'Ref#', 'x', 'y', 'Angle_degree', 'omit']]        #이건 BOM 비교용
            # df2 = df2[['Ref#', 'Part#', 'x', 'y', 'Angle_degree', 'omit']]                  # 이건 AOI 용
            # omitted = df2.loc[df2['omit'] == True, 'omit'].index                            # 이것도 AOI 용
            # df2.drop(omitted, inplace=True)                                                 # 이것도 AOI 용

            cnxn.close()
            if df2.empty:
                print(recipe_name + " is EMPTY")
                break
            else:
                print("recipe_"+recipe_name+" is completed")
                df2.to_csv(recipe_name + ".csv", index=False, header=False)
        print("END")


    def retranslateUi(self, Bong_2nd_win):
        _translate = QtCore.QCoreApplication.translate
        Bong_2nd_win.setWindowTitle(_translate("Bong_2nd_win", "Final directory input [BOM]"))
        self.label.setText(_translate("Bong_2nd_win", "Final directory on SIPLACE RECIPE"))
        self.label_2.setText(_translate("Bong_2nd_win", "Line                   "))
        # self.SUBMIT_BUTTON.setText(_translate("Bong_2nd_win", "Submit"))
        self.DIR_BUTTON.setText(_translate("Bong_2nd_win", "OK"))
        self.label_3.setText(_translate("Bong_2nd_win", "Final directory"))
        self.label_dir.setText(_translate("Bong_2nd_win", ""))
        self.label_line.setText(_translate("Bong_2nd_win", ""))
        # self.label_remark.setText(_translate("Bong_2nd_win", "**** Warning: 'Omitted component' will be deleted ****"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bong_1st_win = QtWidgets.QMainWindow()
    ui = Ui_Bong_1st_win()
    ui.setupUi(Bong_1st_win)
    Bong_1st_win.show()

    #두번째 페이지 돌려주는 LOOP
    Bong_2nd_win = QtWidgets.QDialog()
    ui2 = Ui_Bong_2nd_win()
    ui2.setupUi_2(Bong_2nd_win)

    Bong_1st_win.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
