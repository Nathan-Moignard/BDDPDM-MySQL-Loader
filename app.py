from src.downloadSource import downloadSource
from src.mysql_loader import connectDB, importData
from mysql import  connector
from sys import stderr

class CIS_bdpm:
    tableName = 'CIS_bdpm'
    tableInit = 'CREATE TABLE CIS_bdpm (id INT UNIQUE AUTO_INCREMENT DEFAULT NULL, CIS INT PRIMARY KEY, Denomination VARCHAR(255), Forme VARCHAR(255), Administration VARCHAR(255), StatusAdm VARCHAR(255), ProcedureAut VARCHAR(255), DateCommercialisation VARCHAR(255), DateAMM VARCHAR(255), StatusBdm VARCHAR(255), Autorisation VARCHAR(255), Titulaires VARCHAR(255), Surveillance VARCHAR(255));'
    tableSchema = '(CIS, Denomination, Forme, Administration, StatusAdm, StatusAdm, DateCommercialisation, DateAMM, StatusBdm, Autorisation, Titulaires, Surveillance)'

class CIS_CIP_bdpm:
    tableName = 'CIS_CIP_bdpm'
    tableInit = 'CREATE TABLE CIS_CIP_bdpm (id INT UNIQUE AUTO_INCREMENT DEFAULT NULL, CIS INT PRIMARY KEY, CIP7 INT, Libelle VARCHAR(255), StatusAdm VARCHAR(255), EtatCommercialisation VARCHAR(255), DateCommercialisation VARCHAR(255), CIP13 BIGINT, AgrementCollectivites VARCHAR(255), TauxRemboursement VARCHAR(255), TBD1 TEXT, TBD2 TEXT, TBD3 TEXT, IndicationsRemboursement LONGTEXT);'
    tableSchema = '(CIS, CIP7, Libelle, StatusAdm, EtatCommercialisation, DateCommercialisation, CIP13, AgrementCollectivites, TauxRemboursement, TBD1, TBD2, TBD3, IndicationsRemboursement)'


class CIS_CIP_bdpm:
    tableName = 'CIS_CIP_bdpm'
    tableInit = 'CREATE TABLE CIS_CIP_bdpm (id INT UNIQUE AUTO_INCREMENT DEFAULT NULL, CIS INT PRIMARY KEY, CIP7 INT, Libelle VARCHAR(255), StatusAdm VARCHAR(255), EtatCommercialisation VARCHAR(255), DateCommercialisation VARCHAR(255), CIP13 BIGINT, AgrementCollectivites VARCHAR(255), TauxRemboursement VARCHAR(255), TBD1 TEXT, TBD2 TEXT, TBD3 TEXT, IndicationsRemboursement LONGTEXT);'
    tableSchema = '(CIS, CIP7, Libelle, StatusAdm, EtatCommercialisation, DateCommercialisation, CIP13, AgrementCollectivites, TauxRemboursement, TBD1, TBD2, TBD3, IndicationsRemboursement)'

# class CIS_COMPO_bdpm:
#     tableName = 'CIS_COMPO_bdpm'
#     tableInit = '''CREATE TABLE CIS_COMPO_bdpm (
#         id INT UNIQUE AUTO_INCREMENT DEFAULT NULL,
#         CIS INT PRIMARY KEY,
#         Designation VARCHAR(255),
#         CodeSubstance INT,
#         DenominationSubstance VARCHAR(255),
#         DosageSubstance VARCHAR(255),
#         ReferenceDosage VARCHAR(255),
#         NatureComposant VARCHAR(255),
#         NumeroLien INT,
#         Extra VARCHAR(255));'''
#     tableSchema = '(CIS, Designation, CodeSubstance, DenominationSubstance, DosageSubstance, ReferenceDosage, NatureComposant, NumeroLien, Extra)'

class CIS_HAS_SMR_bdpm:
    tableName = 'CIS_HAS_SMR_bdpm'
    tableInit = 'CREATE TABLE CIS_HAS_SMR_bdpm (id INT UNIQUE AUTO_INCREMENT DEFAULT NULL, CIS INT PRIMARY KEY, CIP7 INT, Libelle VARCHAR(255), StatusAdm VARCHAR(255), EtatCommercialisation VARCHAR(255), DateCommercialisation VARCHAR(255), CIP13 BIGINT, AgrementCollectivites VARCHAR(255), TauxRemboursement VARCHAR(255), TBD1 TEXT, TBD2 TEXT, TBD3 TEXT, IndicationsRemboursement LONGTEXT);'
    tableSchema = '(CIS, CIP7, Libelle, StatusAdm, EtatCommercialisation, DateCommercialisation, CIP13, AgrementCollectivites, TauxRemboursement, TBD1, TBD2, TBD3, IndicationsRemboursement)'

def start():
    downloadSource('CIS_bdpm.txt')
    downloadSource('CIS_CIP_bdpm.txt')
    # downloadSource('CIS_COMPO_bdpm.txt')
    # downloadSource('CIS_HAS_SMR_bdpm.txt')
    # downloadSource('CIS_HAS_ASMR_bdpm.txt')
    # downloadSource('CIS_GENER_bdpm.txt')
    # downloadSource('CIS_CPD_bdpm.txt')
    # downloadSource('CIS_InfoImportantes.txt')

    connection: connector | connector.DatabaseError  = connectDB()

    if type(connection) is  connector.connection_cext.CMySQLConnection:
        print('MySQL Server ' + connection.get_server_info())
        importData(connection, CIS_bdpm.tableName, CIS_bdpm.tableInit, CIS_bdpm.tableSchema)
        importData(connection, CIS_CIP_bdpm.tableName, CIS_CIP_bdpm.tableInit, CIS_CIP_bdpm.tableSchema)
        # importData(connection, CIS_COMPO_bdpm.tableName, CIS_COMPO_bdpm.tableInit, CIS_COMPO_bdpm.tableSchema)
    else:
        print(connection, file=stderr)

start()
