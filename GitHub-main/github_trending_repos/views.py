# from django.shortcuts import render

import requests
from rest_framework.views import APIView
from rest_framework.response import Response


# Create an API request 
# class Pythonrepoview :
#     url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#     response = requests.get(url)
#     print("Status code: ", response.status_code)
#     # In a variable, save the API response.
#     response_dict = response.json()
#     # Evaluate the results.
#     print(response_dict.keys())
    

class PythonRepoView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        resp = requests.get(url=url)
        response_data = resp.json()
        print(response_data)             
        return Response(response_data) 
   
class CRepoView(APIView):
    def get(self,request):
        url = 'https://api.github.com/search/repositories?q=language:c&sort=stars'
        resp = requests.get(url=url)
        response_data = resp.json()
        print(response_data)             
        return Response(response_data) 
   
class CplusplusRepoView(APIView):
    def get(self,request):
        url = 'https://api.github.com/search/repositories?q=language:c++&sort=stars'
        resp = requests.get(url=url)
        response_data = resp.json()
        print(response_data)             
        return Response(response_data) 

class JavaRepoView(APIView):
    def get(self,request):
        url = 'https://api.github.com/search/repositories?q=language:java&sort=starss'
        resp = requests.get(url=url)
        response_data = resp.json()
        print(response_data)             
        return Response(response_data) 



    
















# Create your views here
