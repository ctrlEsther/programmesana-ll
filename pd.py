'''
    Tīna Estere Pokšāne 12.DIT klase


    1.uzd atbilde: zem class izveidošanas definēt atribūta vērtību kā piemēram "cipars = 4"
    2.uzd atbilde: 
class Klients():

    def attribute(self, vards):
        self.vards = vards

(python)


    3.uzd atbilde:
class Prece():

    def attribute(self, cena):
        self.cena = cena


(python)

    4.uzd atbilde: D
'''



import json

sastavdalas = []

class Dators():
           
    def sastavdalas(self, veids, modelis, cena):
        self.veids = veids
        self.modelis = modelis
        self.cena = cena

    def get_sastavdalas(self):
        
        return self.veids, self.modelis, self.cena
    
    def set_sastavdalas(self, new_veids, new_modelis, new_cena):

        self.veids = new_veids
        self.modelis = new_modelis
        self.cena = new_cena



ierice = Dators()
k = 2

while k > 1:
    darbiba = input('ievadi darbību, ko vēlies izpildīt. P - Pievienot jaunu sastāvdaļu, R - rediģēt jau esošu sastāvdaļu, A - apskatīt jau esošās sastāvdaļas. Ja vēlies izbeigt, ievadi "exit"'  )

    if darbiba == 'P' :
        veids = input("ievadi sava datora sastāvdaļas veidu:" )
        modelis = input('ievadi savas sastāvdaļas modeli:' )
        cena = input('ievadi sava datora sastāvdaļas cenu:' )

        sastavdalas.append({"veids": veids, "modelis": modelis, "cena": cena})

        ierice.set_sastavdalas(veids, modelis, cena)

    elif darbiba == 'A' :
        for i, sastavdala in enumerate(sastavdalas, start=1):
            print(f"{i}.sastavdala: \n Veids: {sastavdala['veids']},\n Modelis: {sastavdala['modelis']},\n Cena: {sastavdala['cena']}")

    elif darbiba == 'R':

        numurs = int(input('Ievadi nr kuru sastāvdaļu vēlies rediģēt: '))
        numurs = numurs - 1

        if numurs >= 0 and numurs < len(sastavdalas):
            sastavdala = sastavdalas[numurs]

            veids = input("ievadi sava datora izlaboto sastāvdaļas veidu: " )
            modelis = input('ievadi savas sastāvdaļas izlaboto modeli: ' )
            cena = input('ievadi sava datora sastāvdaļas izlaboto cenu: ' )

            ierice.set_sastavdalas(veids, modelis, cena)
        
        else:
            print('Nederīgs sastāvdaļas numurs.')

    elif darbiba == "exit":
        break

    else:
        print("šāda darbība nav pieejama")