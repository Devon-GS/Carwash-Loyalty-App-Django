from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Carwash, LoyaltyCode
import random

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
    if request.method == "POST":
        current_user = request.user
        user_data = Carwash.objects.get(main_user=current_user.id)
        carwash = int(user_data.carwash_purchased)
        used_codes = int(user_data.used_codes)


        data = LoyaltyCode.objects.values_list('loyalty_code', flat=True)[0]
        entered_code = request.POST['loyalty']

        if int(entered_code) == int(data):
            if used_codes == int(entered_code):
                messages.success(request, ('Sorry, That Code Was Already Used'))
                return redirect('enter_code')
            else:
                # Add code to used codes
                user_data.used_codes = entered_code
                user_data.save()

                # Add one carwash to carwashs purchased
                user_data.carwash_purchased = carwash + 1
                user_data.save()

                messages.success(request, ('Code Was Entered Successfully'))
                return redirect('enter_code')
        else:
            messages.success(request, ('Wrong Code, Please Try Again'))
            return redirect('enter_code')
    else:
        return render(request, 'carwash/enter_code.html', {})


def redeem_code(request):
    try:
        current_user = request.user
        user_data = Carwash.objects.get(main_user=current_user.id)
        carwash_purchased = int(user_data.carwash_purchased)
        user_free_code = int(user_data.free_code)
    except:
        messages.success(request, ('There Was An Error Getting Your Profile, Please Try Again'))
        return redirect('home')
    else:
        if carwash_purchased == 9:
            if user_free_code == 0:
                # Create Free Code
                code = []
                for i in range(0,5):
                    x = random.randint(1,10)
                    code.append(x)
                code = ''.join(map(str, code))
                code = int(code)

                # Save Free Code To Database
                user_data.free_code = code
                user_data.save()
            else:
                code = user_free_code

            return render(request, 'carwash/redeem_code.html', {
            'carwash_purchased': carwash_purchased,
            'code': code,
            'user_free_code': user_free_code,
            })   
        else:
            code = 'You still have ' + str(10 - carwash_purchased) + ' car washes to go!'
            return render(request, 'carwash/redeem_code.html', {
                'carwash_purchased': carwash_purchased,
                'code': code,
                'user_free_code': user_free_code,
            })

   