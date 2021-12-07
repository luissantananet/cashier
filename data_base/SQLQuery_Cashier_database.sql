# Criar Banco de Dados
create database dbcashier;
# Usar o Banco
use dbcashier;

create table tbllogin(
	idlogin int not null auto_increment,
    nome VARCHAR(100) not null,
    login VARCHAR(50) not null,
    senha VARCHAR(50) not null,
    primary key(idlogin)
);
create table tbllancamento(
	idlanc int not null auto_increment,
    doc varchar(20),
    datah date,
    descricao varchar(150),
    tipo varchar(10),
    valor decimal(8,2),
    primary key(idlanc)
);

-- --------------------------------------------------------
--  Inserido dados na tabelas
-- --------------------------------------------------------

insert into tbllogin(nome, login, senha) values('Administrador','adm','adm');