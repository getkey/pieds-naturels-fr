# Pieds poétiques naturels en français

Le but de ce logiciel est de calculer quel types de pieds correspondent fréquemment aux mots français. Autrement dit, quel pied est le plus naturel en français.

Pour le moment ce logiciel est assez peu précis, il a 2 façons de calculer l'accent principal et ne calcule aucun accent secondaire.

Les résultats préliminaires semblent montrer que les rythmes binaires sont les plus communs au sein d'un mot.
Au sein d'une phrase, il est fort possible que la forte proportion de monosyllabes rendent les rythmes ternaires autant voir plus communs que les rythmes binaires. Il faut poursuivre les recherches.

Il est relativement certain que les ïambes sont aussi communes que les trochées, et les anapestes que les amphibraques.

## Lancer l'analyse

Ce logiciel utilise la base de donnée fréquentielle [Lexique](http://www.lexique.org/).

```sh
./main.py path/to/lexique.tsv
```

### Nix

Si [Nix](https://nixos.org/) est installé, il peut mettre en place automatiquement un environnement de développement avec toutes les dépendances.

```sh
nix-shell
./main.py
```
