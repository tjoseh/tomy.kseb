from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from payroll.models import *
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def home(request):
    return render_to_response('index.html',  
                                context_instance=RequestContext(request)
    )
def dashboard(request):
    
    employees = Employe.objects.all();
    return render_to_response('dashboard.html',{'employees':employees},
                                context_instance=RequestContext(request)
    )   
def charts(request):
    return render_to_response('charts.html',  
                                context_instance=RequestContext(request)
    )
def forms(request):
    return render_to_response('forms.html',  
                                context_instance=RequestContext(request)
    )
def tables(request):
    return render_to_response('tables.html',  
                                context_instance=RequestContext(request)
    )
def bootstrap_elements(request):
    return render_to_response('bootstrap-elements.html',  
                                context_instance=RequestContext(request)
    )
def bootstrap_grid(request):
    return render_to_response('bootstrap-grid.html',  
                                context_instance=RequestContext(request)
    )
def blank_page(request):
    return render_to_response('blank-page.html',  
                                context_instance=RequestContext(request)
    )
    
def ajax_emp_filter(request):
    print "here"
    dob="06-1981" #Due to Django bug neeed to convert date to "YYYY-MM-DD format
    #dob='21-05-1981'
    dob= request.POST.get('dob', None)
    emp_obj = Employe.objects
    if dob: #dob is not None
        dob = datetime.strptime(dob, '%d-%m-%Y').strftime('%Y-%m-%d')
        emp_obj=emp_obj.filter(dob=dob)
    
    employees=emp_obj.all()
    tab_list=[]
    for emp in employees:
        tab_list.append("<tr><td>")
        tab_list.append(str(emp.employe_id))
        tab_list.append("</td><td>")
        tab_list.append(emp.first_name)
        tab_list.append(emp.last_name)
        tab_list.append("</td><td>")
        tab_list.append(emp.pan)
        tab_list.append("</td><td>")
        tab_list.append(emp.dob.strftime('%d-%m-%Y'))
        tab_list.append("</td></tr>")
    print " ".join(tab_list)
    return HttpResponse(" ".join(tab_list))
    
#def load_employees():
#    employees = Employe.objects.all();
#    return render_to_response('gl/metro_product_details.html',  {'store':store,'product':product,'images':images},
#                                context_instance=RequestContext(request)
#    ) 
