Aiguille et botte de foin: scikit-learn et joblib pour explorer des données volumeuses
######################################################################################
:date: 2010-07-16T22:06:02.127059
:category: talk
:tags: 2010

Que cela soit sous la forme de bases de données, d'images, de textes ou de séries temporelles, les systèmes informatiques modernes accumulent de gros volumes de données.

La fouille de donnée pour extraire des informations pertinentes des univers numériques est normalement réservée à des logiciels spécialisés qui intègrent accès aux données, algorithmes d'apprentissage statistiques et moteurs d'exécution avec bien souvent une interface utilisateur dédiée, des outils de visualisation, ou un langage de script.

Pour permettre d'attaquer des problèmes variés, tant en ce qui concerne le type de données traitées que le contexte d'application, il est important de fournir des briques réutilisables sous forme de librairies.

Je présenterai deux efforts récents allant dans cette direction et qui s'intègrent dans l'univers riche de modules Python pour la gestion de base de données ou le calcul scientifique:

* `scikit-learn <http://scikit-learn.sourceforge.net/>`_: une librairie regroupant des algorithmes d'apprentissage statistique sous forme d'objets s'efforçant d'abstraire les détails mathématiques pour répondre à des cas d'utilisation concret.

* `joblib <http://packages.python.org/joblib/>`_: un projet encore jeune de métaprogrammation pour assembler des fonctions et des objets Python sous forme d'une `pipeline` permettant de traiter efficacement de grosses données. La particularité de `joblib` est d'encourager le développement de code Python classique en évitant le recours à un moteur d'exécution.

L'originalité de l'approche présentée est de séparer moteur d'exécution, algorithmes, et accès aux données pour maximiser la réutilisation de code.

J'illustrerai l'utilisation de ces librairies sur des problèmes d'apprentissage statistique et de fouille de données avec des images et des données textuelles.

