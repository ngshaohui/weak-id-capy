from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
import random
from redeem.models import Coupon, ManualProtection
from django.db.models import F
from .utils import get_random_coupon_code
import re

NUM_COUPONS = 128


def __generate_nonce(length: int = 0) -> str:
    if length == 0:
        length = random.randrange(0, 42)
    return length * '\u200B'


def landing(request):
    total_count = Coupon.objects.all().count()
    available_count = Coupon.objects.filter(status=False).count()
    serials = range(1, total_count + 1)
    zero_pad = map(lambda x: f'coupon-status/capybara/100{x:03}/', serials)
    return render(
        request,
        "landing.html",
        {
            'range': zero_pad,
            "total_count": total_count,
            "available": available_count
        }
    )


def coupon_status(request, serial):
    ManualProtection.objects.filter(id=1).update(attempts=F('attempts') + 1)
    attempts = ManualProtection.objects.get(id=1).attempts

    timeout = 0
    if attempts >= 20 and attempts < 100:
        timeout = 3
    elif attempts >= 100:
        timeout = 8

    match = re.search(r'^10(\d+)$', serial)
    if not match:
        # TODO test
        return render(
            request,
            "missing.html",
            {"serial": serial}
        )
    coupon = Coupon.objects.get(id=match.group(1))

    # prevent sorting by length
    nonce = __generate_nonce()

    if not coupon.status:
        return render(
            request,
            "success.html",
            {
                "nonce": nonce,
                "timeout": timeout,
                "serial": serial,
                "code": coupon.code
            }
        )
    else:
        return render(
            request,
            "failure.html",
            {
                "nonce": nonce,
                "timeout": timeout,
                "serial": serial,
                "code": coupon.code
            }
        )


def redeem(request):
    message = None
    status = None

    if request.method == 'POST':
        code = request.POST.get('coupon_code', '').strip().lower()

        try:
            coupon = Coupon.objects.get(code=code)
            if coupon.status:
                message = f"Coupon '{code}' has already been redeemed."
                status = 'warning'
            else:
                coupon.status = True
                coupon.save()
                message = f"Coupon '{code}' successfully redeemed! Enjoy your capy"
                status = 'success'
        except Coupon.DoesNotExist:
            message = f"Coupon '{code}' is not valid."
            status = 'danger'

    return render(request, 'hidden-redemption.html', {
        'message': message,
        'status': status,
    })


def seed():
    # Delete existing posts
    Coupon.objects.all().delete()
    ManualProtection.objects.all().delete()

    coupon_codes = get_random_coupon_code(128)
    # Randomly select 5 codes to be marked as unavailable (status=False)
    unavailable_codes = set(random.sample(coupon_codes, 5))

    for idx, code in enumerate(coupon_codes, start=1):
        Coupon.objects.create(
            id=idx,
            code=code,
            status=(code not in unavailable_codes),
            updated_at=timezone.now(),
        )

    ManualProtection.objects.get_or_create(
        id=1,
        defaults={'attempts': 0},
    )
    # this is for debug
    print("seeded for")
    for code in unavailable_codes:
        print(code)


def reset(request):
    # this reset does nothing
    if request.method == "POST":
        confirm = request.POST.get('confirm')

        if confirm != "confirm":
            return JsonResponse({"success": False})

        seed()
        return redirect("/")
    else:
        return render(request, "reset.html")
