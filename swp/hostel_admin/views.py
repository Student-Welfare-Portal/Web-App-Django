from django.shortcuts import render, redirect
from dashboard.models import HostelAnnouncements
from .forms import HostelAnnouncementForm, AddAnnouncementForm
from django.http import HttpResponse
import datetime
import time
from django.template.loader import render_to_string
from orders.models import ManualOrder
from .forms import AddItemForm

def hostel_admin_index(request):
    return render(request, 'hostel_admin/index.html')

def hostel_admin_dashboard(request):
    hostel_announcements = list(HostelAnnouncements.objects.all())
    hostel_announcements.sort(key = lambda a: a.timestamp, reverse = True)

    return render(request, 'hostel_admin/hostel_admin_dashboard.html', {
    'hostel_announcements': hostel_announcements,
    })

# announcement_title=forms.CharField(label='announcement_title',widget=forms.TextInput(attrs={"class":"form-control"}))
# announcement=forms.CharField(label='announcement',widget=forms.TextInput(attrs={"class":"form-control"}))
# timestamp=forms.DateField(label='timestamp',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_at=timestamp=forms.DateField(label='created_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# created_by=forms.CharField(label='created_by',widget=forms.TextInput(attrs={"class":"form-control"}))
# modified_at=timestamp=forms.DateField(label='modified_at',input_formats=['%Y-%m-%d'],widget=forms.DateInput(format = '%Y-%m-%d',attrs={"class":"form-control","id":"to_date","name":"date1","placeholder":"YYYY-MM-DD","type":"text"}))
# modified_by=forms.CharField(label='modified_by',widget=forms.TextInput(attrs={"class":"form-control"}))
def announcement_delete(request, id):
    print(id)
    announcement = HostelAnnouncements.objects.get(pk=id)
    announcement.delete()
    hostel_announcements = HostelAnnouncements.objects.all()
    return render(request, 'hostel_admin/hostel_admin_dashboard.html', {
    'hostel_announcements': hostel_announcements,
    })

def announcement_edit(request, id):
    hostel_announcement = HostelAnnouncements.objects.get(pk=id)
    hostel_announcement_form = AddAnnouncementForm(initial = {
    'announcement_title': hostel_announcement.announcement_title,
    'announcement': hostel_announcement.announcement,
    })
    print(hostel_announcement_form)
    return render(request, 'hostel_admin/edit_announcements.html', {
    'form': hostel_announcement_form,
    'id': id,
    })

def add_announcement(request):
    if request.method == 'GET':
        add_announcement_form = AddAnnouncementForm()
        return HttpResponse(render_to_string('hostel_admin/add.html',context={
        'add_announcement_form': add_announcement_form,
        }))

def add_announcement_url(request):
    if request.method == 'POST':
        form = AddAnnouncementForm(request.POST)
        if form.is_valid():
            add_announcement_form=form.save(commit=False)
            add_announcement_form.timestamp=datetime.datetime.now()
            add_announcement_form.created_at=datetime.datetime.now().date()
            add_announcement_form.modified_at = datetime.datetime.now().date()
            add_announcement_form.created_by=request.user.username
            add_announcement_form.modified_by=request.user.username
            add_announcement_form.save()

            return redirect('hostel_admin:hostel_admin_dashboard')

def save_edit_changes(request, id):
    if request.method == 'POST':
        try:
            announcement = HostelAnnouncements.objects.get(pk=id)
        except HostelAnnouncements.DoesNotExist:
            announcement = None
        if announcement is not None:
            announcement_title = request.POST.get('announcement_title')
            announcement_body = request.POST.get('announcement')
            flag = 0
            if announcement_title != announcement.announcement_title:
                announcement.announcement_title = announcement_title
                flag = 1
                announcement.announcement = announcement_body
                announcement.timestamp=datetime.datetime.now()
                announcement.modified_at = datetime.datetime.now().date()
                announcement.modified_by=request.user.username
            if announcement_body != announcement.announcement:
                announcement.announcement = announcement_body
                if flag == 0:
                    announcement.timestamp=datetime.datetime.now()
                    announcement.modified_at = datetime.datetime.now().date()
                    announcement.modified_by=request.user.username
            announcement.save()
        return redirect('hostel_admin:hostel_admin_dashboard')

def manual_orders(request):
    if request.method == 'GET':
        manual_orders = ManualOrder.objects.all()
        length = len(manual_orders)
        return HttpResponse(render_to_string('hostel_admin/manual_order.html',context={
        'manual_orders': manual_orders,
        'len': length,
        }))

def add_item(request):
    if request.method == 'POST':
        add_item_form = AddItemForm(data = request.POST)
        if add_item_form.is_valid():
            form = add_item_form.save(commit = False)
            form.item_type = 'Others'
            form.timestamp=datetime.datetime.now()
            form.created_at = datetime.datetime.now().date()
            # print(form.created_at)
            # print('hi')
            form.modified_at = datetime.datetime.now().date()
            form.modified_by = request.user.username
            form.created_by = request.user.username
            print('hi')
            form.save()
            print('done')
        return redirect('hostel_admin:hostel_admin_dashboard')
    else:
        item_form = AddItemForm()
        return HttpResponse(render_to_string('hostel_admin/item_form.html',context={
        'form': item_form,
        }))
