Intégration continue avec apycot
################################
:date: 2010-07-13T19:14:11.304178
:category: talk
:tags: 2010

`apycot`_ est un outil d'intégration continue permettant de lancer une série
de tests automatiques lorsqu'un changement est détecté dans un entrepôt de
gestion de sources (svn ou mercurial).

La plateforme fournit déjà un ensemble de plugins permettant de s'assurer que
les tests unitaires passent (unittest, py.test), que la couverture de code est suffisante (pycoverage),
que le code respecte les conventions de codage du projet (pylint), que des bugs ne sont
pas détectés (pylint, pychecker) ainsi que certains autres autour du packaging (distutils, debian).

Cette présentation a pour but de présenter l'outil et ses possibilités, qui ne se limitent
pas au monde python, ainsi qu'un exemple concret d'utilisation par l'équipe de développement
de `mercurial`_ avec le site `hgpycot`_.

Enfin, la présentation conclura en exposant les évolutions futures, en particulier la
maintenance d'entrepôts debian/ubuntu et établira un comparatif avec les outils
existants comme `buildbot`_.


.. _apycot: http://www.logilab.org/project/apycot
.. _mercurial: http://mercurial.selenic.com/
.. _hgpycot: http://apycot.hg-scm.org/
.. _buildbot: http://buildbot.net/

