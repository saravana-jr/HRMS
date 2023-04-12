from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import LeaveRequest
# from .forms import LeaveRequestForm

# def design(request):
#     return render(request,"peopleconnect/design.html")



def design(request):
    if request.method == 'POST':
        leave_type = request.POST['leave_type']
        from_date = request.POST['start-date']
        to_date = request.POST['to-date']
        reason = request.POST['reason']
        LeaveRequest.objects.create(leave_type=leave_type, from_date=from_date, to_date=to_date, reason=reason)
        return render(request, 'peopleconnect/sent.html')
    else:
        return render(request, 'peopleconnect/design.html')
    
# def leave_submitted(request):
#     return render(request, 'peopleconnect/sent.html')
    
def leave_submitted(request):
    if request.method == 'POST':
        LeaveRequest.objects.all().delete()
        return render(request,'peopleconnect/design.html')
    else:
        return render(request, 'peopleconnect/sent.html')


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