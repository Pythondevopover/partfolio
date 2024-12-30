from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sizning xabaringiz muvaffaqiyatli yuborildi!')
            return redirect('home')  # Sahifani yangilaydi
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'telegram_link': 'https://t.me/Python_devopover',  # Telegram havolasi
    }
    return render(request, 'contact_us.html', context)
def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)
