from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList

# Create your views here.
def home_view(request,*args,**kwargs):
    # return HttpResponse("<h1>HELLO WORLd</h1>")
    return render(request,"index.html",{})

def contact_view(request,*args,**kwargs):

    return HttpResponse("<h1>Contact us</h1>")

def index(request): 
    todos = TodoList.objects.all() 
    # all the data loaded in todos

    if request.method == "POST":

        if "taskAdd" in request.POST: 
            
            title    = request.POST["title"] #title
            due_date = str(request.POST["date"]) #date
            label    = request.POST["label"] #category
            status   = request.POST["status"]

            Todo = TodoList(title=title, due_date=due_date, label=label, status=status)
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page

        if "taskDelete" in request.POST:

            checkedlist = request.POST["checkedbox"] 
            for todo_title in checkedlist:
                todo = TodoList.objects.get(title=int(todo_title)) 
                todo.delete() #deleting todo

    return render(request, "index.html", {"todos": todos})