from django.shortcuts import render

from .models import MenuItem

def menu(request):
    top_level_items = MenuItem.objects.filter(parent=None)
    return render(request, 'menu.html', {'top_level_items': top_level_items})

def navbarview(request):
    top_level_items = MenuItem.objects.filter(parent=None)
    return render(request, 'base.html', {'top_level_items': top_level_items})
    # return render(request,'base.html')


# from django.shortcuts import render
# from .models import MenuItem

# def menu(request):
#     menu_items = MenuItem.objects.all()
#     return render(request, 'menu.html', {'menu_items': menu_items})