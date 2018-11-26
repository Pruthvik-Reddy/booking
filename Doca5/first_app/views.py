from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import category,location,doctor,Appointments
from .forms import FormName,AppForm,Form2
from doc_app.models import slots


# Create your views here.
def index(request):


    return render(request, "first_app/homepage.html")

def book(request):
    form=FormName(request.POST)
    #if form.is_valid():
    #    loc=form.cleaned_data['loc']
    #    cat=form.cleaned_data['cat']
    #   details=doctor.objects.filter(location=loc)


        #print(loc)
        #print(cat)
    #print(form)
    context = {
        "categories": category.objects.all(),
        "locations": location.objects.all(),

    }



    return render(request, "first_app/book_appointments.html", context=context)

def showapp(request):

    loc=request.POST.get('loc')
    cat=request.POST.get('cat')
    sort=request.POST.get('sort')
    #date=request.POST.get('date')
    details = doctor.objects.filter(location__loc_name=loc,category__cat_name=cat ).values().order_by(sort)
    #form=slotform
    #details = doctor.objects.filter((location__loc_name=loc),(category_cat_name=cat)).select_related('doctor').values()
    context={
        "doctors":details,
       # "form":form
    }


    return render(request,"first_app/show_appointments.html",context=context)

def bookapp(request):
    #form=AppForm()
    #if request.method=="POST":
    #    form=AppForm(request.POST)
    #    if form.is_valid():
    #        form.save(commit=True)
    #    else:
    #        print("FORM INVALID")


    #doc_name=request.POST.get('doc_name')
    #fees=request.POST.get('fees')
    #rating=request.POST.get('rating')
    #form.doc_name=doc_name
    #form.fees=fees
    #form.rating=rating
    #form.save()
    """
    if request.method=='POST':
        form=AppForm(request.POST)
        if form.is_valid():
            doc_name=form.cleaned_data['doc_name']
            fees=form.cleaned_data['fees']
            rating=form.cleaned_data['rating']
            doctor.objects.create(
                doc_name=doc_name,
                fees=fees,
                rating=rating,
            ).save()
            print("booked")
    else:
        form=AppForm
    context={
        'form':form
    }
    """
    #return render(request,"my_app/add.html",context=context)
    if request.method=="POST":
        print("boooked2")
        form=Form2(request.POST)
        print("booked4")
        #doc_name=form.cleaned_data['doc_name']
        #fees=request.POST.get('fees')
        #doc_name = form.cleaned_data['doc_name']
        #print(fees)
        #print(form)
        if form.is_valid():
            print("booked3")
            doc_name=request.POST.get('doc_name')
            print(doc_name)
            #fees=request.POST.get('fees')
            #rating=request.POST.get('rating')
            date=request.POST.get('date')
            start_time=request.POST.get('start_time')
            dobj = doctor.objects.get(doc_name=doc_name)
            fees=dobj.fees
            rating=dobj.rating
            print(date)
            print(start_time)
            print(fees)
            print(rating)

            Appointments.objects.create(
                doc_name=doc_name,
                fees=fees,
                rating=rating,
                date=date,
                start_time=start_time,

            ).save()
            print("BOOKED5")
            context={
                'doc_name':doc_name,
                'fees':fees,
                'date':date,
            }

            return render(request, "first_app/booked.html", context=context)
    else:
        print("booked1")
        form=Form2
    #print("booked")


def slotapp(request):
    if request.method=="POST":
        print("boooked2")
        form=AppForm(request.POST)
        print("booked4")
        #doc_name=form.cleaned_data['doc_name']
        #fees=request.POST.get('fees')
        #doc_name = form.cleaned_data['doc_name']
        #print(fees)
        #print(form)
        doc_name = request.POST.get('doc_name')
        fees = request.POST.get('fees')
        rating = request.POST.get('rating')
        date = request.POST.get('date')
        print(date)
        dobj=doctor.objects.get(doc_name=doc_name)
        details1 = slots.objects.filter(doc_name=dobj,date=date ).values()
        context={
           "details1": details1,
        }
        return render(request,"first_app/slot_book.html",context=context)


def showappmnts(request):
    appointments = Appointments.objects.all()
    context = {
        'appointments':appointments
    }
    return render(request, "first_app/yourappointments.html", context=context)

def delete(request,pk):
    reminder = get_object_or_404(Appointments, pk=pk)
    reminder.delete()
    if(request.method=='DELETE'):
        reminder=get_object_or_404(Appointments, pk=pk)
        reminder.delete()
    return HttpResponseRedirect('/first_app/yourappointments/')
