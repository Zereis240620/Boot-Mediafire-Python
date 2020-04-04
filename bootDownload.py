from selenium import webdriver
from PyQt5 import QtWidgets, uic
from multiprocessing import Process
import time

janela = QtWidgets.QApplication([])
interface = uic.loadUi("template.ui")

def RegraBoot():
	 lin = []
	 
	 if interface.input1.text() != '':	
	 	print('preenchido'+interface.input1.text())
	 	lin.append(interface.input1.text())
	 if interface.input2.text() != '':	
	  print('preenchido'+interface.input2.text())
	  lin.append(interface.input2.text())
	 if interface.input3.text() != '':	
	  print('preenchido'+interface.input3.text())
	  lin.append(interface.input3.text())
	 if interface.input4.text() != '':	
	 	print('preenchido'+interface.input4.text())
	 	lin.append(interface.input4.text())
	 if interface.input5.text() != '':	
	 	print('preenchido'+interface.input5.text())
	 	lin.append(interface.input5.text())
	 if not lin:
	 	interface.text.setText("campos vazios")
	 	print('Sem dados')
	 else:
	    chromedriver = 'C:/Users/ZeReis-Dev/Desktop/python/chromedriver'
	    for c in lin:
	  	 	print(lin)
	  	 	url = c.split('/')
	  	 	print('Tamanho lista',len(url))
	  	 	if len(url) < 2:
	  	 		interface.text.setText("Desculpe mais alguma(s) de suas Url(s) é invalida")
	  	 		print('Url é invalida')
	  	 	else: 
	  	 		if url[2] == 'www.mediafire.com':
	  	 			print('Url Valida')
	  	 			interface.text.setText("")
	  	 			browser = webdriver.Chrome(chromedriver)
	  	 			browser.get(c)
	  	 			browser.maximize_window()
	  	 			browser.find_element_by_xpath('//*[@id="download_link"]/a[2]').click()



interface.pushButton.clicked.connect(RegraBoot)

interface.show()
janela.exec_()

