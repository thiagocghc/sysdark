# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_material_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QRegularExpression)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tela_cadastro = QPushButton(self.frame)
        self.btn_tela_cadastro.setObjectName(u"btn_tela_cadastro")

        self.horizontalLayout.addWidget(self.btn_tela_cadastro)

        self.btn_vendas = QPushButton(self.frame)
        self.btn_vendas.setObjectName(u"btn_vendas")

        self.horizontalLayout.addWidget(self.btn_vendas)

        self.btn_relatorio = QPushButton(self.frame)
        self.btn_relatorio.setObjectName(u"btn_relatorio")

        self.horizontalLayout.addWidget(self.btn_relatorio)

        self.btn_sair = QPushButton(self.frame)
        self.btn_sair.setObjectName(u"btn_sair")

        self.horizontalLayout.addWidget(self.btn_sair)


        self.verticalLayout_2.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_cad = QWidget()
        self.page_cad.setObjectName(u"page_cad")
        self.verticalLayout = QVBoxLayout(self.page_cad)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_cad)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.page_cad)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.input_nome = QLineEdit(self.page_cad)
        self.input_nome.setObjectName(u"input_nome")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.input_nome)

        self.label_3 = QLabel(self.page_cad)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.input_fone = QLineEdit(self.page_cad)
        self.input_fone.setObjectName(u"input_fone")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.input_fone)

        self.label_4 = QLabel(self.page_cad)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.input_email = QLineEdit(self.page_cad)
        self.input_email.setObjectName(u"input_email")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.input_email)

        self.label_5 = QLabel(self.page_cad)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.input_endereco = QLineEdit(self.page_cad)
        self.input_endereco.setObjectName(u"input_endereco")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.input_endereco)

        self.label_6 = QLabel(self.page_cad)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.input_cidade = QLineEdit(self.page_cad)
        self.input_cidade.setObjectName(u"input_cidade")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.input_cidade)

        self.label_7 = QLabel(self.page_cad)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.combo_estado = QComboBox(self.page_cad)
        self.combo_estado.addItem("")
        self.combo_estado.addItem("")
        self.combo_estado.addItem("")
        self.combo_estado.addItem("")
        self.combo_estado.addItem("")
        self.combo_estado.addItem("")
        self.combo_estado.setObjectName(u"combo_estado")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.combo_estado)

        self.label_8 = QLabel(self.page_cad)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.input_cnpj = QLineEdit(self.page_cad)
        self.input_cnpj.setObjectName(u"input_cnpj")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.input_cnpj)


        self.verticalLayout.addLayout(self.formLayout)

        self.stackedWidget.addWidget(self.page_cad)
        self.page_relatorio = QWidget()
        self.page_relatorio.setObjectName(u"page_relatorio")
        self.verticalLayout_5 = QVBoxLayout(self.page_relatorio)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.page_relatorio)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_relatorio = QLabel(self.frame_4)
        self.label_relatorio.setObjectName(u"label_relatorio")

        self.verticalLayout_4.addWidget(self.label_relatorio)

        self.input_filtrar = QLineEdit(self.frame_4)
        self.input_filtrar.setObjectName(u"input_filtrar")

        self.verticalLayout_4.addWidget(self.input_filtrar)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.table_relatorio = QTableWidget(self.page_relatorio)
        if (self.table_relatorio.columnCount() < 8):
            self.table_relatorio.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_relatorio.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_relatorio.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_relatorio.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_relatorio.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_relatorio.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_relatorio.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_relatorio.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_relatorio.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.table_relatorio.setObjectName(u"table_relatorio")
        self.table_relatorio.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_3.addWidget(self.table_relatorio)

        self.frame_3 = QFrame(self.page_relatorio)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_editar = QPushButton(self.frame_3)
        self.btn_editar.setObjectName(u"btn_editar")

        self.verticalLayout_3.addWidget(self.btn_editar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")

        self.verticalLayout_3.addWidget(self.btn_excluir)

        self.btn_exportar = QPushButton(self.frame_3)
        self.btn_exportar.setObjectName(u"btn_exportar")

        self.verticalLayout_3.addWidget(self.btn_exportar)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_relatorio)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_cancelar = QPushButton(self.frame_2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.horizontalLayout_2.addWidget(self.btn_cancelar)

        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")

        self.horizontalLayout_2.addWidget(self.btn_cadastrar)


        self.verticalLayout_2.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        #################################
        #VALIDATOR
        self.validaCep = QRegularExpression("[0-9]{5}-[0-9]{3}")
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_tela_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRO", None))
        self.btn_vendas.setText(QCoreApplication.translate("MainWindow", u"VENDAS", None))
        self.btn_relatorio.setText(QCoreApplication.translate("MainWindow", u"RELAT\u00d3RIO", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">SYS DARK MODE</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ENDERECO", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ESTADO", None))
        self.combo_estado.setItemText(0, QCoreApplication.translate("MainWindow", u"MATO GROSSO DO SUL", None))
        self.combo_estado.setItemText(1, QCoreApplication.translate("MainWindow", u"RIO GRANDE DO SUL", None))
        self.combo_estado.setItemText(2, QCoreApplication.translate("MainWindow", u"S\u00c3O PAULO", None))
        self.combo_estado.setItemText(3, QCoreApplication.translate("MainWindow", u"RIO DE JANEIRO", None))
        self.combo_estado.setItemText(4, QCoreApplication.translate("MainWindow", u"MINAS GERAIS", None))
        self.combo_estado.setItemText(5, QCoreApplication.translate("MainWindow", u"BAHIA", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.input_cnpj.setInputMask(QCoreApplication.translate("MainWindow", u"00.000.000/0000-00", None))
        self.label_relatorio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">SYSDARK MODE</span></p></body></html>", None))
        self.input_filtrar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtrar cadastro: digite o NOME ou CNPJ do cliente", None))
        ___qtablewidgetitem = self.table_relatorio.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_relatorio.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem2 = self.table_relatorio.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem3 = self.table_relatorio.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"FONE", None));
        ___qtablewidgetitem4 = self.table_relatorio.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem5 = self.table_relatorio.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ENDERECO", None));
        ___qtablewidgetitem6 = self.table_relatorio.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        ___qtablewidgetitem7 = self.table_relatorio.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        self.btn_editar.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.btn_exportar.setText(QCoreApplication.translate("MainWindow", u"EXPORTAR", None))
        self.btn_cancelar.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
    # retranslateUi

