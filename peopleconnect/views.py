from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .models import LeaveRequest

from .forms import LeaveRequestForm

def Leave(request):
    leave_requests = LeaveRequest.objects.all()
    context = {'leave_requests': leave_requests}
    return render(request, 'peopleconnect/Leave.html', context)
    
    
def new_form(request):
    if request.method == 'POST':
        form=LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request=form.save()
            leave_requests = LeaveRequest.objects.all()
            context = {'leave_requests': leave_requests}
            return render(request, 'peopleconnect/Leave.html',context)
        else:
            return render(request, 'peopleconnect/new.html', {"form": form})
    
    else:
        form = LeaveRequestForm()
        return render(request, 'peopleconnect/new.html', {"form": form})
    
    
def edit(request,leave_id):
    
    leave_request = LeaveRequest.objects.get(id=leave_id)
    if request.method == 'POST':
        form=LeaveRequestForm(request.POST,instance=leave_request)
        if form.is_valid():
            leave_request=form.save()
            return redirect('Leave')
    # if request.method == 'POST':
    #     leave_request.leave_type = request.POST.get('leave_type')
    #     leave_request.description = request.POST.get('Description')
    #     leave_request.No_of_Leaves = request.POST.get('No.of.Leaves')
    #     leave_request.save()
    #     return redirect('Leave')
    else:
        form = LeaveRequestForm(instance=leave_request)
        context = {'form': form, 'leave_request': leave_request}
        return render(request, 'peopleconnect/edit.html',context)
    

def view(request,leave_id):
    leave_requests=get_object_or_404(LeaveRequest,id=leave_id)
    context={'leave_requests': leave_requests}
    return render(request, 'peopleconnect/view.html',context)
    
def delete(request,leave_id):
    leave_request=get_object_or_404(LeaveRequest,id=leave_id)
    if request.method == 'POST':
        leave_request.delete()
        return redirect('Leave')

    else:
        return render(request, 'peopleconnect/delete.html')
        

    
    
    
# def leave_submitted(request):
#     if request.method == 'POST':
#         LeaveRequest.objects.all().delete()
#         return render(request,'peopleconnect/design.html')
#     else:
#         return render(request, 'peopleconnect/sent.html')


# def design(request):
#     if request.method == 'POST':
#         form = LeaveRequestForm(request.POST)
#         if form.is_valid():
#             print('Form is valid')
#             form.save()
#             return redirect('sent.html')  
#     else:
#         form = LeaveRequestForm()
#         print('Form is valid')
#     return render(request, 'peopleconnect/design.html', {'form': form})

# def design(request):
#     if request.method == 'POST':
#         form = LeaveRequestForm(request.POST)
#         if form.is_valid():
#             print('Form is valid')
#             leave = form.save(commit=False)
#             print('Form is being submitted')
#             leave.save()
#             return redirect('sent.html')  
#     else:
#         form = LeaveRequestForm()
#     return render(request, 'peopleconnect/design.html', {'form': form})