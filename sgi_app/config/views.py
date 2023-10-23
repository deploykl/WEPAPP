from django.shortcuts import render, redirect


def INDEX(request):
    return render(request, "main/login.html", None)