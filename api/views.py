from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def hello(request):
    return Response({
        "message": "Hello from my CSC325 CI/CD project<3",
        "course": "CSC325"
    })