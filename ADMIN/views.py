from django.shortcuts import render
from . models import itemtable

# Create your views here.
def fileupload(request):

    if request.method=='POST':
        itemname=request.POST.get('itemname')
        itemprice=request.POST.get('itemprice')
        itemdecription=request.POST.get('itemdecription')
        picture=request.FILES.get('picture')
        obj=itemtable.objects.create(itemname=itemname,itemprice=itemprice,itemdecription=itemdecription,picture=picture)
        obj.save()
        if obj:
            message="file upload successfully"
            return render(request,'items.html',{"success":message})
        else:
             return render(request,'items.html')
    else:
        return render(request,'items.html')

        