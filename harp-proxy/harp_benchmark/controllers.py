from harp.http import HttpResponse, HttpRequest
from harp_apps.proxy.controllers import HttpProxyController

class BenchmarkController(HttpProxyController):
    async def __call__(self, request: HttpRequest) -> HttpResponse:
        if request.method == "GET" and request.path == "/single":
            return HttpResponse( "P", status=200 )
