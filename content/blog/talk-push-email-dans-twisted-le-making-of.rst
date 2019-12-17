"Push-email" dans Twisted: le making-of
#######################################
:date: 2010-07-13T23:35:22.704075
:category: talk
:tags: 2010

Le projet Twisted est un ensemble de modules, de classes et de
fonctions qui permettent de construire efficacement des applications
réseau performantes et robustes.

Ce framework réseau couvre en particulier les protocoles d'emails:
SMTP, POP et IMAP. Par contre, Twisted ne fournit pas une extension du
standard IMAP: la commande *IDLE* qui permet le *push email*, c'est a
dire une methode d'acces aux emails plus performante: elle offre une
latence moindre, tout en diminuant la charge du serveur.

Apres une introduction sur les points cles de Twisted, cette
presentation montre les etapes d'une implementation de cette
extension d'IMAP dans Twisted :

1. la réalisation d'un prototype du mécanisme de notification serveur
   vers client, avec les abstractions du framework,

2. puis l'architecture du module IMAP dans Twisted et le portage du
   prototype dans ces classes,

3. ensuite, les tests d'intégration avec les serveurs largement
   utilises: Dovecot et Gmail,

4. enfin, l'adoption des méthodes du projet Twisted qui conditionnent
   la revue du code et son eventuelle integration

