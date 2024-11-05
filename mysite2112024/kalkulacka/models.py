from django.db import models

def spocitaj(prva, druha):
    return float(prva) + float(druha)

def odpocitaj(prva, druha):
    return float(prva) - float(druha)

def vynasob(prva, druha):
    return float(prva) * float(druha)

def vydel(prva,druha):
    return float(prva) / float(druha)

def umocni(prva,druha):
    return float(prva) ** float(druha)