from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, render
from models import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from reportlab.pdfgen.canvas import Canvas
import reportlab.lib.fonts 
from reportlab.pdfgen import canvas
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from urllib import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
import xhtml2pdf.pisa as pisa
from cStringIO import StringIO
#import sx.pisa3 as pisa

def addrecordfunction(request):    
    if request.POST:
        post = request.POST
        new_salary = Salary(
            name = post["name"],
            year = post["year"],
            total = post["total"],
            remarks = post["remarks"])       
        new_salary.save()
        p = Salary.objects.get(year=post["year"],name=post["name"])
        new_month = Month(
            nameID = p,
            month = post["month1"],
            salary = post["salary1"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month2"],
            salary = post["salary2"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month3"],
            salary = post["salary3"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month4"],
            salary = post["salary4"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month5"],
            salary = post["salary5"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month6"],
            salary = post["salary6"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month7"],
            salary = post["salary7"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month8"],
            salary = post["salary8"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month9"],
            salary = post["salary9"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month10"],
            salary = post["salary10"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month11"],
            salary = post["salary11"]
        )
        new_month.save()
        new_month = Month(
            nameID = p,
            month = post["month12"],
            salary = post["salary12"]
        )
        new_month.save()
        #return HttpResponseRedirect("/salary/")
    return render_to_response("add.html")

def welcomefunction(request):
		return render_to_response("welcome.html")
  
def mainfunction(request):
		return render_to_response("main.html") 

def invoicesearchfunction(request):
    title = ""
    if request.POST:
        title = request.POST["title"]
        p = Invoice.objects.filter(title=title)    
        if len(p) >  0:
            q = Invoice.objects.get(title=title)
            k = InDetail.objects.filter(productionID=q)                  
            c = Context({"invoice_list": p,"detail_list": k})        
            return render_to_response("invoice.html", c)
    return HttpResponseRedirect("/invoicesearch/")

def formfunction(request):
    return render_to_response("formsearch.html")
    
def formsearchfunction(request):
    year = ""
    if request.POST:
        year = request.POST["year"]
        p = Form.objects.filter(year=year)    
        if len(p) >  0:
            q = Form.objects.get(year=year)
            k = FormDetail.objects.filter(yearincomeID=q)                  
            c = Context({"form_list": p,"formdetail_list": k})        
            return render_to_response("form.html", c)
        return HttpResponseRedirect("/formsearch/")
    return HttpResponseRedirect("/formsearch/")
 
def invoicefunction(request):
    invoice_list = Invoice.objects.all()
    c = Context({"invoice_list":invoice_list})
    return render_to_response("invoicesearch.html",c)
 
def invioceupdatefunction(request):
    if request.POST:
        post = request.POST
      	p = Invoice.objects.get(id=post["id"])
        p.title = post["title"]
        p.drawer = post["drawer"]
        p.date = post["date"]
        p.save()
        return HttpResponseRedirect("/invoice/")
    elif request.GET:
    		if len(Invoice.objects.filter(id=request.GET["id"]))>0:
    			invoice = Invoice.objects.get(id=request.GET["id"])
    			c = Context({"p": invoice})
    			return render_to_response("edit_invoice.html", c)
    else:
        return HttpResponseRedirect("/invoice/") 
        
def formupdatefunction(request):
    if request.POST:       
        post = request.POST
      	p = Form.objects.get(id=post["id"])
        p.year = post["year"]
        if len(Form.objects.filter(year = p.year))>0:
            return HttpResponseRedirect("/form/")
        p.save()
        return HttpResponseRedirect("/form/")
    elif request.GET:
    		if len(Form.objects.filter(id=request.GET["id"]))>0:
    			form = Form.objects.get(id=request.GET["id"])
    			c = Context({"p": form})
    			return render_to_response("edit_form.html", c)
    else:
        return HttpResponseRedirect("/form/") 
   
def indetailupdatefunction(request):
    if request.POST:
        post = request.POST
      	p = InDetail.objects.get(id=post["id"])
        p.production = post["production"]
        p.number = post["number"]
        p.Univalent = post["Univalent"]
        p.total = post["total"]        
        p.save()
        return HttpResponseRedirect("/invoice/")
    elif request.GET:
    		if len(InDetail.objects.filter(id=request.GET["id"]))>0:
    			indetail = InDetail.objects.get(id=request.GET["id"])
    			c = Context({"p": indetail})
    			return render_to_response("edit_indetail.html", c)
    else:
        return HttpResponseRedirect("/invoice/") 
        
def formdetailupdatefunction(request):
    if request.POST:
        post = request.POST
      	p = FormDetail.objects.get(id=post["id"])
        p.yearincome = post["yearincome"]
        p.yearcost = post["yearcost"]
        p.sellingexpenses = post["sellingexpenses"]
        p.managementexpenses = post["managementexpenses"] 
        p.financialexpenses = post["financialexpenses"] 
        p.incomefrominvestment = post["incomefrominvestment"] 
        p.save()
        return HttpResponseRedirect("/form/")
    elif request.GET:
    		if len(FormDetail.objects.filter(id=request.GET["id"]))>0:
    			formdetail = FormDetail.objects.get(id=request.GET["id"])
    			c = Context({"p": formdetail})
    			return render_to_response("edit_formdetail.html", c)
    else:
        return HttpResponseRedirect("/form/") 
def indetaildeletefunction(request):
    dltid = request.GET["id"]
    if len(InDetail.objects.filter(id=dltid)) > 0:
        InDetail.objects.filter(id=dltid).delete()
        return HttpResponseRedirect("/invoice/")   
        
def invoicezoomfunction(request):    
    p = Invoice.objects.filter(id=request.GET["id"])
    q = Invoice.objects.get(id=request.GET["id"])
    k = InDetail.objects.filter(productionID=q)
    c = Context({"invoice_list": p,"detail_list": k})
    return render_to_response("zoom_invoice.html",c)

def formzoomfunction(request):    
    p = Form.objects.filter(id=request.GET["id"])
    q = Form.objects.get(id=request.GET["id"])
    k = FormDetail.objects.filter(yearincomeID=q)
    c = Context({"form_list": p,"formdetail_list": k})
    return render_to_response("zoom_form.html",c)
    
def formprintfunction(request):
    form_list = Form.objects.filter(id=request.GET["id"])
    q = Form.objects.get(id=request.GET["id"])
    formdetail_list = FormDetail.objects.filter(yearincomeID=q)
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="form_print.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    for form in form_list: 
        p.drawString(40, 770, "----------------------------------------------------------------------------------------------------------------------------------")
        p.drawString(255, 750, form.year)
        p.drawString(40, 730, "----------------------------------------------------------------------------------------------------------------------------------")
        for k in range(9):        
            p.drawString(40, 765-k*10, "|")
            p.drawString(558, 765-k*10, "|")
            p.drawString(120, 725-k*10, "|")
            p.drawString(200, 725-k*10, "|") 
            p.drawString(300, 725-k*10, "|") 
            p.drawString(390, 725-k*10, "|")
            p.drawString(470, 725-k*10, "|")
        i = 0
        p.drawString(50, 700, "year income")
        p.drawString(140, 700, "year cost")
        p.drawString(210, 700, "selling expenses")
        p.drawString(310, 710, "management")
        p.drawString(310, 695, " expenses")
        p.drawString(400, 710, "financial")
        p.drawString(400, 695, "expenses")
        p.drawString(480, 710, "investment")
        p.drawString(480, 695, "  income")
        p.drawString(40, 680, "----------------------------------------------------------------------------------------------------------------------------------")
        
        for formdetail in formdetail_list:
            p.drawString(80,650-i,formdetail.yearincome)
            p.drawString(155,650-i,formdetail.yearcost)
            p.drawString(240,650-i,formdetail.sellingexpenses)
            p.drawString(340,650-i,formdetail.managementexpenses)
            p.drawString(420,650-i,formdetail.financialexpenses)
            p.drawString(40, 650-i-20, "----------------------------------------------------------------------------------------------------------------------------------")
                        
            for k in range(6):        
                p.drawString(40, 685-i-k*10, "|")
                p.drawString(558, 685-i-k*10, "|") 
                p.drawString(120, 685-i-k*10, "|") 
                p.drawString(200, 685-i-k*10, "|") 
                p.drawString(300, 685-i-k*10, "|") 
                p.drawString(390, 685-i-k*10, "|") 
                p.drawString(470, 685-i-k*10, "|")               
            i+=50
        
       # p.drawString(40, 650-i-20, "------------------------------------------------------------------------------------------------------------")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
    
def invoiceprintfunction(request):   

    invoice_list = Invoice.objects.filter(id=request.GET["id"])
    q = Invoice.objects.get(id=request.GET["id"])
    indetail_list = InDetail.objects.filter(productionID=q)
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice_print.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    for invoice in invoice_list: 
        p.drawString(40, 770, "------------------------------------------------------------------------------------------------------------")
        p.drawString(255, 750, invoice.title)
        p.drawString(40, 730, "------------------------------------------------------------------------------------------------------------")
        for k in range(9):        
            p.drawString(40, 765-k*10, "|")
            p.drawString(470, 765-k*10, "|")
            p.drawString(170, 725-k*10, "|")
            p.drawString(260, 725-k*10, "|") 
            p.drawString(360, 725-k*10, "|") 
        i = 0
        p.drawString(50, 700, "Name of production")
        p.drawString(200, 700, "Number")
        p.drawString(300, 700, "Univalent")
        p.drawString(400, 700, "Total")
        p.drawString(40, 680, "------------------------------------------------------------------------------------------------------------")
        
        for indetail in indetail_list:
            p.drawString(100,650-i,indetail.production)
            p.drawString(200,650-i,str(indetail.number))
            p.drawString(290,650-i,indetail.Univalent)
            p.drawString(400,650-i,indetail.total)
            p.drawString(40, 650-i-20, "------------------------------------------------------------------------------------------------------------")
                        
            for k in range(6):        
                p.drawString(40, 685-i-k*10, "|")
                p.drawString(470, 685-i-k*10, "|") 
                p.drawString(170, 685-i-k*10, "|") 
                p.drawString(260, 685-i-k*10, "|") 
                p.drawString(360, 685-i-k*10, "|") 
                
            i+=50
        for k in range(6):        
                p.drawString(40, 685-i-k*10, "|")
                p.drawString(470, 685-i-k*10, "|")
                p.drawString(260, 685-i-k*10, "|") 

        p.drawString(150, 650-i, invoice.drawer)
        p.drawString(325, 650-i, invoice.date)
        p.drawString(40, 650-i-20, "------------------------------------------------------------------------------------------------------------")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
    
#     pdf = pisa.CreatePDF(open('test.html','rb'),open('test.pdf','wb'))
#    data = open("1.html").read()
#    result = file('test.pdf','wb')
#    pdf = pisa.CreatePDF(data,result)
#    result.close()
#    pisa.startViewer('test.pdf')
def formdetaildeletefunction(request):
    dltid = request.GET["id"]
    if len(FormDetail.objects.filter(id=dltid)) > 0:
        FormDetail.objects.filter(id=dltid).delete()
        return HttpResponseRedirect("/form/")  

def addinvoicefunction(request):
    if request.POST:
        post = request.POST
        new_invoice = Invoice(
            title = post["title"],
            drawer = post["drawer"],
            date = post["date"])     
        new_invoice.save()
        #return HttpResponseRedirect("/invoice/") 
    return render_to_response("add_invoice.html")
    
def addformfunction(request):
    if request.POST:
        post = request.POST
        new_form = Form(
            year = post["year"])
        new_form.save()
        #return HttpResponseRedirect("/invoice/") 
    return render_to_response("add_form.html")

def addindetailfunction(request):    
    if request.POST:
        post = request.POST
        p = Invoice.objects.get(id=request.GET["id"])
        new_indetail = InDetail(
            productionID = p,
            production = post["production"],
            number = post["number"],
            Univalent = post["Univalent"],
            total = post["total"])       
        new_indetail.save()
        return HttpResponseRedirect("/invoice/")
    return render_to_response("add_indetail.html")
        
def addformdetailfunction(request):    
    if request.POST:
        post = request.POST
        p = Form.objects.get(id=request.GET["id"])
        new_formdetail = FormDetail(
            yearincomeID = p,
            yearincome = post["yearincome"],
            yearcost = post["yearcost"],
            sellingexpenses = post["sellingexpenses"],
            managementexpenses = post["managementexpenses"],
            financialexpenses = post["financialexpenses"],
            incomefrominvestment = post["incomefrominvestment"])
        new_formdetail.save()
        return render_to_response("formsearch.html")
    return render_to_response("add_formdetail.html")

    
def salaryfunction(request):  
    return render_to_response("salary.html")
    
def taxfunction(request):
    if request.POST:
        post = request.POST
        if post["costing"] == "" or post["selling"] =="":
            return HttpResponseRedirect("/tax/")
        a = float(post["costing"])
        b = float(post["selling"]) 
        if (b-a) >= 0:
            c = float((b-a) * 0.17)
            d = float((b-a) * 0.25)
        else:
            c = 0.0
            d = 0.0
        x = Context({"cost_list": [a],"sel_list": [b],"addv_list": [c],"nation_list": [d]})        
        return render_to_response("taxresult.html", x)
#        new_tax = Tax(
#            costing = post["costing"],
#            selling = post["selling"],
#            addvalue = c,
#            nation = d)
#        new_tax.save()
#        return HttpResponseRedirect("/taxresult/")
    return render_to_response("tax.html")    
    
def taxresultfunction(request):
    tax_list = Tax.objects.all()
    c = Context({"tax_list":tax_list})
    return render_to_response("taxresult.html",c)
       
def registerfunction(request):  
   if request.user.is_authenticated():
		c = Context({"title":"Error", "message":"You have registed,please log out first.", "url":"/logout/", "urltext":"logout" })
		return render_to_response("message.html", c)
   else:
       if request.POST:
          name = request.POST["username"]
          mail = request.POST["email"]
          pass1 = request.POST["password1"]
          pass2 = request.POST["password2"]
          empty = False
          namevalid = True
          passvalid = True
          success = False
          if name=="" or mail=="" or pass1=="" or pass2=="":
              empty = True
          u = User.objects.filter(username=name)
          if len(u)>0:
              namevalid = False
          if pass1 != pass2:
              passvalid = False
          if (not empty) and namevalid and passvalid:
              user = User.objects.create_user(username = name, email = mail, password = pass1)
              user.is_staff = True #administer right!!!!
              user.save()
              success = True
          return render_to_response("registration/register.html",{'invalidname': not namevalid, 'invalidpass': not passvalid, 'success': success, 'empty': empty, })
       else:
          return render_to_response("registration/register.html")
    

def salary_searchfunction(request):
    year = ""
    name = ""
    month = ""
    if request.POST:
        year = request.POST["year"]
        name = request.POST["name"]
        beginmonth = request.POST["beginmonth"]
        endmonth = request.POST["endmonth"]
        if year == "input year" and (beginmonth == "input begining month" or endmonth == "input ending month"):
            p = Salary.objects.filter(name=name)
            if len(p) <= 0:
                return HttpResponseRedirect("/salary/")
            c = Context({"salary_list": p})
            return render_to_response("salary_detail.html", c)
        if name == "input name" and (beginmonth == "input begining month" or endmonth == "input ending month"):
            p = Salary.objects.filter(year=year)
            if len(p) <= 0:
                return HttpResponseRedirect("/salary/")
            c = Context({"salary_list": p})
            return render_to_response("salary_detail.html", c)
        if (year != "input year" and name != "input name" and (beginmonth == "input begining month" or endmonth == "input ending month")): 
            p = Salary.objects.filter(year=year,name=name)
            if len(p) <= 0:
                return HttpResponseRedirect("/salary/")
            c = Context({"salary_list": p})
            return render_to_response("salary_detail.html", c)
        if (year != "input year" and name != "input name" and beginmonth != "input begining month" and endmonth != "input ending month"):           
            q = Salary.objects.filter(year=year,name=name)
            if len(q) <= 0:
                return HttpResponseRedirect("/salary/")
            p = Salary.objects.get(year=year,name=name)
            if len(Month.objects.filter(nameID=p,month=beginmonth)) > 0:
                begin = Month.objects.get(nameID=p,month=beginmonth)
                end = Month.objects.get(nameID=p,month=endmonth)
                sum = 0
                for i in range(begin.id,end.id+1):
                    k = Month.objects.filter(id=i)
                    sum += int(k[0].salary)
                c = Context({"total_list": [sum],"salary_list": q,"begin_list": [beginmonth],"end_list":[endmonth]})        
                return render_to_response("salary_detail.html", c)
    return HttpResponseRedirect("/salary/")