from django.shortcuts import render, redirect
from .forms import ReservationForm


def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')  # Redirect to a success page after successful reservation
    else:
        form = ReservationForm()
    return render(request, 'reservation/reserve.html', {'form': form})
