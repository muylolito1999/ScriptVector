import numpy as np

def inserisci_vettori():
    n = int(input("Inserisci il numero di vettori: "))
    dimensione = int(input("Inserisci la dimensione dei vettori: "))
    vettori = []
    for i in range(n):
        # Ottiene il vettore come input, separato da spazi
        vettore = list(map(float, input(f"Inserisci il vettore {i + 1} (elementi separati da spazio): ").split()))
        if len(vettore) != dimensione:
            raise ValueError("Tutti i vettori devono avere la stessa dimensione.")
        vettori.append(vettore)
    return np.array(vettori).T  # Trasposta per avere vettori come colonne

def verifica_indipendenza(vettori):
    if np.linalg.matrix_rank(vettori) == min(vettori.shape[0], vettori.shape[1]):
        print("I vettori sono linearmente indipendenti.")
    else:
        print("I vettori non sono linearmente indipendenti.")

def main():
    try:
        vettori = inserisci_vettori()
        verifica_indipendenza(vettori)
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()
