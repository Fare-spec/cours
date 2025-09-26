#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 09:15:57 2025

@author: elouan.fare
"""


def creer_liste():
    return ()


def est_vide(liste):
    return len(liste) == 0


def ajouter(liste, element):
    return (element, liste)


def tete(liste):
    assert not (est_vide(liste)), "Liste vide"
    element, _ = liste
    return element


def queue(liste):
    assert not (est_vide(liste)), "Liste vide"
    _, reste = liste
    return reste
