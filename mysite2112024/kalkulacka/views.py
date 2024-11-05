from django.shortcuts import render

from . import models

def index(request):
    error_msg = None
    vysledok = None
    if request.method == "POST":
        try:
            float(request.POST["prva"])
            float(request.POST["druha"])
        except:
            error_msg = "Prva alebo Druha hodnota nie je cislo!"
            return render(request, "kalkulacka/index.html", dict(error_msg=error_msg, vysledok=vysledok))
        
        if request.POST["operacia"] == "/" and float(request.POST["druha"]) == 0:
            error_msg = "Nedá sa deliť nulou!"
            return render(request, "kalkulacka/index.html", dict(error_msg=error_msg, vysledok=vysledok))
        if request.POST["operacia"] == "+":
            vysledok = models.spocitaj(request.POST["prva"], request.POST["druha"])
        elif request.POST["operacia"] == "-":
            vysledok = models.odpocitaj(request.POST["prva"], request.POST["druha"])
        elif request.POST["operacia"] == "*":
            vysledok = models.vynasob(request.POST["prva"], request.POST["druha"])
        elif request.POST["operacia"] == "/":
            vysledok = models.vydel(request.POST["prva"], request.POST["druha"])
        elif request.POST["operacia"] == "**":
            vysledok = models.umocni(request.POST["prva"], request.POST["druha"])
        else:
            error_msg = "Niečo sa pokazilo"
            return render(request, "kalkulacka/index.html", dict(error_msg=error_msg, vysledok=vysledok))
    return render(request, "kalkulacka/index.html", dict(error_msg=error_msg, vysledok=vysledok))