from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={'author' : 'Rahim','age' : 20,'lst':['python','is','best','language',],'birthday':datetime.datetime.now(),'val':'', 'courses' :[
        {
            'id':1,
            'name':"django",
            'fee':2000
        },
        {
            'id':2,
            'name':"python",
            'fee':1000
        },
        {
            'id':3,
            'name':"C++",
            'fee':500
        },
    ]}
    return render(request,'home.html',d)
