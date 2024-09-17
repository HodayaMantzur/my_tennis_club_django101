<<<<<<< HEAD
from django.shortcuts import render
from members.models import Member

def members(request):
  mymembers = Member.objects.all()
  context = {
    'mymembers': mymembers,
    'name': 'RAN'
  }
  return render(request, "all_members.html", context)


def details(request, id):
  mymember = Member.objects.get(id=id)
  context = {
    'mymember': mymember,
  }
  return render(request, "details.html", context)

=======
from django.shortcuts import render
from members.models import Member

def members(request):
  mymembers = Member.objects.all()
  context = {
    'mymembers': mymembers,
    'name': 'RAN'
  }
  return render(request, "all_members.html", context)


def details(request, id):
  mymember = Member.objects.get(id=id)
  context = {
    'mymember': mymember,
  }
  return render(request, "details.html", context)

>>>>>>> 6a028d562591f51c2fd9f4d8900b788561431771
