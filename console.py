from typing import Text
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import mysql.connector
import mysql.connector.errors

numero_id = 0
# conexões com o banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="dbcashier")
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
    edt_doc = frm_lancamentos.edt_doc.text()
    data = frm_lancamentos.dateEdit.text()
    edt_desc1 = frm_lancamentos.edt_desc1.text()
    edt_desc2 = frm_lancamentos.edt_desc2.text()
    box_tipo = frm_lancamentos.box_tipo
    edt_valor = frm_lancamentos.edt_valor.text()

def inerir_lanc_tablewidget():
    numcols = frm_lancamentos.tableWidget.columnCount()
    numrows = frm_lancamentos.tableWidget.rowCount()
    frm_lancamentos.tableWidget.setRowCount(numrows)
    frm_lancamentos.tableWidget.setColumnCount(numcols)
    frm_lancamentos.tableWidget.setItem(numrows -1,0,QTableWidgetItem(edt_doc))
    frm_lancamentos.tableWidget.setItem(numrows -1,1,QTableWidgetItem(data))
    frm_lancamentos.tableWidget.setItem(numrows -1,2,QTableWidgetItem(edt_desc1))
    frm_lancamentos.tableWidget.setItem(numrows -1,3,QTableWidgetItem(edt_desc2))
    frm_lancamentos.tableWidget.setItem(numrows -1,4,QTableWidgetItem(str(box_tipo)))
    frm_lancamentos.tableWidget.setItem(numrows -1,5,QTableWidgetItem(edt_valor))


def exclir_lancamento():
    linhalanc = frm_lancamentos.tableWidget.currentRow()
    frm_lancamentos.tableWidget.removeRow(linhalanc)

    cursor = banco.cursor()
    cursor.execute("SELECT idcliente FROM tblcliente")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linhalanc][0]
    cursor.execute("DELETE FROM tbllancamento WHERE idlanc="+str(valor_id))
def salvar_lancamento():
    global numero_id
    
    #comando mysql para inserir dados no banco
    cursor = banco.cursor()
    comando_SQL_id = "SELECT id FROM tbllancamento"
    cursor.execute(comando_SQL_id)
    numero_id = cursor.fetchall()

    if not idlanc == numero_id:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO tblproduto (codico, descricao, grupo, fabricante, unidade, pcound, pcovenda, markup) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dados = (str(linhaCod), str(linhaDesc), str(linhaGrupo), str(linhaFab), str(linhaUnd), str(linhaPrecocomp), str(linhaprecovenda), str(linhamarkup))
        cursor.execute(comando_SQL,dados)
        banco.commit()
    else:
        cursor = banco.cursor()
        cursor.execute ("UPDATE tblproduto SET codico ='{}', descricao ='{}', grupo ='{}', fabricante ='{}', unidade ='{}',pcound ='{}', pcovenda ='{}', markup ='{}' WHERE id {}".format(linhaCod, linhaDesc, linhaGrupo, linhaFab, linhaUnd, linhaPrecocomp, linhaprecovenda, linhamarkup, numero_id))
        banco.commit()
def editar_lancamento():
    global numero_id
    linha = frm_principal.tableWidget.currentRow()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM tbllancamento"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM tbllancamento WHERE idlanc="+str(valor_id))
    produto = cursor.fetchall()
    frm_lancamentos.show()

    frm_lancamentos.line_ean.setText(str(produto[0][0])) #campo codico
    frm_lancamentos.line_descricao.setText(str(produto[0][1])) #campo descrição 
    frm_lancamentos.line_grupo.setText(str(produto[0][2])) #campo grupo
    frm_lancamentos.line_fabric.setText(str(produto[0][3])) #campo fabricante 
    frm_lancamentos.line_tipo_und.setText(str(produto[0][4])) #campo undade
    frm_lancamentos.precounid.setText(str(produto[0][5])) #campo preço por unidade
    frm_lancamentos.precovenda.setText(str(produto[0][6])) #campo preço de venda
    frm_lancamentos.markup.textsetText(str(produto[0][7])) #campo margem de lucro
    
    numero_id = valor_id
def excluir_lancamento_total():
    pass  
def chama_lancamento():
    frm_lancamentos.show()
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
    # botões da tela principal
    frm_principal.btn_editar.clicked.connect(editar_lancamento)
    frm_principal.btn_excluir.clicked.connect(excluir_lancamento_total)
    frm_principal.btn_lancar.clicked.connect(chama_lancamento)
    # botões da tela lançamentos
    frm_lancamentos.btn_inserir.clicked.connect(inserir_lancamento)
    frm_lancamentos.btn_excluir.clicked.connect(exclir_lancamento)
    frm_lancamentos.btn_salvar.clicked.connect(salvar_lancamento)
    
    
    frm_login.show()
    app.exec()