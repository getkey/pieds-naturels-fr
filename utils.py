import os
import argparse
import pandas as pd

def get_df():
	env_lexique_tsv = os.environ.get("LEXIQUE_TSV")
	parser = argparse.ArgumentParser("frequence")
	parser.add_argument(
		"lexique",
		help="Chemin de la base de donnée Lexique au format .tsv.\nIl peut aussi être fourni par la variable d'environnement $LEXIQUE_TSV.",
		type=str,
		default=env_lexique_tsv,
		nargs=("?" if env_lexique_tsv else None), # optional if env var is set ( in which case it will use the default)
	)
	args = parser.parse_args()

	pd.set_option("display.max_rows", None)
	df = pd.read_csv(args.lexique, sep="\t")

	return df

def add_nbsyll(df: pd.DataFrame):
	df["nbsyll"] = df["orthosyll"].apply(lambda x: x.count("-") + x.count(" ") + 1)
	return df

def add_freq(df: pd.DataFrame):
	df["freq"] = (df["freqfilms2"] + df["freqlivres"]) / 2
	return df
