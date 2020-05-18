from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList, status_values, label_values

# Create your views here.
# def home_view(request,*args,**kwargs):
#     # return HttpResponse("<h1>HELLO WORLd</h1>")
#     return render(request,"index.html",{})

# def contact_view(request,*args,**kwargs):

#     return HttpResponse("<h1>Contact us</h1>")

def index(request): 
    todos  = TodoList.objects.all() 
    labelv = label_values.objects.all()
    statusv = status_values.objects.all()
    # all the data loaded in todos

    if request.method == "POST":

        if "taskAdd" in request.POST: 
            
            title    = request.POST["description"] #title
            due_date = str(request.POST["date"]) #date
            label    = request.POST["label_select"] #category
            status   = request.POST["status_select"]

            Todo = TodoList(title=title, due_date=due_date)
            Todo.save() #saving the todo

            labelO = label_values(label=label)
            labelO.save() #saving the todo

            statusO = status_values(status=status)
            statusO.save() #saving the todo
            
            return redirect("/") #reloading the page

        if "taskDelete" in request.POST:

            checkedlist = request.POST["checkedbox"] 
            for todo_title in checkedlist:
                todo = TodoList.objects.get(title=int(todo_title)) 
                todo.delete() #deleting todo

    return render(request, "index.html", {"todos": todos, "labelv":labelv, "statusv":statusv})