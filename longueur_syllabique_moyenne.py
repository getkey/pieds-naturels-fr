#!/usr/bin/env python3

import utils

def main():
	df = utils.get_df()
	df = df.loc[:, ("freqfilms2", "freqlivres", "orthosyll")]
	df = df[df["orthosyll"].notna()]

	df = utils.add_nbsyll(df)

	wa_films = sum(df["nbsyll"] * df["freqfilms2"]) / sum(df["freqfilms2"])
	print(f"Nombre de syllabe moyen par mot (films): {wa_films}")

	wa_livres = sum(df["nbsyll"] * df["freqlivres"]) / sum(df["freqlivres"])
	print(f"Nombre de syllabe moyen par mot (livres): {wa_livres}")

if __name__ == "__main__":
	main()
