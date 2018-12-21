Solutions pour le calcul scientifique intense en mémoire et CPU
###############################################################
:date: 2011-07-08T16:09:43.682854
:category: talk
:tags: 2011

Au sein de l'INRIA Rennes, nous développons une application d'assemblage génomique en Python. Ce type de calcul scientifique nécessite de très grosses ressources. La structure de donnée résidant en mémoire occupe des centaines de gigaoctets. Chaque traitement requiert des milliers d'heures CPU. Pourtant, cette implémentation Python a obtenu des meilleures performances temps/mémoire que les autres outils concurrents écrits en C++, au cours d'une compétition récente (www.assemblathon.org).
Cette présentation décrit comment nous avons combiné des librairies Python pour rendre les calculs efficaces:
- interfaçage d'une table de hachage (google_sparsehash) et d'un graphe (igraph) entre Python et C++ avec SWIG
- calcul distribué client/serveur avec RPyC et parallèle avec multiprocessing
- accélération JIT avec psyco/PyPy

