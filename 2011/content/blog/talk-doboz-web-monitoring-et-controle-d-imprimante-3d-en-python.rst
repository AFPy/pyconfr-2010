Doboz-web : monitoring et controle  d'imprimante 3d en python
#############################################################
:date: 2011-07-15T21:40:40.518484
:category: talk
:tags: 2011

Doboz-web est projet de systeme de controle et de monitoring pour des imprimantes 3d open source (type Reprap)

* basé sur une structure client / serveur (serveur quasi 100% python pur utilisant Bottle et pyserial , entre autre, pour la gestion des machines )
* permet différentes formes de monitoring (webcam, données 3d etc)
* combine python du coté serveur avec jquery/webgl coté client (fonctionnalité client riche dans une page web)
* axé utilisateur final et multi platformes
* à terme , sous partie d'une application plus grande dédiée à la gestion simplifiée d'un "parc" de Repraps/Arduinos/Réseaux de capteurs

Au cours de la présentation, j'aborderai différents thèmes:

* présentation générale du projet: sans Python, pas réellement possible avec autant de facilité
* difficultés techniques , choix d'architecture
* problématiques multi platformes
* problématiques de la distribution en python : distributions d'Applications et non de Frameworks
 
Infos sur le projet: 

http://www.kaosat.net/?tag=doboz-web
https://github.com/kaosat-dev/Doboz/wiki/Doboz-web

