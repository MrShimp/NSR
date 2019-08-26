from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from backend.functions import *
# Create your views here.


class IndexView(APIView):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Hello, world. You're at the polls index.")


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        #out = read_csv.csv_json()
        out = 1
        response = JsonResponse(out, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response

    def post(self,request, *args, **kwargs):
        #out = read_csv.csv_json()
        out = 1
        response = JsonResponse(out)
        response['Access-Control-Allow-Origin'] = "*"
        return response


class ExploreView(APIView):
    def get(self, request, *args, **kwargs):
        out = get_color_data()
        response = JsonResponse(out, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response


class ExploreView_POST(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        out = get_selected_score(data['feature_name'], data['features'])
        response = JsonResponse(out, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response


class DetailView(APIView):
    def get(self, request, param1, *args, **kwargs):
        target = param1
        out = get_selected_score(target)
        response = JsonResponse(out, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response


class RawDataView(APIView):
    def get(self, request, param1, *args, **kwargs):
        target = param1
        out = get_row_data(target)
        response = JsonResponse(out, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response


class GetNameView(APIView):
    def get(self, request, param1, *args, **kwargs):
        target = param1
        out = getname(target)
        response = JsonResponse(out, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response


class GetVibrancyRankView(APIView):
    def get(self, request, param1, *args, **kwargs):
        target = param1
        out = get_vibrancy_rank(target)
        response = JsonResponse(out, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response


class GetAddress(APIView):
    def get(self, request,  *args, **kwargs):
        target = request.GET.get('address')
        zip = request.GET.get('zip')
        out = get_address_id(target, zip)
        response = JsonResponse(out, safe=False)
        response['Access-Control-Allow-Origin'] = "*"
        return response