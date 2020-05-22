from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList

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

def home(request): 
    todos  = TodoList.objects.all() 
    # labelv = label_values.objects.all()
    # statusv = status_values.objects.all()

    # all the data loaded in todos

    if request.method == "POST":

        if "taskAdd" in request.POST: 
            
            title    = request.POST["description"] #title
            due_date = str(request.POST["date"]) #date
            label    = request.POST["label_select"] #category
            status   = request.POST["status_select"]

            Todo = TodoList(title=title, due_date=due_date, label=label, status=status)
            Todo.save() #saving the todo

            return redirect("/") #reloading the page

        if "taskDelete" in request.POST:

            checkedlist = request.POST["checkedbox"] 
            print(checkedlist)
                # print(todo_title)
                # todo = TodoList.objects.get(title=todo_title) 
                # todo.delete() #deleting todo
            todo = TodoList.objects.get(title=checkedlist) 
            todo.delete() #deleting todo

    # return render(request, "index.html", {"todos": todos, "labelv":labelv, "statusv":statusv})
    return render(request, "pages/index.html", {"todos": todos, 'labelv':label_json, 'statusv':status_json})



    # # ------------

    #     if "taskAdd" in request.POST: #checking if there is a request to add a todo
    #         title = request.POST["description"] #title
    #         date = str(request.POST["date"]) #date
    #         category = request.POST["category_select"] #category
    #         content = title + " -- " + date + " " + category #content
    #         Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
    #         Todo.save() #saving the todo 
    #         return redirect("/") #reloading the page
    #     if "taskDelete" in request.POST: #checking if there is a request to delete a todo
    #         checkedlist = request.POST["checkedbox"] #checked todos to be deleted
    #         for todo_id in checkedlist:
    #             todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
    #             todo.delete() #deleting todo
