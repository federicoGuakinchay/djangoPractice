from django.shortcuts import redirect
from django.urls import reverse, resolve
from django.utils.deprecation import MiddlewareMixin

class AuthenticationMiddleware:
    """Middleware to ensure user authentication."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Reverse URL for login, register, and password reset URLs
        login_url = reverse('users:login')
        home_url = reverse('users:home')
        about_me = reverse('about_me')
        register_urls = [
            reverse('users:register'),
            reverse('users:succes')
        ]

        password_reset_urls = [
            reverse('password_reset'),
            reverse('password_reset_done'),
            reverse('password_reset_complete')
        ]

        # List of allowed URLs without authentication
        allowed_urls = [login_url, *register_urls, home_url,about_me] + password_reset_urls 

        # Get the name of the currently accessed URL path
        resolved_url = resolve(request.path_info)

        # Initialize variables
        confirm_url = []
        reg_res = None

        # If the accessed URL is the confirmation URL, extract uidb64 and token
        if resolved_url.url_name in ['users:confirm_registration', 'password_reset_confirm']:
            parts = request.path_info.split('/')
            if len(parts) >= 5: 
                uidb64 = parts[2]  
                token = parts[3]  

                if resolved_url.url_name == 'users:confirm_registration':
                    confirm_url = [reverse('users:confirm_registration', kwargs={'uidb64': uidb64, 'token': token})]
                    reg_res = 0  # Registration confirmation
                elif resolved_url.url_name == 'password_reset_confirm':
                    confirm_url = [reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})]
                    reg_res = 1  # Password reset confirmation

        # If the user is not authenticated and trying to access a restricted page
        if not request.user.is_authenticated and resolved_url.url_name not in [
            'login', 'register', 'password_reset', 'password_reset_done', 'succes',
            'password_reset_confirm', 'password_reset_complete', 'home', 'confirm_registration','about_me'
        ] + confirm_url + allowed_urls:
            
            if reg_res is not None:
                # Redirect based on confirmation type
                if reg_res == 1:
                    return redirect(f'reset/{uidb64}/{token}')  # page to reset password
                elif reg_res == 0:
                    return redirect(f'accounts/confirm/{uidb64}/{token}') # page to comfirm email 
            else:
                return redirect('users:home')

        # Call the next middleware or view
        response = self.get_response(request)
        return response