import random
import csv

new_csv_file = open("Euromilhoes.csv", "w", encoding="utf-8",newline = "")

writer = csv.writer(new_csv_file)
writer.writerow(['1numero','2numero','3numero','4numero','5numero','1estrela','2estrela'])
for i in range(50):
    numeros = []

    while len(numeros) < 5:
        num_sorteado = random.randint(1,50)
        if num_sorteado not in numeros:
            numeros.append(num_sorteado)
        
    estrelas = []
    
    while len(estrelas) < 2:
        estrela_sorteada = random.randint(1,12)
        if estrela_sorteada not in estrelas:
            estrelas.append(estrela_sorteada)
    writer.writerow(numeros + estrelas)
    print(numeros, estrelas)
    
 