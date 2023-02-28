import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QMessageBox,QMainWindow)
from PyQt6.QtCore import Qt
from mazmorraDavidCompilada import Ui_MainWindow
import random as rnd
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initializeUI()
        self.show()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.sala="central"
        self.inicio=0
        self.salasCompletadas=[]
        self.ui.actionSalir.triggered.connect(self.salir)
        self.ui.actionAyuda.triggered.connect(self.ayuda)
        self.ui.jugar.clicked.connect(self.jugar)
        self.ui.salir.clicked.connect(self.salirSala)
        self.ui.norte.clicked.connect(self.salaNorte)
        self.ui.este.clicked.connect(self.salaEste)
        self.ui.oeste.clicked.connect(self.salaOeste)
        self.ui.sur.clicked.connect(self.salaSur)
        self.ui.norte.clicked.connect(self.salaNorte)
        self.ui.radio1.setText("")
        self.ui.radio2.setText("")
        self.ui.radio3.setText("")
        self.ui.infosala.setText("Para comenzar a jugar dale al boton de jugar, para salir dale al boton de salir")
        
    def jugar(self):
        if(self.sala=="central" and self.inicio==0):
            self.ui.inicio.setEnabled(True)
            self.ui.inicio.setStyleSheet("QPushButton{background-color: #E78406}")
            self.ui.norte.setEnabled(True)
            self.ui.sur.setEnabled(True)
            self.ui.este.setEnabled(True)
            self.ui.oeste.setEnabled(True)
            self.inicio+=1
        elif(self.sala=="este"):
            self.ui.este.setStyleSheet("QPushButton{background-color: #E78406}")
            
            self.jugarEste()
            
        elif(self.sala=="oeste"):
            self.jugarOeste()
        elif(self.sala=="sur"):
            self.ui.sur.setStyleSheet("QPushButton{background-color: #E78406}")
            self.jugarSur()
        elif(self.sala=="norte"):
            self.ui.norte.setStyleSheet("QPushButton{background-color: #E78406}")
            self.jugarNorte()
    
    def salirSala(self):
        if(self.sala=="central"):
            self.ui.salir.setEnabled(False)
            self.ui.inicio.setStyleSheet("QPushButton{background-color: #E78406}")
            self.ui.norte.setEnabled(True)
            self.ui.sur.setEnabled(True)
            self.ui.este.setEnabled(True)
            self.ui.oeste.setEnabled(True)
        elif(self.sala=="este"):
            self.sala="central"
            self.ui.jugar.setEnabled(False)
            self.ui.inicio.setStyleSheet("QPushButton{background-color: #E78406}")
            self.ui.este.setStyleSheet("background-color:#B5C1BC;color:black")
            self.habilitar()
        elif(self.sala=="oeste"):
            self.sala="central"
            self.ui.jugar.setEnabled(False)
            self.ui.inicio.setStyleSheet("QPushButton{background-color: #E78406}")
            self.ui.oeste.setStyleSheet("background-color:#B5C1BC;color:black")
            self.ui.radio1.setEnabled(False)
            self.ui.radio2.setEnabled(False)
            self.ui.radio3.setEnabled(False)
            self.ui.radio1.setText("")
            self.ui.radio2.setText("")
            self.ui.radio3.setText("")
            self.habilitar()
        elif(self.sala=="sur"):
            self.sala="central"
            self.ui.jugar.setEnabled(False)
            self.ui.inicio.setStyleSheet("QPushButton{background-color: #E78406}")
            self.ui.sur.setStyleSheet("background-color:#B5C1BC;color:black")
            self.ui.radio1.setEnabled(False)
            self.ui.radio2.setEnabled(False)
            self.ui.radio3.setEnabled(False)
            self.ui.radio1.setText("")
            self.ui.radio2.setText("")
            self.ui.radio3.setText("")
            self.habilitar()
        elif(self.sala=="norte"):
            self.sala="central"
            self.ui.jugar.setEnabled(False)
            self.ui.inicio.setStyleSheet("QPushButton{background-color: #E78406}")
            self.ui.norte.setStyleSheet("background-color:#B5C1BC;color:black")
            self.habilitar()

    def ayuda(self):
         QMessageBox.information(self, "Ayuda",
                "Estas en una mazmorra de la cual solo puedes salir completando todas las salas, selecciona una sala"
                +", esta te mostrara las instrucciones, dentro de la sala dale al boton,"
                +" de jugar cuando tu respuesta este seleccionada, si es necesaria, sino pulsa jugar o salir segun lo que desees hacer") 
 
    def deshabilitar(self):
        #self.ui.frame.setEnabled(True)
        #if(self.sala=="central"):
            self.ui.inicio.setEnabled(False)
            self.ui.norte.setEnabled(False)
            self.ui.sur.setEnabled(False)
            self.ui.este.setEnabled(False)
            self.ui.oeste.setEnabled(False)
    
    def habilitar(self):
        if("oeste" not in self.salasCompletadas):
            self.ui.oeste.setEnabled(True)
        if("este" not in self.salasCompletadas):
            self.ui.este.setEnabled(True)
        if("norte" not in self.salasCompletadas):
            self.ui.norte.setEnabled(True)
        if("sur" not in self.salasCompletadas):
            self.ui.sur.setEnabled(True)
        self.ui.inicio.setEnabled(True)
        self.ui.jugar.setEnabled(False)
        self.ui.inicio.setStyleSheet("QPushButton{background-color: #E78406}")
        self.ui.salir.setEnabled(False)
        if("norte" in self.salasCompletadas and
        "sur" in self.salasCompletadas and
        "este" in self.salasCompletadas and
        "oeste" in self.salasCompletadas):
            self.ui.resultado.setText("HAS COMLPETADO LA MAZMORRA!!!")

    def salaSur(self):
        self.ui.sur.setStyleSheet("QPushButton{background-color: #E78406}")
        self.ui.inicio.setStyleSheet("background-color:#B5C1BC;color:black")
        self.ui.salir.setEnabled(True)
        self.ui.jugar.setEnabled(True)
        self.sala="sur"
        self.deshabilitar()
        texto="Has entrado a una sala con una pregunta dificilisima, responde correctamente para completar la sala"
        self.ui.radio1.setEnabled(True)
        self.ui.radio2.setEnabled(True)
        self.ui.radio3.setEnabled(True)
        preguntas=["¿Cual es el rio mas largo de España?","¿cual es el rio mas largo de la Peninsula Iberica?","¿Cual es el rio mas largo del mundo?"
        ,"¿Cual es la montaña mas alta de España?","¿Cual es la montaña mas alta del mundo?","¿Cual es el oceano mas grande?","¿Cual es el pais con mayor extension?"]
        respuestas = ["Ebro","Tajo","Amazonas","Teide","Everest","Pacifico","Rusia"]
        numPregunta=rnd.randint(0,len(preguntas)-1)
        self.ui.infosala.setText(texto+"\n\n"+preguntas[numPregunta])
        print(preguntas[numPregunta])
        self.ui.radio1.setText(respuestas[rnd.randint(0,len(preguntas)-1)])
        self.ui.radio2.setText(respuestas[numPregunta])
        self.ui.radio3.setText(respuestas[rnd.randint(0,len(preguntas)-1)])

    def jugarSur(self):
        if(self.ui.radio2.isChecked()):
            self.ui.resultado.setText("Has acertado, completaste la sala!!")
            self.salasCompletadas.append('sur')
            self.ui.este.setEnabled(False)
            self.sala="central"
            self.ui.sur.setStyleSheet("QPushButton{background-color: lightgreen}")
            self.habilitar()
            self.ui.radio1.setEnabled(False)
            self.ui.radio2.setEnabled(False)
            self.ui.radio3.setEnabled(False)
            self.ui.radio1.setText("")
            self.ui.radio2.setText("")
            self.ui.radio3.setText("")
        elif(not self.ui.radio1.isChecked() and not self.ui.radio2.isChecked() and not self.ui.radio3.isChecked()):
            self.ui.resultado.setText("Elige una respuesta")
        else:
            self.ui.resultado.setText("Has fallado, vuelve a intentarlo ;)")

    def salaOeste(self): 
        self.ui.oeste.setStyleSheet("QPushButton{background-color: #E78406}")
        self.ui.inicio.setStyleSheet("background-color:#B5C1BC;color:black")
        self.ui.salir.setEnabled(True)
        self.ui.jugar.setEnabled(True)
        self.sala="oeste"
        self.deshabilitar()
        texto="Has entrado a una sala con una advivinanza,acierta la respuesta para completar la sala"
        self.ui.radio1.setEnabled(True)
        self.ui.radio2.setEnabled(True)
        self.ui.radio3.setEnabled(True)
        preguntas = ["Entra duro y grande en la boca,pero sale blando y pequeño. ¿Qué es?","Húmedo por dentro, con pelos por fuera. Comienza por la C. ¿De qué se trata?"
            ,"Lo levanto cuando estoy contento,pero es más pequeño que el resto. ¿Qué es?","Aparato que vibra y gira, te metes en la boca unas 3 veces al día y mide unos 15 cm. ¿Qué es?"
            ,"Las personas siempre duermen menos en un mes del año. ¿Cuál es este mes?","Soy alto siendo joven y corto cuando soy viejo. Resplandezco con la vida y el viento es mi mayor enemigo. ¿Qué soy?"
            ,"Crezco a pesar de no estar vivo. No tengo pulmones, pero para vivir necesito el aire. El agua, aunque no tenga boca, me mata. ¿Qué soy?","Estando roto es más útil que sin romperse. ¿Qué es?"
            ,"La señora y el señor Sánchez tienen 6 hijos. Cada hijo tiene una hermana. ¿Cuántas personas hay en la familia Sánchez?","Te paras cuando está verde y continúas cuando está rojo. ¿Qué es?"]
        respuestas = ["Un chicle","Un coco","El dedo pulgar","Un cepillo de dientes eléctrico","Febrero","Una vela","El fuego","Un huevo","9","Una sandia"]
        numPregunta=rnd.randint(0,len(preguntas)-1)
        self.ui.infosala.setText(texto+"\n\n"+preguntas[numPregunta])
        print(preguntas[numPregunta])
        self.ui.radio1.setText(respuestas[rnd.randint(0,len(preguntas)-1)])
        self.ui.radio2.setText(respuestas[numPregunta])
        self.ui.radio3.setText(respuestas[rnd.randint(0,len(preguntas)-1)])

    def jugarOeste(self):
        if(self.ui.radio2.isChecked()):
            self.ui.resultado.setText("Has acertado, completaste la sala!!")
            self.salasCompletadas.append('oeste')
            self.ui.este.setEnabled(False)
            self.sala="central"
            self.habilitar()
            self.ui.oeste.setStyleSheet("QPushButton{background-color: lightgreen}")
            self.ui.radio1.setEnabled(False)
            self.ui.radio2.setEnabled(False)
            self.ui.radio3.setEnabled(False)
            self.ui.radio1.setText("")
            self.ui.radio2.setText("")
            self.ui.radio3.setText("")
        elif(not self.ui.radio1.isChecked() and not self.ui.radio2.isChecked() and not self.ui.radio3.isChecked()):
            self.ui.resultado.setText("Elige una respuesta")
        else:
            self.ui.resultado.setText("Has fallado, vuelve a intentarlo ;)")

    def salaEste(self):
        self.ui.este.setStyleSheet("QPushButton{background-color: #E78406}")
        self.ui.inicio.setStyleSheet("background-color:#B5C1BC;color:black")
        self.ui.salir.setEnabled(True)
        self.ui.jugar.setEnabled(True)
        self.sala="este"
        self.deshabilitar()
        texto="Has entrado a una sala con un cofre del tesoro, para abrirlo tienes que sacar mas de 63, sino te tocara esperar 20 segundos"
        self.ui.infosala.setText(texto)
        
    def jugarEste(self):
        puntuacionCofre=rnd.randint(0, 100)
        print("Has sacado: ",puntuacionCofre," puntos")
        if(puntuacionCofre > 63):
            self.salasCompletadas.append('este')
            self.ui.resultado.setText("Lo has abierto con "+str(puntuacionCofre)+" puntos")
            print("Lo has conseguido abrir")
            self.ui.este.setEnabled(False)
            self.sala="central"
            self.ui.este.setStyleSheet("QPushButton{background-color: lightgreen}")
            self.habilitar()
        else:
            self.ui.resultado.setText("Has sacado  "+str(puntuacionCofre)+" puntos, vuelve a intentarlo")
                
    def salaNorte(self):
        self.ui.norte.setStyleSheet("QPushButton{background-color: #E78406}")
        self.ui.inicio.setStyleSheet("background-color:#B5C1BC;color:black")
        self.sala="norte"
        self.ui.salir.setEnabled(True)
        self.ui.jugar.setEnabled(True)
        puntuacionEnemigo=rnd.randint(0, 100)
        texto = "El enemigo te ha atacado, su puntuacion ha sido de: "+str(puntuacionEnemigo)
        self.ui.infosala.setText("Has entrado en una sala con un monstruo el cual te va a atacar YAA\n"+texto+
        "\n¿Deseas contraatacarle?")
        print("El enemigo te ha atacado, su puntuacion ha sido de: ",puntuacionEnemigo)
        if(puntuacionEnemigo>=90):
            self.sala="central"
            self.ui.resultado.setText("El monstruo te ha ganado, te hemos curado en la sala central")
            self.ui.norte.setStyleSheet("")
            self.ui.inicio.setStyleSheet("QPushButton{background-color: #E78406}")
            self.ui.jugar.setEnabled(False)

    def jugarNorte(self):
        puntuacionJugador=rnd.randint(0, 100)
        print("Tu puntuacion ha sido de: ",puntuacionJugador)
        if(puntuacionJugador>60):
            self.salasCompletadas.append('norte')
            self.ui.resultado.setText("Has derrotado al enemigo con una puntuacion de: "+str(puntuacionJugador))
            self.sala="central"
            self.ui.norte.setStyleSheet("QPushButton{background-color: lightgreen}")
            self.ui.norte.setEnabled(False)
            self.habilitar()
        else:
            self.ui.resultado.setText("No has logrado derrotar al enemigo con tu puntuacion de: "+str(puntuacionJugador))
            self.salaNorte()
                
    def salir():
        sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Keypad = MainWindow()
    sys.exit(app.exec())