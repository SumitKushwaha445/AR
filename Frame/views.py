from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import default_storage
from django.contrib import messages
import pyrebase
import firebase
from firebase_admin import credentials, auth



config={
    'apiKey': "AIzaSyC-fHf5xZVbjVZyYox7WcybHSBkzwcTiqc",
    'authDomain': "artify-102aa.firebaseapp.com",
    'projectId': "artify-102aa",
    'storageBucket': "artify-102aa.appspot.com",
    'messagingSenderId': "235969339174",
    'appId': "1:235969339174:web:f9a6bd6c5227aaaf512be7",
    'measurementId': "G-4V3XYJVJL6"
}

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);



def signup_login(request):

    if request.method == "POST" and "register" in request.POST:
        # Code for user registration
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        newuser = User.objects.create_user(username=username, email=email, password=password)
        newuser.save()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect("/base")
        else:
            print("error")

    elif request.method == "POST" and "login" in request.POST:
        # Code for user login
        if request.user.is_authenticated:
            return redirect("/home")
        else:
            username = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect("/base")
            else:
                print("error")

    return render(request, 'login.html')







