from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from .models import TourGuide, TourGuideSerializer, Tour, TourSerializer

class TourGuideView(APIView):
    def get(self, request):

        all_entries = TourGuide.objects.all()
        #serialize de contact
        serializer = TourGuideSerializer(all_entries, many=True)
        #include it on the response
        return Response(serializer.data)
    
class SingleTourGuideView(APIView):#this goes to tourguide full profile
    def get(self, request, tourguide_id):
            singletourguide = TourGuide.objects.get(id=tourguide_id)
            
            serializer = TourGuideSerializer(singletourguide, many=False)
        #include it on the response
            return Response(serializer.data)
    def put(self, request):
        
        body_unicode = request.body.decode('utf-8')
        c = json.loads(body_unicode) #c=requestobject
        # create the new contact
        p = TourGuide(gender=c['gender'], name=c['name'], oneliner=c['oneliner'], image=c['image'])
        #save the contact
        p.save()
        serializer = TourGuideSerializer(p, many=False)
        
        #include it on the response
        return Response(serializer.data)
    
    def post(self, request, tourguide_id):
            
            body_unicode = request.body.decode('utf-8')
            c = json.loads(body_unicode)
        
            # new_tour_guide = TourGuide(gender=c['gender'], name=c['name'], oneliner=c['oneliner'], image=c['image'])
            guide_to_edit=TourGuide.objects.get(id=tourguide_id)
            guide_to_edit.gender=c['gender']
            guide_to_edit.name=c['name']
            guide_to_edit.oneliner=c['oneliner']
            guide_to_edit.image=c['image']
            guide_to_edit.save()
            
            serializer = TourGuideSerializer(guide_to_edit, many=False)
            return Response(serializer.data)
    def delete(self, request, tourguide_id):
            
            body_unicode = request.body.decode('utf-8')
            c = json.loads(body_unicode)
            guide_to_delete=TourGuide.objects.filter(id=tourguide_id).delete()
            # guide_to_delete.save()
            serializer = TourGuideSerializer(guide_to_delete, many=False)
            return Response(serializer.data)
class SingleTourView(APIView): #this goes to tourguide full profile
    def get(self, request, tour_id):
            singletour = Tour.objects.get(id=tour_id)
            
            serializer = TourSerializer(singletour, many=False)
        #include it on the response
            return Response(serializer.data)
    def put(self, request):
        
        body_unicode = request.body.decode('utf-8')
        c = json.loads(body_unicode) #c=requestobject
        # create the new contact
        d = Tour(title=c['title'], tour_summary=c['tour_summary'], cost=c['cost'], guests=c['guests'], image=c['image'], category=c['category'])
        #save the contact
        d.save()
        serializer = TourSerializer(d, many=False)
        
        #include it on the response
        return Response(serializer.data)
    
    def post(self, request, tour_id):
            
            body_unicode = request.body.decode('utf-8')
            c = json.loads(body_unicode)
        
            # new_tour_guide = TourGuide(gender=c['gender'], name=c['name'], oneliner=c['oneliner'], image=c['image'])
            tour_to_edit=Tour.objects.get(id=tour_id)
            tour_to_edit.title=c['title']
            tour_to_edit.tour_summary=c['tour_summary']
            tour_to_edit.cost=c['cost']
            tour_to_edit.image=c['category']
            tour_to_edit.category=c['category']
            tour_to_edit.save()
            
            serializer = TourSerializer(tour_to_edit, many=False)
            return Response(serializer.data)
    def delete(self,request, tour_id):
            
            body_unicode = request.body.decode('utf-8')
            c = json.loads(body_unicode)
            tour_to_delete=Tour.objects.filter(id=tour_id).delete()
            # guide_to_delete.save()
            serializer = TourSerializer(tour_to_delete, many=False)
            return Response(serializer.data)

