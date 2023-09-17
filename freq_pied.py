#!/usr/bin/env python3

import pandas as pd
import utils

def row_to_foot(row: pd.Series):
	if row["nbsyll"] == 1:
		return "brève"

	if row["oxytone2"]:
		if row["nbsyll"] == 2:
			return "ïambe"
		if row["nbsyll"] == 3:
			return "anapeste"
		if row["nbsyll"] == 4:
			return "péon quatrième"
		if row["nbsyll"] == 5:
			return "loïsthios"

		return "inconnu"

	# assuming paroxytone
	if row["nbsyll"] == 2:
		return "trochée"
	if row["nbsyll"] == 3:
		return "amphibraque"
	if row["nbsyll"] == 4:
		return "péon troisième"
	if row["nbsyll"] == 5:
		return "anétos"


	return "inconnu"

def sudise_phon(phon: str):
	# this is an extreme accent, it's not realistic
	if phon.endswith(("j", "p", "b", "t", "d", "k", "g", "f", "v", "s", "z", "S", "Z", "m", "n", "N", "l", "R", "x", "G")):
		return phon + "°"

	return phon

def foot_type(df: pd.DataFrame):
	# cleanup
	res = df.loc[:, ("ortho", "cgram", "freqfilms2", "freqlivres", "phon", "orthosyll")]
	res = res[res["orthosyll"].notna()]
	res = res[res["cgram"].notna()]
	res["ortho"] = res["ortho"].str.strip()

	res = utils.add_freq(res)
	res["phon_sud"] = res["phon"].apply(sudise_phon)
	res = utils.add_nbsyll(res)

	# both are imperfect approximations, it's recommended to test both
	res["oxytone1"] = ~res["phon_sud"].str.endswith("°")
	res["oxytone2"] = ~(res["ortho"].str.fullmatch(r".*(?<!é)es?$") | (res["ortho"].str.endswith("ent") & ~res["cgram"].eq("VER")))

	res["pied"] = res.apply(row_to_foot, axis=1)

	return res


def main():
	df = utils.get_df()

	feet = foot_type(df)
	# feet = feet.sort_values(by="freq", ascending=False)
	# print(feet.head(200))
	res = feet.groupby("pied").agg({"freq": "sum"}).sort_values(by="freq", ascending=False)
	print(res)

if __name__ == "__main__":
	main()
