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

	wa_films = weighted_mean(df, "nbsyll", "freqfilms2")
	print(f"Nombre de syllabe moyen par mot (films): {wa_films}")

	wa_livres = weighted_mean(df, "nbsyll", "freqlivres")
	print(f"Nombre de syllabe moyen par mot (livres): {wa_livres}")

	wm_films = weighted_median(df, "nbsyll", "freqfilms2")
	print(f"Nombre de syllabe median par mot (films): {wm_films}")

	wm_livres = weighted_median(df, "nbsyll", "freqlivres")
	print(f"Nombre de syllabe median par mot (livres): {wm_livres}")

if __name__ == "__main__":
	main()
