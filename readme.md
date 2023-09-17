# Pieds poétiques naturels en français

Le but de ce logiciel est de calculer quel types de pieds correspondent fréquemment aux mots français. Autrement dit, quel pied est le plus naturel en français.

Pour le moment ce logiciel est assez peu précis, il a 2 façons de calculer l'accent principal et ne calcule aucun accent secondaire.

Il semblerait que:

- les ïambes à peu près aussi communes que les trochées, et les anapestes que les amphibraques
- les pieds binaires sont plus communs que les pieds ternaires

## Lancer l'analyse

Ce logiciel utilise la base de donnée fréquentielle [Lexique](http://www.lexique.org/).

```sh
./freq_pied.py path/to/lexique.tsv
./longueur_syllabique_moyenne.py path/to/lexique.tsv
```

### Nix

Si [Nix](https://nixos.org/) est installé, il peut mettre en place automatiquement un environnement de développement avec toutes les dépendances.

```sh
nix-shell
./freq_pied.py
./longueur_syllabique_moyenne.py
```
