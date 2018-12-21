Comment Python est développé, vu par un core developer
######################################################
:date: 2011-07-05T22:12:49.432730
:category: talk
:tags: 2011

Python est un logiciel libre développé par une centaine de "core developers" ainsi que des centaines de contributeurs, ponctuels voir occasionnels. Je vais vous présenter comment Python est développé, vu de l'intérieur, du point de vue d'un core developer.

Les nouvelles fonctionnalités, améliorations et corrections de bugs passent par divers canaux de communication : salons IRC, listes de diffusion, et surtout le bug tracker. Chaque canal a son rôle et ses habitués. Les nouvelles fonctionnalités impactant beaucoup de code ou polémiques doivent passer par l'étape d'une PEP (proposition d'améliration de Python).

Le code source de Python anciemment géré par Subversion est passé à Mercurial. Étant donné que 3 versions sont encore actives (2.7, 3.2 et 3.3), ça demande un peu de gymnastique pour corriger un bug dans toutes les branches. Les avantages et incovénients de Mercurial seront rapidement passés en revue.

L'objectif de la présentation est d'expliquer pourquoi certains bugs mettent plusieurs mois à être corrigé, pourquoi certaines demandes de fonctionnalité sont refusées et encore d'encourager à contribuer à Python (tout ça !).

