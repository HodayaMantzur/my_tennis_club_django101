<<<<<<< HEAD
from django.shortcuts import redirect, render

from courts.models import Court

def courts(request):
  courts = Court.objects.all()
  context = {
    'courts': courts,
  }
  return render(request, "all_courts.html", context)


def reserve(request, id):
  court = Court.objects.get(id=id)
  court.is_occupied = True
  court.save()
=======
from django.shortcuts import redirect, render

from courts.models import Court

def courts(request):
  courts = Court.objects.all()
  context = {
    'courts': courts,
  }
  return render(request, "all_courts.html", context)


def reserve(request, id):
  court = Court.objects.get(id=id)
  court.is_occupied = True
  court.save()
>>>>>>> 6a028d562591f51c2fd9f4d8900b788561431771
  return redirect('/courts/')