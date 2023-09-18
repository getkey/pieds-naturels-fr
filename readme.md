# Pieds poétiques naturels en francitan

Le but de ce logiciel est de calculer quels types de pieds poétiques correspondent à la prosodie francitane. Autrement dit, quels pieds semblent naturels à l'oreille.

Pour le moment ce logiciel est assez peu précis, il a 2 façons de calculer l'accent principal et ne calcule aucun accent secondaire. Ceci étant dit, voici les trouvailles:

- les mots oxytons sont à peu près aussi communs que les mots paroxytons (donc les ïambes que les trochées, et les anapestes que les amphibraques). Voir `./freq_pied.py`.
- une phrase a en moyenne un accent toutes les 4 ou 5 syllabes. Les rythmes avec un nombre de temps similaires devraient donc paraitre plus naturels. Cependant si on fait un parallèle avec la musique, les signatures rythmiques complexes sont difficiles à percevoir correctement. À expérimenter, mais il est probable que les pieds trisyllabiques soit un juste milieu. Voir `./longueur_syllabique.py`.

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
