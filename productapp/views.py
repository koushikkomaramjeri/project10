from django.shortcuts import render,redirect
from django.views import View
from .forms import ProductForm
from django.http import HttpResponse
from .models import Product
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class ProdutInput(View):
    def get(self,request):
        condic={"pform":ProductForm()}
        return render(request,'productinput.html',context=condic)
class ProductInsert(View):
    def get(self,request):
        pf=ProductForm(request.GET)
        if pf.is_valid():
            pf.save()
        return redirect("http://localhost:8000/productsdisplay")
class ProductsDisplay(View):
    def get(self,request):
        qs=Product.objects.all()
        condict={"records":qs}
        return render(request,'productsdisplay.html',context=condict)
class ProductUpdateInput(View):
    def get(self,request):
        qs = Product.objects.all()
        condict = {"records": qs}
        return render(request, 'productupdateinput.html', context=condict)
class ProuductUpdateDetails(View):
    def get(self,request):
        prod=Product.objects.get(pid=request.GET["pid"])
        print(prod.pmfdt)
        con_dic={"pid":prod.pid,'pname':prod.pname,'pcost':prod.pcost,'pmfdt':str(prod.pmfdt),'pexpdt':str(prod.pexpdt)}
        return render(request,'update.html',context=con_dic)
class Update(View):
    def get(self,request):
        p=Product(pid=int(request.GET["t1"]),
                  pname=request.GET["t2"],
                  pcost=float(request.GET["t3"]),
                  pmfdt=request.GET["t4"],
                  pexpdt=request.GET["t5"]
                  )
        p.save()
        return redirect("http://localhost:8000/productsdisplay")
class ProductDeleteInput(View):
    def get(self,request):
        qs = Product.objects.all()
        condict = {"records": qs}
        return render(request, 'productdeleteinput.html', context=condict)
class ProductDelete(View):
    def get(self,request):
        prod=Product.objects.filter(pid=int(request.GET["pid"]))
        prod.delete()
        return redirect("http://localhost:8000/productsdisplay")