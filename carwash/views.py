from django.shortcuts import render
from .models import Carwash

def home(request):
    try:
        current_user = request.user
        carwash = Carwash.objects.get(main_user=current_user.id)
        carwash_purchased = int(carwash.carwash_purchased)
        return render(request, 'carwash/home.html', {
            'carwash': carwash,
            'current_user': current_user,
            'carwash_purchased': carwash_purchased,
        })
    except:
        return render(request, 'carwash/home.html', {})        





def enter_code(request):
    return render(request, 'carwash/enter_code.html', {})

def redeem_code(request):
    return render(request, 'carwash/redeem_code.html', {})