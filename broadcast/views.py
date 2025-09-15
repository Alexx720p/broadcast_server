from django.http import JsonResponse
from .redis_client import redis_client


def connected_clients(request):
    clients = redis_client.smembers('connected_clients')
    details = []
    for client_id in clients:
        info = redis_client.hgetall(f'client: {client_id.decode()}')
        decoded_info = {k.decode(): v.decode() for k, v in info.items()}
        details.append({'id': client_id.decode(), **decoded_info})
    return JsonResponse({'connected_clients': details})