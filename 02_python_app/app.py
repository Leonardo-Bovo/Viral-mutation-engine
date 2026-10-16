messaggio_iniziale = "Ciao questa è la prima versione dell'app per il crea vaccini, \nadesso sono da terminale ma tra qualche settimana/un mese \nsarò una semplice schermata grafica"
import time
import sys

# 1. Definizione delle variabili dell'interfaccia
UI_titolo = "-------------------------------------Viral Mutation Engine-------------------------------------\n"
descrizione = (
    "Il sistema analizza l'antigene di un nuovo virus, ricerca somiglianze \n"
    "strutturali in un archivio storico e impiega un **algoritmo genetico ad alte prestazioni** \n"
    "per sintetizzare ed evolvere un vaccino/anticorpo ad alta affinità di legame, \n"
    "simulando la risposta immunitaria e la corsa agli armamenti biologica (mutazioni del patogeno).\n"
)

# 2. Avvio del programma
print(UI_titolo)
print(descrizione)

# Input dell'utente
virus = input("Inserisci il virus da analizzare: ")
print("\n[!] Inizializzazione sequenziamento...")

# 3. Barra di caricamento animata sulla stessa riga
sys.stdout.write("Caricamento: [")
sys.stdout.flush()

for i in range(15):
    time.sleep(0.15)  # Crea una breve pausa per simulare il calcolo
    sys.stdout.write("■")
    sys.stdout.flush()

sys.stdout.write("] 100% Completato!\n\n")

# 4. Output finale dei risultati
print("----------------------------------- RISULTATI OBIETTIVO -----------------------------------")
print(f"Target virale elaborato con successo: {virus.upper()}")
print("Mutazioni simulate: Generazione G-10 completata.")
print("-------------------------------------------------------------------------------------------")
