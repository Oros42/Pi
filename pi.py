#!/bin/python
# -*- coding: utf-8 -*-
#
# Petit calcul de PI
# 	affiche
#	3.141592653589793
# 	au lieu de Pi ~ 3.14159265358979323846264338327950288419716939937510...
#
# Author : Oros
# Date : 27/06/2014
# Licence : Public domaine
#
# Histoire de ce script :
# J'ai passé ces derniers jours sur un lit d'hôpital.
# Je me faisais franchement chier. Je n'avais aucun
# livre ni feuille ni crayon ni connexion internet sur 
# mon téléphone portable. Je ne sais pas pourquoi mais
# en me remémorant les décimales de Pi, j'ai eu un
# doute sur la 37ème décimales. N'ayant que mon téléphone
# pour coder en python, je me suis dis pas grave comme
# je suis coinsé là, allons écrire un peu de code
# pour trouver ces décimales de Pi :-D
# Je n'ai, encore aujourd'hui, jamais lu d'algo 
# expliquant comment calculé Pi ! Mais voilà,
# j'ai quand même réussit à à écris ce petit
# bout de code ^_^
# Il n'est absolument pas parfait, je n'obtiens que
# 16 décimales mais c'est la même valeur que math.pi :-p

import math
r=100
a=math.sqrt(r*r+r*r)/2
a=math.sqrt(a*a+math.pow(r-a,2))/2
i=16
while i<100000000000:
	i*=2
	a=math.sqrt(a*a+math.pow(r-math.sqrt(r*r-a*a),2))/2
print("Mon calcul de Pi :", ((a/2)*i)/r)
print("Math.pi :", math.pi)
#('Mon calcul de Pi :', 3.141592653589793)
#('Math.pi :', 3.141592653589793)
