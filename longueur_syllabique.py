#!/usr/bin/env python3

import utils

def weighted_median(df, val, weight):
	# courtesy of https://stackoverflow.com/a/55521559
    df_sorted = df.sort_values(val)
    cumsum = df_sorted[weight].cumsum()
    cutoff = df_sorted[weight].sum() / 2.
    return df_sorted[cumsum >= cutoff][val].iloc[0]

def weighted_mean(df, val, weight):
	return sum(df[val] * df[weight]) / sum(df[weight])

def main():
	df = utils.get_df()
	df = df.loc[:, ("freqfilms2", "freqlivres", "orthosyll")]
	df = df[df["orthosyll"].notna()]

	df = utils.add_nbsyll(df)

	# Cas le plus plausible: les monosyllabes ne sont pas accentués
	df["acc_mono_bref"] = df["nbsyll"].apply(lambda x: 0 if x == 1 else 1/x)
	# Cas extrême: les monosyllabes sont accentués
	df["acc_mono_long"] = df["nbsyll"].apply(lambda x: 1 if x == 1 else 1/x)

	print("Longueur moyenne du pied reconstitué")

	wa_films_mono_bref = weighted_mean(df, "acc_mono_bref", "freqfilms2")
	wa_films_mono_long = weighted_mean(df, "acc_mono_long", "freqfilms2")
	print(f"Films: mono_bref {1/wa_films_mono_bref}, mono_long {1/wa_films_mono_long}")

	wa_livres_mono_bref = weighted_mean(df, "acc_mono_bref", "freqlivres")
	wa_livres_mono_long = weighted_mean(df, "acc_mono_long", "freqlivres")
	print(f"Livres: mono_bref {1/wa_livres_mono_bref}, mono_long {1/wa_livres_mono_long}")

if __name__ == "__main__":
	main()
