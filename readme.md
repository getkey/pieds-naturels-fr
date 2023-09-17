# Pieds poétiques naturels en français

Le but de ce logiciel est de calculer quels types de pieds correspondent fréquemment aux mots français. Autrement dit, quel pied est le plus naturel en français.

Pour le moment ce logiciel est assez peu précis, il a 2 façons de calculer l'accent principal et ne calcule aucun accent secondaire.

Il semblerait que:

- les mots oxytons sont à peu près aussi communs que les mots paroxytons (donc les ïambes que les trochées, et les anapestes que les amphibraques). Voir `./freq_pied.py`.
- étant donné la prévalence des monosyllabes (généralement non-accentués), les rythmes avec un certain nombre de temps semblent plus naturels. Cependant si on fait un parallèle avec la musique, les signatures rythmiques complexes sont difficiles à percevoir. Les pieds trisyllabiques sont probablement un juste milieu. Voir `./longueur_syllabique.py`.

## Lancer l'analyse

Ce logiciel utilise la base de donnée fréquentielle [Lexique](http://www.lexique.org/).

```sh
./freq_pied.py path/to/lexique.tsv
./longueur_syllabique.py path/to/lexique.tsv
```

### Nix

Si [Nix](https://nixos.org/) est installé, il peut mettre en place automatiquement un environnement de développement avec toutes les dépendances.

```sh
nix-shell
./freq_pied.py
./longueur_syllabique.py
```
