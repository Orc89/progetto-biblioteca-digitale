# PROGETTO 3 - AGENZIA DI VIAGGI
#
# Il programma gestisce clienti, viaggi e prenotazioni utilizzando:
# variabili, OOP, NumPy, Pandas e Matplotlib.

from pathlib import Path
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


SEED = 42
random.seed(SEED)
np.random.seed(SEED)

CARTELLA_OUTPUT = Path(__file__).resolve().parent


# ============================================================
# PARTE 1 - VARIABILI E TIPI DI DATI
# ============================================================

nome = "Mario Rossi"
eta = 34
saldo = 2500.75
vip = True

destinazioni_disponibili = [
    "Roma",
    "Parigi",
    "Tokyo",
    "New York",
    "Il Cairo",
    "Bangkok",
    "Rio de Janeiro",
    "Città del Capo"
]

prezzi_medi_viaggi = {
    "Roma": 450.00,
    "Parigi": 650.00,
    "Tokyo": 1600.00,
    "New York": 1500.00,
    "Il Cairo": 900.00,
    "Bangkok": 1400.00,
    "Rio de Janeiro": 1700.00,
    "Città del Capo": 1550.00
}

categorie_destinazioni = {
    "Roma": "Europa",
    "Parigi": "Europa",
    "Tokyo": "Asia",
    "Bangkok": "Asia",
    "New York": "America",
    "Rio de Janeiro": "America",
    "Il Cairo": "Africa",
    "Città del Capo": "Africa"
}


def stampa_parte_1():
    print("=== PARTE 1 - DATI INIZIALI ===")
    print(f"Nome cliente: {nome}")
    print(f"Età: {eta}")
    print(f"Saldo conto: € {saldo:.2f}")
    print(f"Cliente VIP: {vip}")
    print("\nDestinazioni disponibili:")

    for destinazione in destinazioni_disponibili:
        prezzo = prezzi_medi_viaggi[destinazione]
        print(f"- {destinazione}: prezzo medio € {prezzo:.2f}")


# ============================================================
# PARTE 2 - PROGRAMMAZIONE A OGGETTI
# ============================================================

class Cliente:
    def __init__(self, nome, eta, vip=False):
        self.nome = nome
        self.eta = int(eta)
        self.vip = bool(vip)

    def __str__(self):
        stato_vip = "Sì" if self.vip else "No"
        return (
            f"Cliente: {self.nome} | Età: {self.eta} | "
            f"VIP: {stato_vip}"
        )

    def stampa_informazioni(self):
        print(self)


class Viaggio:
    def __init__(self, destinazione, prezzo, durata_giorni):
        self.destinazione = destinazione
        self.prezzo = float(prezzo)
        self.durata_giorni = int(durata_giorni)

    def __str__(self):
        return (
            f"Destinazione: {self.destinazione} | "
            f"Prezzo: € {self.prezzo:.2f} | "
            f"Durata: {self.durata_giorni} giorni"
        )


class Prenotazione:
    SCONTO_VIP = 0.10

    def __init__(self, cliente, viaggio, giorno_partenza):
        self.cliente = cliente
        self.viaggio = viaggio
        self.giorno_partenza = int(giorno_partenza)

    def calcola_importo_finale(self):
        if self.cliente.vip:
            return self.viaggio.prezzo * (1 - self.SCONTO_VIP)
        return self.viaggio.prezzo

    def dettagli(self):
        importo_finale = self.calcola_importo_finale()
        sconto = "10%" if self.cliente.vip else "Nessuno"

        print("\n=== DETTAGLI PRENOTAZIONE ===")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Età: {self.cliente.eta}")
        print(f"Cliente VIP: {'Sì' if self.cliente.vip else 'No'}")
        print(f"Destinazione: {self.viaggio.destinazione}")
        print(f"Prezzo iniziale: € {self.viaggio.prezzo:.2f}")
        print(f"Sconto applicato: {sconto}")
        print(f"Importo finale: € {importo_finale:.2f}")
        print(f"Giorno di partenza: {self.giorno_partenza}")
        print(f"Durata: {self.viaggio.durata_giorni} giorni")


# ============================================================
# PARTE 3 - NUMPY
# ============================================================

def analisi_numpy():
    prezzi_simulati = np.random.uniform(200, 2000, 100)

    prezzo_medio = np.mean(prezzi_simulati)
    prezzo_minimo = np.min(prezzi_simulati)
    prezzo_massimo = np.max(prezzi_simulati)
    deviazione_standard = np.std(prezzi_simulati)

    percentuale_sopra_media = (
        np.sum(prezzi_simulati > prezzo_medio)
        / prezzi_simulati.size
        * 100
    )

    print("\n=== PARTE 3 - ANALISI NUMPY ===")
    print(f"Numero di prenotazioni simulate: {prezzi_simulati.size}")
    print(f"Prezzo medio: € {prezzo_medio:.2f}")
    print(f"Prezzo minimo: € {prezzo_minimo:.2f}")
    print(f"Prezzo massimo: € {prezzo_massimo:.2f}")
    print(f"Deviazione standard: € {deviazione_standard:.2f}")
    print(
        "Percentuale di prenotazioni sopra la media: "
        f"{percentuale_sopra_media:.2f}%"
    )

    return prezzi_simulati


# ============================================================
# PARTE 4 - PANDAS
# ============================================================

def crea_clienti():
    return [
        Cliente("Mario Rossi", 34, True),
        Cliente("Lucia Bianchi", 28, False),
        Cliente("Giovanni Verdi", 45, False),
        Cliente("Sara Esposito", 31, True),
        Cliente("Luca Ferrari", 39, False),
        Cliente("Anna Romano", 52, True),
        Cliente("Paolo Conti", 26, False),
        Cliente("Elena De Luca", 47, False),
        Cliente("Marco Ricci", 36, True),
        Cliente("Giulia Marino", 42, False),
        Cliente("Francesca Greco", 29, False),
        Cliente("Andrea Gallo", 50, True),
        Cliente("Simona Costa", 33, False),
        Cliente("Davide Fontana", 41, False),
        Cliente("Claudia Rizzo", 38, True)
    ]


def genera_prenotazioni(clienti, numero_prenotazioni=100):
    prenotazioni = []
    righe_dataframe = []

    for _ in range(numero_prenotazioni):
        cliente = random.choice(clienti)
        destinazione = random.choice(destinazioni_disponibili)
        prezzo_medio = prezzi_medi_viaggi[destinazione]

        prezzo = np.random.uniform(
            prezzo_medio * 0.80,
            prezzo_medio * 1.20
        )

        durata = random.randint(3, 15)
        giorno_partenza = random.randint(1, 30)

        viaggio = Viaggio(destinazione, round(prezzo, 2), durata)
        prenotazione = Prenotazione(
            cliente,
            viaggio,
            giorno_partenza
        )

        prenotazioni.append(prenotazione)

        righe_dataframe.append(
            {
                "Cliente": cliente.nome,
                "Destinazione": destinazione,
                "Prezzo": round(viaggio.prezzo, 2),
                "Giorno_Partenza": giorno_partenza,
                "Durata": durata,
                "Incasso": round(
                    prenotazione.calcola_importo_finale(),
                    2
                ),
                "VIP": cliente.vip,
                "Categoria": categorie_destinazioni[destinazione]
            }
        )

    dataframe = pd.DataFrame(righe_dataframe)
    return prenotazioni, dataframe


def analisi_pandas(dataframe):
    incasso_totale = dataframe["Incasso"].sum()

    incasso_medio_destinazione = (
        dataframe.groupby("Destinazione")["Incasso"]
        .mean()
        .sort_values(ascending=False)
    )

    top_3_destinazioni = (
        dataframe["Destinazione"]
        .value_counts()
        .head(3)
    )

    print("\n=== PARTE 4 - ANALISI PANDAS ===")
    print(f"Incasso totale dell'agenzia: € {incasso_totale:.2f}")

    print("\nIncasso medio per destinazione:")
    for destinazione, incasso in incasso_medio_destinazione.items():
        print(f"- {destinazione}: € {incasso:.2f}")

    print("\nTop 3 destinazioni più vendute:")
    for posizione, (destinazione, vendite) in enumerate(
        top_3_destinazioni.items(),
        start=1
    ):
        print(f"{posizione}. {destinazione}: {vendite} prenotazioni")

    return incasso_totale, incasso_medio_destinazione, top_3_destinazioni


# ============================================================
# PARTE 5 - MATPLOTLIB
# ============================================================

def crea_grafici(dataframe):
    incasso_destinazione = (
        dataframe.groupby("Destinazione")["Incasso"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(11, 6))
    incasso_destinazione.plot(kind="bar")
    plt.title("Incasso totale per destinazione")
    plt.xlabel("Destinazione")
    plt.ylabel("Incasso (€)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    percorso_barre = CARTELLA_OUTPUT / "incasso_per_destinazione.png"
    plt.savefig(percorso_barre, dpi=150)
    plt.close()

    incasso_giornaliero = (
        dataframe.groupby("Giorno_Partenza")["Incasso"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(11, 6))
    plt.plot(
        incasso_giornaliero.index,
        incasso_giornaliero.values,
        marker="o"
    )
    plt.title("Andamento giornaliero degli incassi")
    plt.xlabel("Giorno di partenza")
    plt.ylabel("Incasso (€)")
    plt.grid(True)
    plt.tight_layout()
    percorso_linee = CARTELLA_OUTPUT / "andamento_giornaliero_incassi.png"
    plt.savefig(percorso_linee, dpi=150)
    plt.close()

    vendite_destinazione = dataframe["Destinazione"].value_counts()

    plt.figure(figsize=(9, 9))
    plt.pie(
        vendite_destinazione.values,
        labels=vendite_destinazione.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Percentuale di vendite per destinazione")
    plt.tight_layout()
    percorso_torta = (
        CARTELLA_OUTPUT / "percentuale_vendite_destinazione.png"
    )
    plt.savefig(percorso_torta, dpi=150)
    plt.close()

    print("\n=== PARTE 5 - GRAFICI CREATI ===")
    print(f"- {percorso_barre.name}")
    print(f"- {percorso_linee.name}")
    print(f"- {percorso_torta.name}")


# ============================================================
# PARTE 6 - ANALISI AVANZATA
# ============================================================

def analisi_avanzata(dataframe):
    incasso_categoria = (
        dataframe.groupby("Categoria")["Incasso"]
        .sum()
        .sort_values(ascending=False)
    )

    durata_media_categoria = (
        dataframe.groupby("Categoria")["Durata"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n=== PARTE 6 - ANALISI AVANZATA ===")

    print("\nIncasso totale per categoria:")
    for categoria, incasso in incasso_categoria.items():
        print(f"- {categoria}: € {incasso:.2f}")

    print("\nDurata media dei viaggi per categoria:")
    for categoria, durata in durata_media_categoria.items():
        print(f"- {categoria}: {durata:.2f} giorni")

    percorso_csv = CARTELLA_OUTPUT / "prenotazioni_analizzate.csv"
    dataframe.to_csv(
        percorso_csv,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nDataFrame salvato nel file: {percorso_csv.name}")
    return incasso_categoria, durata_media_categoria


# ============================================================
# PARTE 7 - ESTENSIONI
# ============================================================

def clienti_con_piu_prenotazioni(dataframe, n=5):
    if n <= 0:
        raise ValueError("Il valore di N deve essere maggiore di zero.")

    return dataframe["Cliente"].value_counts().head(n)


def grafico_combinato_categorie(dataframe):
    incasso_medio = (
        dataframe.groupby("Categoria")["Incasso"]
        .mean()
        .sort_index()
    )

    durata_media = (
        dataframe.groupby("Categoria")["Durata"]
        .mean()
        .reindex(incasso_medio.index)
    )

    figura, asse_incasso = plt.subplots(figsize=(10, 6))

    asse_incasso.bar(
        incasso_medio.index,
        incasso_medio.values,
        label="Incasso medio"
    )
    asse_incasso.set_xlabel("Categoria")
    asse_incasso.set_ylabel("Incasso medio (€)")

    asse_durata = asse_incasso.twinx()
    asse_durata.plot(
        durata_media.index,
        durata_media.values,
        marker="o",
        label="Durata media"
    )
    asse_durata.set_ylabel("Durata media (giorni)")

    plt.title("Incasso medio e durata media per categoria")
    figura.tight_layout()

    percorso_combinato = CARTELLA_OUTPUT / "confronto_categorie.png"
    plt.savefig(percorso_combinato, dpi=150)
    plt.close()

    print(f"\nGrafico combinato creato: {percorso_combinato.name}")


# ============================================================
# PROGRAMMA PRINCIPALE
# ============================================================

def main():
    stampa_parte_1()

    cliente_esempio = Cliente(nome, eta, vip)
    viaggio_esempio = Viaggio(
        "Parigi",
        prezzi_medi_viaggi["Parigi"],
        5
    )
    prenotazione_esempio = Prenotazione(
        cliente_esempio,
        viaggio_esempio,
        15
    )

    print("\n=== PARTE 2 - ESEMPIO OOP ===")
    cliente_esempio.stampa_informazioni()
    print(viaggio_esempio)
    prenotazione_esempio.dettagli()

    analisi_numpy()

    clienti = crea_clienti()
    prenotazioni, dataframe = genera_prenotazioni(
        clienti,
        numero_prenotazioni=100
    )

    print("\n=== ANTEPRIMA DEL DATAFRAME ===")
    print(dataframe.head())

    analisi_pandas(dataframe)
    crea_grafici(dataframe)
    analisi_avanzata(dataframe)

    top_clienti = clienti_con_piu_prenotazioni(dataframe, n=5)

    print("\n=== PARTE 7 - TOP 5 CLIENTI ===")
    for posizione, (cliente, numero) in enumerate(
        top_clienti.items(),
        start=1
    ):
        print(f"{posizione}. {cliente}: {numero} prenotazioni")

    grafico_combinato_categorie(dataframe)

    print("\n=== FILE GENERATI ===")
    print("- prenotazioni_analizzate.csv")
    print("- incasso_per_destinazione.png")
    print("- andamento_giornaliero_incassi.png")
    print("- percentuale_vendite_destinazione.png")
    print("- confronto_categorie.png")

    print("\n=== FINE PROGRAMMA ===")


if __name__ == "__main__":
    main()