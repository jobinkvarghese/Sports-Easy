from django.shortcuts import render
from . models import itemtable

# Create your views here.
def fileupload(request):

    if request.method=='POST':
        itemname=request.POST.get('itemname')
        itemprice=request.POST.get('itemprice')
        itemdescription=request.POST.get('itemdescription')
        picture=request.FILES.get('picture')
        brand=request.POST.get('brand')
        seller=request.POST.get('seller')
        status=request.POST.get('status')
        colour=request.POST.get('colour')
        obj=itemtable.objects.create(itemname=itemname,itemprice=itemprice,itemdescription=itemdescription,picture=picture,brand=brand,seller=seller,status=status,colour=colour)
        obj.save()
        if obj:
            message="file upload successfully"
            return render(request,'items.html',{"success":message})
        else:
             return render(request,'items.html')
    else:
        return render(request,'items.html')

        