# PROGETTO FINALE M1
# Analisi di Vendite in una Catena di Negozi
#
# Librerie utilizzate:
# - NumPy
# - Pandas
# - Matplotlib
#
# Il file vendite.csv deve trovarsi nella stessa cartella
# di questo programma.


from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Percorso della cartella che contiene il programma.
CARTELLA_PROGETTO = Path(__file__).resolve().parent
PERCORSO_VENDITE = CARTELLA_PROGETTO / "vendite.csv"


# ============================================================
# PARTE 2 - IMPORTAZIONE CON PANDAS
# ============================================================

def importa_dataset():
    """Importa vendite.csv e mostra le informazioni richieste."""

    if not PERCORSO_VENDITE.exists():
        raise FileNotFoundError(
            "Il file vendite.csv non è stato trovato nella cartella "
            "del progetto."
        )

    df = pd.read_csv(
        PERCORSO_VENDITE,
        encoding="utf-8-sig"
    )

    # Converte la colonna Data in formato data.
    df["Data"] = pd.to_datetime(
        df["Data"],
        format="%Y-%m-%d"
    )

    print("=== PRIME 5 RIGHE DEL DATASET ===")
    print(df.head())

    print("\n=== NUMERO DI RIGHE E COLONNE ===")
    print(df.shape)

    print("\n=== INFORMAZIONI GENERALI ===")
    df.info()

    return df


# ============================================================
# PARTE 3 - ELABORAZIONI CON PANDAS
# ============================================================

def analisi_pandas(df):
    """Esegue le elaborazioni richieste con Pandas."""

    # Creazione della colonna Incasso.
    df["Incasso"] = (
        df["Quantità"] * df["Prezzo_unitario"]
    ).round(2)

    incasso_totale = df["Incasso"].sum()

    incasso_medio_negozio = (
        df.groupby("Negozio")["Incasso"]
        .mean()
        .sort_values(ascending=False)
    )

    top_3_quantita = (
        df.groupby("Prodotto")["Quantità"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )

    incasso_medio_negozio_prodotto = (
        df.groupby(["Negozio", "Prodotto"])["Incasso"]
        .mean()
        .round(2)
    )

    print("\n=== ANALISI CON PANDAS ===")
    print(f"Incasso totale della catena: € {incasso_totale:.2f}")

    print("\nIncasso medio per negozio:")
    for negozio, incasso in incasso_medio_negozio.items():
        print(f"- {negozio}: € {incasso:.2f}")

    print("\nTop 3 prodotti più venduti per quantità:")
    for posizione, (prodotto, quantita) in enumerate(
        top_3_quantita.items(),
        start=1
    ):
        print(f"{posizione}. {prodotto}: {quantita} unità")

    print("\nIncasso medio per Negozio e Prodotto:")
    print(incasso_medio_negozio_prodotto)

    return df


# ============================================================
# PARTE 4 - USO DI NUMPY
# ============================================================

def analisi_numpy(df):
    """Calcola le statistiche della quantità con NumPy."""

    quantita = df["Quantità"].to_numpy()

    media = np.mean(quantita)
    minimo = np.min(quantita)
    massimo = np.max(quantita)
    deviazione_standard = np.std(quantita)

    percentuale_sopra_media = (
        np.sum(quantita > media) / quantita.size
    ) * 100

    print("\n=== ANALISI CON NUMPY ===")
    print(f"Media quantità: {media:.2f}")
    print(f"Quantità minima: {minimo}")
    print(f"Quantità massima: {massimo}")
    print(f"Deviazione standard: {deviazione_standard:.2f}")
    print(
        "Percentuale di vendite sopra la media: "
        f"{percentuale_sopra_media:.2f}%"
    )

    # Array NumPy 2D: Quantità e Prezzo_unitario.
    dati_2d = df[
        ["Quantità", "Prezzo_unitario"]
    ].to_numpy(dtype=float)

    incassi_numpy = dati_2d[:, 0] * dati_2d[:, 1]

    # Confronto con la colonna Incasso del DataFrame.
    confronto = np.allclose(
        incassi_numpy,
        df["Incasso"].to_numpy(),
        atol=0.01
    )

    print("\nArray NumPy 2D - prime 5 righe:")
    print(dati_2d[:5])

    print(
        "\nConfronto NumPy/colonna Incasso corretto:",
        confronto
    )

    return confronto


# ============================================================
# PARTE 5 - VISUALIZZAZIONI CON MATPLOTLIB
# ============================================================

def crea_grafici(df):
    """Crea e salva i tre grafici richiesti."""

    # 1. Grafico a barre: incasso totale per negozio.
    incasso_negozio = (
        df.groupby("Negozio")["Incasso"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))
    incasso_negozio.plot(kind="bar")
    plt.title("Incasso totale per negozio")
    plt.xlabel("Negozio")
    plt.ylabel("Incasso (€)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(
        CARTELLA_PROGETTO / "incasso_per_negozio.png",
        dpi=150
    )
    plt.close()

    # 2. Grafico a torta: percentuale di incassi per prodotto.
    incasso_prodotto = (
        df.groupby("Prodotto")["Incasso"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(9, 9))
    plt.pie(
        incasso_prodotto.values,
        labels=incasso_prodotto.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Percentuale di incassi per prodotto")
    plt.tight_layout()
    plt.savefig(
        CARTELLA_PROGETTO / "incassi_per_prodotto.png",
        dpi=150
    )
    plt.close()

    # 3. Grafico a linee: andamento giornaliero degli incassi.
    incasso_giornaliero = (
        df.groupby("Data")["Incasso"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(12, 6))
    plt.plot(
        incasso_giornaliero.index,
        incasso_giornaliero.values,
        marker="o"
    )
    plt.title("Andamento giornaliero degli incassi")
    plt.xlabel("Data")
    plt.ylabel("Incasso (€)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(
        CARTELLA_PROGETTO / "andamento_giornaliero_incassi.png",
        dpi=150
    )
    plt.close()

    print("\n=== GRAFICI CREATI ===")
    print("- incasso_per_negozio.png")
    print("- incassi_per_prodotto.png")
    print("- andamento_giornaliero_incassi.png")


# ============================================================
# PARTE 6 - ANALISI AVANZATA
# ============================================================

def assegna_categoria(prodotto):
    """Associa ogni prodotto a una grande categoria."""

    categorie = {
        "Smartphone": "Informatica",
        "Laptop": "Informatica",
        "Tablet": "Informatica",
        "Monitor": "Informatica",
        "TV": "Elettrodomestici",
        "Cuffie": "Audio",
        "Console": "Gaming",
        "Fotocamera": "Fotografia",
    }

    return categorie.get(prodotto, "Altro")


def analisi_avanzata(df):
    """Crea Categoria, calcola le statistiche e salva il CSV."""

    df["Categoria"] = df["Prodotto"].apply(
        assegna_categoria
    )

    incasso_totale_categoria = (
        df.groupby("Categoria")["Incasso"]
        .sum()
        .sort_values(ascending=False)
    )

    quantita_media_categoria = (
        df.groupby("Categoria")["Quantità"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n=== ANALISI AVANZATA ===")

    print("\nIncasso totale per categoria:")
    for categoria, incasso in incasso_totale_categoria.items():
        print(f"- {categoria}: € {incasso:.2f}")

    print("\nQuantità media venduta per categoria:")
    for categoria, quantita_media in quantita_media_categoria.items():
        print(f"- {categoria}: {quantita_media:.2f}")

    percorso_output = (
        CARTELLA_PROGETTO / "vendite_analizzate.csv"
    )

    df.to_csv(
        percorso_output,
        index=False,
        encoding="utf-8-sig",
        date_format="%Y-%m-%d"
    )

    print(
        "\nDataFrame aggiornato salvato in:",
        percorso_output.name
    )

    return df


# ============================================================
# PARTE 7 - ESTENSIONI
# ============================================================

def top_n_prodotti(df, n):
    """
    Restituisce i primi N prodotti in base
    all'incasso totale.
    """

    if not isinstance(n, int):
        raise TypeError("N deve essere un numero intero.")

    if n <= 0:
        raise ValueError("N deve essere maggiore di zero.")

    classifica = (
        df.groupby("Prodotto")["Incasso"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )

    return classifica


def grafico_combinato(df):
    """
    Crea un grafico combinato:
    - barre: incasso medio per categoria;
    - linea: quantità media per categoria.
    """

    incasso_medio_categoria = (
        df.groupby("Categoria")["Incasso"]
        .mean()
        .sort_index()
    )

    quantita_media_categoria = (
        df.groupby("Categoria")["Quantità"]
        .mean()
        .reindex(incasso_medio_categoria.index)
    )

    figura, asse_incasso = plt.subplots(figsize=(11, 6))

    asse_incasso.bar(
        incasso_medio_categoria.index,
        incasso_medio_categoria.values
    )
    asse_incasso.set_xlabel("Categoria")
    asse_incasso.set_ylabel("Incasso medio (€)")

    asse_quantita = asse_incasso.twinx()
    asse_quantita.plot(
        quantita_media_categoria.index,
        quantita_media_categoria.values,
        marker="o",
        linewidth=2
    )
    asse_quantita.set_ylabel("Quantità media venduta")

    plt.title(
        "Incasso medio e quantità media per categoria"
    )
    figura.tight_layout()

    plt.savefig(
        CARTELLA_PROGETTO / "grafico_combinato_categorie.png",
        dpi=150
    )
    plt.close()

    print(
        "\nGrafico combinato creato: "
        "grafico_combinato_categorie.png"
    )


# ============================================================
# PROGRAMMA PRINCIPALE
# ============================================================

def main():
    """Esegue tutte le parti del progetto."""

    df = importa_dataset()

    df = analisi_pandas(df)

    confronto_corretto = analisi_numpy(df)

    crea_grafici(df)

    df = analisi_avanzata(df)

    print("\n=== TOP 3 PRODOTTI PER INCASSO ===")
    top_3 = top_n_prodotti(df, 3)

    for posizione, (prodotto, incasso) in enumerate(
        top_3.items(),
        start=1
    ):
        print(
            f"{posizione}. {prodotto}: "
            f"€ {incasso:.2f}"
        )

    grafico_combinato(df)

    print("\n=== CONTROLLO FINALE ===")
    print(
        "Gli incassi NumPy corrispondono "
        "alla colonna Incasso:",
        confronto_corretto
    )

    print("\n=== FILE GENERATI ===")
    print("- vendite_analizzate.csv")
    print("- incasso_per_negozio.png")
    print("- incassi_per_prodotto.png")
    print("- andamento_giornaliero_incassi.png")
    print("- grafico_combinato_categorie.png")

    print("\n=== FINE PROGRAMMA ===")


if __name__ == "__main__":
    main()