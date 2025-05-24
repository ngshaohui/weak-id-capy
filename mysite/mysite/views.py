from django.http import JsonResponse
from django.shortcuts import redirect, render
import random


def __generate_nonce(length: int = 0) -> str:
    if length == 0:
        length = random.randrange(0, 42)
    return length * '\u200B'


def landing(request):
    serials = range(1, 129)
    zero_pad = map(lambda x: f'redemption/capybara/100{x:03}/', serials)
    return render(request, "landing.html", {'range': zero_pad})


def success(request):
    nonce = __generate_nonce()
    return render(request, "success.html", {"nonce": nonce})


def failure(request):
    nonce = __generate_nonce()
    return render(request, "failure.html", {"nonce": nonce})


def redemption(request, serial):
    nonce = __generate_nonce()
    if serial in [
        "100001",
        "100007",
        "100027",
        "100068",
        "100070",
        "100111",
        "100168",
    ]:
        return render(
            request,
            "success.html",
            {"nonce": nonce, "serial": serial}
        )
    else:
        return render(
            request,
            "failure.html",
            {"nonce": nonce, "serial": serial}
        )


def reset(request):
    # this reset does nothing
    if request.method == "POST":
        confirm = request.POST.get('confirm')

        if confirm != "confirm":
            return JsonResponse({"success": False})

        return redirect("/")
    else:
        return render(request, "reset.html")
