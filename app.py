from src import downloadSource


def start():
    downloadSource.downloadSource('CIS_bdpm.txt')
    downloadSource.downloadSource('CIS_CIP_bdpm.txt')
    downloadSource.downloadSource('CIS_COMPO_bdpm.txt')
    downloadSource.downloadSource('CIS_HAS_SMR_bdpm.txt')
    downloadSource.downloadSource('CIS_HAS_ASMR_bdpm.txt')
    downloadSource.downloadSource('CIS_GENER_bdpm.txt')
    downloadSource.downloadSource('CIS_CPD_bdpm.txt')
    downloadSource.downloadSource('CIS_InfoImportantes.txt')

start()