from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View

class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, self.template_name)

        try:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, self.template_name)
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, self.template_name)

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, self.template_name)
