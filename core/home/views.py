from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .utils import send_email_to_user, send_email_with_attachment
from django.conf import settings


# Create your views here.


def home(request):
    peoples = [
        {'name': "John Curry", "age": 30},
        {'name': "Jay Wilson", "age": 34},
        {'name': "John Cole", "age": 22},
        {'name': "Jay Murray", "age": 44},
        {'name': "John Jeffrey", "age": 65},
    ]
    return render(request=request, template_name="home/index.html", context={"peoples": peoples})


def about(request: HttpRequest):
    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis porta quis arcu vitae placerat. Nullam et dignissim odio, sit amet blandit neque. Praesent sit amet purus neque. Pellentesque a lorem erat. Vivamus ultrices mi interdum metus finibus iaculis. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum consectetur sem a commodo tristique. Aliquam sit amet bibendum arcu. Proin scelerisque risus a sapien rutrum finibus. Suspendisse elit diam, ornare et sagittis ac, efficitur convallis erat. Sed id ullamcorper felis. Ut egestas neque urna. Phasellus tellus turpis, fermentum a rutrum vel, interdum non mi.

Interdum et malesuada fames ac ante ipsum primis in faucibus. Aenean sed ligula eleifend, aliquet erat ac, viverra elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aenean tincidunt dolor vulputate neque mollis blandit. Vestibulum sed nulla eros. In tristique ligula eget justo dictum, sed rhoncus velit luctus. Interdum et malesuada fames ac ante ipsum primis in faucibus.

Morbi aliquet egestas elit, id viverra elit cursus ac. Curabitur a lorem in ex commodo tristique nec eu urna. Suspendisse auctor porttitor nisl quis consectetur. Nam elementum, neque vitae porttitor mattis, eros nibh mattis nulla, a gravida nisi nisl eu lorem. Nulla nec placerat lectus, ac faucibus velit. Aliquam vehicula pharetra enim, et gravida turpis porta ac. Duis sit amet nisi interdum tellus interdum maximus iaculis non ligula. Duis augue lacus, dictum nec sapien ut, tincidunt vehicula sapien. Proin justo augue, euismod non lobortis quis, ullamcorper quis mauris. Aenean ullamcorper rutrum orci non bibendum. Donec vel lacinia libero. Nam molestie arcu vitae tortor dignissim scelerisque. Integer eu dictum quam.

Cras libero tortor, elementum ut turpis vel, suscipit commodo dolor. Etiam dignissim, ipsum vel lacinia euismod, risus magna facilisis quam, eget eleifend tellus nibh tristique augue. Suspendisse magna elit, consectetur vel libero at, aliquet blandit magna. Duis et egestas nunc, et euismod sapien. Curabitur ac justo sit amet purus efficitur placerat ut sed massa. Donec enim risus, fermentum a luctus quis, tincidunt a ex. Mauris placerat fermentum nisl. Nullam eu lectus vitae sapien tristique auctor. Cras efficitur sem ex, in rhoncus orci luctus ac. Sed convallis id orci mattis condimentum. Cras non lacinia turpis. Cras interdum lobortis sapien, nec ultricies augue bibendum scelerisque. Suspendisse nibh elit, aliquam vitae dolor id, ultricies dignissim augue. In rhoncus metus tristique, tempor ipsum vehicula, dapibus mi. Ut sagittis aliquam mauris, ut sollicitudin risus tincidunt ut.

Nulla sed rutrum ante. Nulla vehicula dignissim hendrerit. Nullam quis volutpat neque, vitae ultricies magna. Morbi ultrices sit amet purus non fringilla. Sed et sollicitudin leo, a consectetur ipsum. Vivamus commodo cursus hendrerit. Etiam pretium pellentesque orci ac finibus. Donec malesuada iaculis varius.
    """
    return render(request=request, template_name="home/about.html", context={'text': text})


def contact(request: HttpRequest):

    return render(request=request, template_name="home/contact.html")


def success_page(request: HttpRequest):
    return HttpResponse("""
                        <body>
                        <h1 style="text-align:center">Success page</h1>
                        </body>
                        """)


def send_mail_route(request):
    # send_email_to_user()
    file_path = f"{settings.BASE_DIR}/chicken.webp"
    send_email_with_attachment(file_path=file_path)
    return redirect("/")
