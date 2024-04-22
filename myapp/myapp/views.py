from django.http import HttpResponse

from .service.KafkaService import KafkaService

def myView(request):
    print("hello!")
    service = KafkaService()
    service.send_message("test", "my message")
    return HttpResponse("message sent")