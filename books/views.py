from django.shortcuts import render

# Create your views here.

def book_details(request):
    # data={
    #     'type':'Math',
    #     "list":['Math Magic','I love Mathemarics','mathematics class 5'],
    # }
    
    # data2=[
    #     {
    #         'title':'Math Magicy',
    #         'autor':'scott Flansburg'
    #     },
    #             {
    #         'title':'I love Mathematics',
    #         'autor':'Usha Pandir'
    #     },
    # ]
    
    data3={
        'math':{'book1':'Math Magic','book2':'I love Mathematics'},
        'Science':{'book1':'Looking Around :Class 5','book2':'Science class 5'}
    }
    return render(request,'books/bookdetails.html',{'data3':data3})

def members(request):
        return render(request,'books/members.html')
    
   