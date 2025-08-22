import json
from json import JSONDecodeError
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


def parse_numbers(request):
    try:
        data = json.loads(request.body)
    except JSONDecodeError:
        return None, None, JsonResponse({"error": "Invalid JSON"}, status=400)

    A = data.get("A")
    B = data.get("B")

    if not isinstance(A, (int, float)) or not isinstance(B, (int, float)):
        return None, None, JsonResponse({"error": "A and B must be numbers"}, status=400)

    return A, B, None


@csrf_exempt
def add(request):
    if request.method == "POST":
        A, B, error = parse_numbers(request)
        if error:
            return error
        return JsonResponse({"answer": A + B})
    return HttpResponseNotAllowed(["POST"])


@csrf_exempt
def subtract(request):
    if request.method == "POST":
        A, B, error = parse_numbers(request)
        if error:
            return error
        return JsonResponse({"answer": A - B})
    return HttpResponseNotAllowed(["POST"])


@csrf_exempt
def multiply(request):
    if request.method == "POST":
        A, B, error = parse_numbers(request)
        if error:
            return error
        return JsonResponse({"answer": A * B})
    return HttpResponseNotAllowed(["POST"])


@csrf_exempt
def divide(request):
    if request.method == "POST":
        A, B, error = parse_numbers(request)
        if error:
            return error
        if B == 0:
            return JsonResponse({"error": "Division by zero!"}, status=400)
        return JsonResponse({"answer": A / B})
    return HttpResponseNotAllowed(["POST"])
