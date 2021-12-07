from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import mysql.connector.errors

numero_id = 0
# conexões com o banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="dbstore")
def funcao_login():
    #frm_login.lineuser.setText("")
    nome_user =frm_login.lineuser.text()
    key = frm_login.linekey.text()
    
    cursor2 = banco.cursor()
    comando_sql = "SELECT senha FROM tbllogin WHERE login ='{}'".format(nome_user)
    cursor2.execute(comando_sql)
    #nome = cursor2.fetchall()
    senha_db = cursor2.fetchall()
    #print(nome, senha_db)
    if key == senha_db[0][0] : #nome[0][1] == nome_user and
        frm_login.close()
        frm_principal.show()
    else:
        #frm_login.close()
        QMessageBox.about(frm_login, "Erro", "Usuário ou senha invalido!")       
# funções da tela de cadastro Usuário
def cadastrousuario():
    linhanome = frm_caduser.lineNome.text() #campo Nome
    linhauser = frm_caduser.lineUser.text() #campo Usuário
    linhakey = frm_caduser.lineKey.text() #campo senha
    #comando mysql para inserir dados no banco
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO tbllogin (nome, login, senha) VALUES (%s,%s,%s)"
    dados = (str(linhanome),str(linhauser),str(linhakey))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    frm_caduser.lineNome.setText('')
    frm_caduser.lineUser.setText('')
    frm_caduser.lineKey.setText('')
def funcao_cancela():
    frm_login.close()
def inserir_lancamento():
    rowPosition = frm_lancamentos.tableWidget.rowCount()
    frm_lancamentos.tableWidget.insertRow(rowPosition)
    idprod = frm_lancamentos.line_idprod.text()
    line_descprod = frm_lancamentos.line_descprod.text()
    quant = frm_lancamentos.edt_quant.text()
    valorund = frm_lancamentos.edt_valorund.text()
    porsdesc = frm_lancamentos.edt_porsdesc.text()
    valordesc = frm_lancamentos.edt_valordesc.text()
    numcols = frm_lancamentos.tableWidget.columnCount()
    numrows = frm_lancamentos.tableWidget.rowCount()
    frm_lancamentos.tableWidget.setRowCount(numrows)
    frm_lancamentos.tableWidget.setColumnCount(numcols)
    frm_lancamentos.tableWidget.setItem(numrows -1,0,QtGui.QTableWidgetItem(idprod))
    frm_lancamentos.tableWidget.setItem(numrows -1,1,QtGui.QTableWidgetItem(line_descprod))
    frm_lancamentos.tableWidget.setItem(numrows -1,2,QtGui.QTableWidgetItem(quant))
    frm_lancamentos.tableWidget.setItem(numrows -1,3,QtGui.QTableWidgetItem(valorund))
    frm_lancamentos.tableWidget.setItem(numrows -1,4,QtGui.QTableWidgetItem(porsdesc))
    frm_lancamentos.tableWidget.setItem(numrows -1,5,QtGui.QTableWidgetItem(valordesc))


if __name__ == "__main__":
    # chamando as telas
    app = QtWidgets.QApplication([])
    frm_login = uic.loadUi(r'.\forms\frm_login.ui')
    frm_caduser = uic.loadUi(r'.\forms\frm_caduser.ui')
    frm_principal = uic.loadUi(r'.\forms\frm_principal.ui')
    frm_lancamentos = uic.loadUi(r'.\forms\frm_lancamentos.ui')

    # botões da tela login
    frm_login.linekey.setEchoMode(QtWidgets.QLineEdit.Password)
    frm_login.btnlogin.clicked.connect(funcao_login)
    frm_login.btnexit.clicked.connect(funcao_cancela)
    

    frm_login.show()
    app.exec()