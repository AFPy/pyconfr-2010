Python et le monde de la formation
##################################
:date: 2011-07-23T10:14:29.037363
:category: talk
:tags: 2011

Python est un langage reconnu pour sa facilité d'apprentissage ce qui fait qu'il
préconisé comme langage d'apprentissage en seconde[1].

Toutefois Python peut aussi jouer un rôle de l'autre côté de la barrière, pour
les concepteurs de contenu. Ou plutôt pourrait, car pour l'instant, il n'est
guère utilisé.

Nous verrons l'état des lieux des outils d'authoring (eXe), des LMS (??, faute
de bibliothèque SCORM disponible).

Python est toutefois utilisé en périphérie de projets à vocation e-learning
comme Second Life (les sites tournent sous django.)

Toutefois Python peut apporter beaucoup et je l'utilise actuellement en
interne pour :

- Mettre en place les packages SCORM à partir de templates, en ce basant sur des
  cartes MindManager établis par les concepteurs de contenu. SCORM étant avant
  tout basé sur XML pour décrire le contenu, lxml est mis à contribution.
- Produire certaines métadonnées comme la durée d'apprentissage à partir de la
  longueur des ressources (nombres de pages PDFs avec pyPDF, durée des vidéos
  avec pyFFMPEG, etc.)
- Synchroniser le contenu en production (paramiko). Permet en particulier la
  synchronisation y compris depuis Windows.

Ici, la qualité des bibliothèques Python est déterminante.

L'avenir :

- Concevoir une lib SCORM python pour pouvoir concevoir des LMS (une fois la
  lib SCORM, construire un LMS autour de Pinax serait trivial.)
- A moyen terme, SCORM sera remplacé par une API de notification permettant un
  apprentissage distribué (dans le navigateur, sur les smartphones, les
  tablettes, des simulateurs, des robots industriels…) Python pourra être
  utilisé pour certains contenus, ainsi que pour le backend récupérant les
  notifications pour élaborer des tableaux de bord de suivi des apprenants.

[1]: http://algo.jeanlepine.com/python_05.pdf

