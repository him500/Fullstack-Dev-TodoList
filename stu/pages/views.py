from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList 
from _datetime import date

label_json=[

    {'label':'Personal'},
    {'label':'Work'},
    {'label':'Shopping'},
    {'label':'Others'}

]
status_json=[
    {'status':'In progress'},
    {'status':'New'},
    {'status':'Completed'}
]
todos  = TodoList.objects.all()
def home(request): 
    todos  = TodoList.objects.all()
    current_date=date.today()

    for i in range(len(todos)):
        ddate=todos[i].due_date
        if current_date.year >= ddate.year and current_date.month >= ddate.month and current_date.day > ddate.day:
            
            todos[i].archive = True
            todos[i].save()

    if request.method == "POST":

        if "taskAdd" in request.POST: 
            
            title    = request.POST["description"] #title
            due_date = request.POST["date"] #date
            label    = request.POST["label_select"] #category
            status   = request.POST["status_select"]

            # print("Start",list(map(int, due_date.split("-"))),"end")
            Todo = TodoList(title=title, due_date=due_date, label=label, status=status)
            Todo.save() #saving the todo

            return redirect("/") #reloading the page

        if "taskDelete" in request.POST:

            checkedlist = request.POST["checkedbox"] 
            print(checkedlist,len(checkedlist))
            todo = TodoList.objects.filter(title=checkedlist) 
            todo.delete() #deleting todo

            return redirect("/") #reloading the page

    # for todo in TodoList.objects.all():
    #     print(todo.archive)

    return render(request, "pages/index.html", {"todos": todos, 'labelv':label_json, 'statusv':status_json})

def index(request):
    current_date=date.today()

    for i in range(len(todos)):
        ddate=todos[i].due_date
        if current_date.year >= ddate.year and current_date.month >= ddate.month and current_date.day > ddate.day:
            
            todos[i].archive = True
            todos[i].save()
    
    if request.method == "POST":
        

        if "taskAdd" in request.POST: 
            
            title    = request.POST["description"] #title
            due_date = request.POST["date"] #date
            label    = request.POST["label_select"] #category
            status   = request.POST["status_select"]

            # print("Start",list(map(int, due_date.split("-"))),"end")
            Todo = TodoList(title=title, due_date=due_date, label=label, status=status)
            Todo.save() #saving the todo
            # print("task saved")

            return redirect("/") #reloading the page 

    return render(request, "pages/indexN.html", {"todos": todos, 'labelv':label_json, 'statusv':status_json})

def display(request):
    todos=TodoList.objects.all()
    current_date=date.today()

    for i in range(len(todos)):
        ddate=todos[i].due_date
        if current_date.year >= ddate.year and current_date.month >= ddate.month and current_date.day > ddate.day:
            
            todos[i].archive = True
            todos[i].save()
    
    if request.method == "POST":
        if "taskDelete" in request.POST:
            # print("here")

            checkedlist = request.POST["checkedbox"] 
            print(checkedlist,len(checkedlist))
            todo = TodoList.objects.filter(title=checkedlist) 
            todo.delete() #deleting todo

            return redirect("../display/") #reloading the page

    return render(request, "pages/display.html", {"todos": todos})
def archive(request):
    todos=TodoList.objects.all()
    current_date=date.today()

    for i in range(len(todos)):
        ddate=todos[i].due_date
        if current_date.year >= ddate.year and current_date.month >= ddate.month and current_date.day > ddate.day:
            
            todos[i].archive = True
            todos[i].save()
    
    if request.method == "POST":
        if "taskDelete" in request.POST:
            # print("here")

            checkedlist = request.POST["checkedbox"] 
            print(checkedlist,len(checkedlist))
            todo = TodoList.objects.filter(title=checkedlist) 
            todo.delete() #deleting todo

            return redirect("../archive/") #reloading the page

    return render(request, "pages/archive.html", {"todos": todos})
