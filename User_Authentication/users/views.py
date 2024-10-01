from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# for email confirm
from django.contrib.auth.models import User
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from .signals import send_confirmation_email

# for users views 
from django.views.generic import DetailView


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save to the database yet
            user.is_active = False          # Mark user as inactive until email confirmation
            user.save()
            send_confirmation_email(sender=user.__class__, instance=user, created=True)
            messages.success(request, 'Registration successful! Please confirm your email to complete registration.')
            
            return redirect('users:login')  # Redirect to login after showing success message
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@staff_member_required
def admin_view(request):
    return render(request, 'users/admin.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def user_list_view(request):
    query = request.GET.get('q')  # Get the search query from the GET request
    if query:
        # Filter users based on username, first name, or email
        users = User.objects.filter( username__icontains=query)
        return render(request, 'users/user_list.html', {'users': users})
    else:
        users = User.objects.all().order_by("username")
        return render(request, 'users/user_list.html', {'users': users})

@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

def view_404(request):
    return render(request,'404.html')

def confirm_registration(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))          # Decode the base64-encoded user ID
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('users:succes')                         # Redirect to the login page or a success page
    else:
        return render(request, 'invalid_confirmation.html')     # Show an error page if the token is invalid

def succes_registration(request):
    return render(request, 'users/succes.html')

def home(request):
    return render(request, 'home.html')