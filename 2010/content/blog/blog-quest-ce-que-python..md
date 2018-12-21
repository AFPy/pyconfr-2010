---
Title: Qu’est ce que Python?
Date: 2010-07-01T23:41:37.954499
Category: blog
Tags: 2010

<p>
 Python est un langage de programmation haut niveau, interprété, au typage dynamique et à la gestion automatique de la mémoire. Il supporte plusieurs paradigmes ... Oops! Je m’emballe!
</p>
<center><p>
 <img src="http://www.python.org/community/logos/python-logo-master-v3-TM.png" width="566" height="191" alt=""/></p></center>
<p>
 Reprennons...
 <a href="http://www.python.org/~guido/">
  Guido van Rossum
 </a>
 (le
 <b>B</b>enevolent
 <b>D</b>ictator
 <b>F</b>or
 <b>L</b>ife de Python) créé la première release du langage en Février 1991. Il nomme alors son projet Python en référence aux émissions des
 <a href="http://fr.wikipedia.org/wiki/Monty_Python">
  Monthy Python
 </a>
 qui lui offrent un peu de distraction dans ces longues soirées de coding. Une grande partie des développements est effectuée entre 1991 et 2000 au
 <a href="http://www.cnri.reston.va.us/">
  CNRI
 </a>
 à Reston. Depuis 2000, l'équipe de développeurs maintiennent le langage au travers de l'organisme
 <a href="http://www.pythonlabs.com/">
  Python Lab
 </a>. Python est entièrement
 <a href="http://www.opensource.org/">
  Open Source
 </a>
 et sa propriété intellectuelle est surveillée par une association à but non lucratif nommée
 <a href="http://www.python.org/psf/">
  Python Software Fundation
 </a>.
</p>
<p>
</p>
<br/><br/><center><table cellspacing="0" cellpadding="0"><tr><td align="center">
   <p>
    <img src="http://www.python.org/~guido/images/license.jpg" width="281" height="211" alt=""/></p>
  </td>
 </tr><tr><td align="center">
   <p style="font-size: 0.8em; padding: 5px">
    La licence officielle de Python!
   </p>
  </td>
 </tr></table></center>
<br/><p>
</p>
<p>
 Python est suffisamment simple pour être utilisé par des programmeurs débutants, cependant il est également assez complet pour répondre à toutes les contraintes du milieu professionnel. En quelques mots voici les principaux points de la philosophie de Python : syntaxe simple, interactif, qualité, productivité, intégration. Ces points font de lui un langage très attractif. Dans
 <a href="http://books.google.com/books?id=5zYVUIl7F0QC&amp;printsec=frontcover">
  Programming Python
 </a>
 Mark Lutz nous met en garde: “ You should be warned, thoughonce you start using Python, you may never want to go back. ”
</p>
<p>
</p>
<p>
 Les évolutions et les grandes lignes du langage se font au travers des
 <a href="http://www.python.org/dev/peps/">
  PEP</a>s (<b>P</b>ython <b>E</b>nhancement <b>P</b>roposal). Afin d’illustrer un plus précisément cette philosophie, nous recommandont les 2 PEPs suivantes, fondatrices et connues de tout bon développeur Python :
</p>
<p>
</p>
<p style="padding-left: 80px;">
 ●
 <a href="http://www.python.org/dev/peps/pep-0008/">
  PEP 8
 </a>
 - Style Guide for Python Code : Cela évite les questions existentielles!
 <br/>
 ●
 <a href="http://www.python.org/dev/peps/pep-0020/">
  PEP 20
 </a>
 - The Zen of Python : Parfaite pour les Tee Shirts ;)
</p>
<p>
</p>
<p>
On dit de Python qu’il est livré “batteries incluses”, soulignant ainsi qu’il permet, sans modules supplémentaires, de créer des interfaces graphiques, parser ou sérializer différents types de contenus, créer un server web ou envoyer une requête, etc. Il comprend aussi des librairies pour son apprentissage, exemple avec le module <i>turtle</i>:
</p>
<p>
</p>
<center><table cellspacing="0" cellpadding="0" width="560px"><tr><td style="font-family: 'courier', sans-serif; font-weight: bold; vertical-align: middle;">
~$ python
    <br/>
&gt;&gt;&gt; import turtle
    <br/>
&gt;&gt;&gt; for i in range(4):
    <br/>
...     turtle.forward(100)
    <br/>
...     turtle.left(90)
    <br/>
... 
    <br/>
&gt;&gt;&gt; 
    <br/></td>
  <td>
   <center><p>
    <img src="http://www.bewype.org/pyconfr-android/turtle.png" width="182" height="179" alt=""/></p>
   <p style="font-size: 0.8em; padding: 5px">
    Une belle tortue ;)
   </p></center>
  </td>
 </tr></table></center>
<p>
</p>
<br/><br/><p>
 ... ou encore ce texte à méditer, lui aussi built-in et dont les sources sont impénétrables ;)
</p>
<p>
</p>
<p style="font-family: 'courier', sans-serif; font-weight: bold; padding-left: 80px;">
~$ python
 <br/>
 &gt;&gt;&gt; import this
 <br/>
 The Zen of Python, by Tim Peters
 <br/><br/>
 Beautiful is better than ugly.
 <br/>
 Explicit is better than implicit.
 <br/>
 Simple is better than complex.
 <br/>
 Complex is better than complicated.
 <br/>
 Flat is better than nested.
 <br/>
 Sparse is better than dense.
 <br/>
 Readability counts.
 <br/>
 Special cases aren't special enough to break the rules.
 <br/>
 Although practicality beats purity.
 <br/>
 Errors should never pass silently.
 <br/>
 Unless explicitly silenced.
 <br/>
 In the face of ambiguity, refuse the temptation to guess.
 <br/>
 There should be one-- and preferably only one --obvious way to do it.
 <br/>
 Although that way may not be obvious at first unless you're Dutch.
 <br/>
 Now is better than never.
 <br/>
 Although never is often better than *right* now.
 <br/>
 If the implementation is hard to explain, it's a bad idea.
 <br/>
 If the implementation is easy to explain, it may be a good idea.
 <br/>
 Namespaces are one honking great idea -- let's do more of those!
 <br/>
 &gt;&gt;&gt;
</p>

<br/><br/><p>
 Aujourd’hui Python est souvent utilisé comme langage de script pour le développement web car il en facilite le design et la maintenance. Simple à intégrer, il est inclus dans des applications comme Maya, Blender, GIMP, Inkscape, Paint Shop Pro , ArcGIS. Il est installé de base dans Mac OS et la plupart des distributions Linux. Fedora l'utilise dans son programme d'installation Anaconda. L'application emerge pour la gestion des packages Gentoo est écrite en pure Python. Mais encore, une partie importante des logiciels pour le projet One Laptop Per Child sont écrites en Python. Principalement écris en AINSI C , il offre des performances intéressantes et une grande portabilité. Le site Python.org propose une liste complète des différents domaines d’applications couverts et une liste de retours d’expériences aux pages suivantes:
</p>
<p>
</p>
<p style="padding-left: 80px;">
 ●
 <a href="http://www.python.org/about/apps/">
  Application Domains
 </a>
 <br/>
 ●
 <a href="http://www.python.org/about/success/">
  Python Sucess Stories
 </a>
 , pourquoi pas vous ?;)
</p>
<p>
</p>
<p>
 Notons que les entreprises suivantes l'utilise abondamment: YouTube , Google , Yahoo! , CERN , NASA ... voir
 <a href="http://www.python.org/about/quotes/">
  Quotes about Python
 </a>.
</p>
<p>
</p>
<br/><center><table cellspacing="0" cellpadding="0"><tr><td align="center">
   <p>
    <img src="http://martianchronicles.files.wordpress.com/2009/07/space_shuttle_launch.jpg" width="333" height="280" alt=""/></p>
  </td>
 </tr><tr><td align="center">
   <p style="font-size: 0.8em; padding: 5px">
    Three, two, one...Ignition!
   </p>
  </td>
 </tr></table></center>
<br/><p>
 Pour ma part je dirais que quelques best-pratices ont eu raison de moi:
</p>
<p style="padding-left: 80px;">
 ● l’utilisation de
 <a href="http://pypi.python.org/pypi">
  PyPI
 </a>
 (<b>Py</b>thon <b>P</b>ackage <b>I</b>ndex) pour partager et récupérer une librairie
 <br/>
 ● l’utilisation de
 <a href="http://virtualenv.openplans.org/">
  virtualenv
 </a>
 pour travailler sur plusieurs projets sans risque de conflits ou d’oublis de dépendances
 <br/>
 ● l’interpréteur
 <a href="http://ipython.scipy.org/moin/">
  IPython
 </a>
 pour essayer rapidement une méthode ou un type
 <br/>
 ● enfin setup.py commun à toutes les librairies Python et qui assure l’installation, la gestion des dépendances, le déploiement, les tests unitaires sans aucun outil supplémentaire <em style="font-weight: lighter;">(*sauf setuptools) ....</em>
</p>
<p>
</p>
<p>
 Intéressant non? Ce n’est qu’un début, venez à
 <a href="http://www.pycon.fr/conference/edition2010">
  PYCONFR 2010
 </a>
 , c’est l’occasion de découvrir, d’approfondir et de partager nos connaissances autour d’un langage qui a encore beaucoup à nous offrir et qui ne cesse jamais de nous étonner ;)
</p>
<br/><br/>

