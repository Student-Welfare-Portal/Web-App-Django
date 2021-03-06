from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import *
from .forms import *
from dashboard.models import MessAnnouncements
from django.contrib.auth.decorators import login_required
from api_integration.models import Student
import datetime
import time
from api_integration.models import Student


@login_required
def get_admin_status(request):
	st = 0
	dr = Student.objects.filter(student_first_name = str(request.user))
	if(len(dr) == 0):
            return 0
	print(dr, "ASDAS")
	if(dr[0].is_hostel_admin == True):
		st = 1
	elif(dr[0].is_mess_admin == True):
		st = 2
	elif(dr[0].is_medical_admin == True):
		st = 3
	return st

# Create your views here.

def getDate(dat):
	dat = dat.split('-')
	year = int(dat[0])
	month = int(dat[1])
	day = int(dat[2])

	return datetime.date(year,month,day)

@login_required
def mess_dashboard(request):
	mess_announcements = list(MessAnnouncements.objects.all())
	mess_announcements.sort(key = lambda a: a.timestamp, reverse = True)

	mess_items = list(MessItems.objects.all())
	if mess_items:
		order_history = OrderHistoryMess.objects.all()
		user_order_history = list(filter(lambda x: x.student.user == request.user, order_history))
		user_order_history.sort(key = lambda a: a.timestamp, reverse = True)
		all_orders = list(OrderListMess.objects.all())
		user_orders = list(filter(lambda x: x.student.user == request.user, all_orders))
		user_orders.sort(key = lambda a: a.timestamp, reverse = True)
		total_cost = 0
		if user_orders:
			for orders in user_orders:
				total_cost += orders.quantity * orders.item.cost
		return render(request, 'mess/home.html', {
		'items': mess_items,
		'user_orders': user_orders,
		'user_order_history': user_order_history,
		'total_cost': total_cost,
		'mess_announcements': mess_announcements,
		'admin_status': get_admin_status(request)
		})
	else:
		return render(request, 'mess/home.html', {
		'items': mess_items,
		'mess_announcements': mess_announcements,
		'admin_status': get_admin_status(request)
		})
# @login_required
# def mess_dashboard(request):
# 	mess_announcements = list(MessAnnouncements.objects.all())
# 	mess_announcements.sort(key = lambda a: a.timestamp, reverse = True)
#
# 	mess_items = list(MessItems.objects.all())
# 	if mess_items:
# 		order_history = OrderHistoryMess.objects.all()
#
# 		user_order_history = list(filter(lambda x: x.student.user == request.user, order_history))
#
# 		user_order_history.sort(key = lambda a: a.timestamp, reverse = True)
#
# 		all_orders = list(OrderListMess.objects.all())
#
# 		user_orders = list(filter(lambda x: x.student.user == request.user, all_orders))
#
# 		user_orders.sort(key = lambda a: a.timestamp, reverse = True)
#
# 		total_cost = 0
#
# 		if user_orders:
#
# 			for orders in user_orders:
#
# 				total_cost += orders.quantity*orders.item.cost
#
# 		return render(request, 'mess/home.html', {
# 		'items': mess_items,
#         'user_orders': user_orders,
#         'user_order_history': user_order_history,
#         'total_cost': total_cost,
# 		'mess_announcements': mess_announcements,
# 		})
# 	else:
#
# 		return render(request, 'mess/home.html', {
#         'items': mess_items,
# 		'mess_announcements': mess_announcements,
#         })

def dot(K, L):
   if len(K) != len(L):
      return 0

   return sum(i[0] * i[1] for i in zip(K, L))



def changeQuantity(items_p, items_posted, not_order, ordered_items):
    j = 0
    for i in range(len(items_posted)):
        if int(items_posted[i]) > 0:
            obj = MessItems.objects.get(item_name=items_p[j].item_name)
            if obj.quantity - int(items_posted[i]) < 0:
                not_order.append(obj)
            else:
                obj.quantity = obj.quantity - int(items_posted[i])
                obj.save()
                ordered_items.append(obj)
            j+=1

def store_in_items_list(student, items_purchased, items_post, creator):
    j = 0
    for i in range(len(items_post)):
        if int(items_post[i]) != 0:
            obj = MessItems.objects.get(item_name=items_purchased[j].item_name)
            if obj.quantity - int(items_post[i]) > 0:
                obj1 = OrderListMess.objects.create(student=student, item=items_purchased[j], quantity=int(items_post[i]))
                obj1.created_at=obj.timestamp
                obj1.created_by=creator.username
                obj1.save()
            j += 1

def delete_order(request, pk):
    obj = OrderListMess.objects.get(pk=pk)
    obj2 = MessItems.objects.get(item_name=obj.item.item_name)
    obj2.quantity += obj.quantity
    obj2.save()
    print(obj.item.item_name)
    if obj:
        obj1 = OrderHistoryMess.objects.create(student=obj.student, item=obj.item, quantity=obj.quantity, timestamp=obj.timestamp)
        obj1.save()
        obj.delete()
    return redirect('mess:mess_dashboard')

@login_required
def place_order(request):
	if request.method == 'POST':
		items = list(MessItems.objects.all())
		items_post = request.POST.getlist('order')
		print(items_post)
		print(request.POST)
		if items_post:
			items_cost = dot([a.cost for a in items], list(map(int, items_post)))
		if items:
			items_purchased = [items[i] for i in range(len(items)) if items_post[i]!='0']
		not_order = []
		ordered_items = []
		if items_post:
			student = Student.objects.get(user = request.user)
			store_in_items_list(student, items_purchased, items_post, request.user)
			changeQuantity(items_purchased, items_post, not_order, ordered_items)
		if len(not_order) == 0 :
			return redirect('mess:mess_dashboard')
		else:
			total_cost = 0
			for orders in ordered_items:
				total_cost += orders.quantity*orders.cost
			print(total_cost)
			print('hi')
			print(not_order)
			print(ordered_items)
			return render(request, 'mess/not_order.html', {
			'ordered_items': ordered_items,
			'not_ordered': not_order,
			'total_cost': total_cost,
			'admin_status': get_admin_status(request)
			})

@login_required
def mess_leave(request):
	if request.method == 'POST':
		form = MessLeaveForm(request.POST)
		if form.is_valid():
			leave_form = form.save(commit=False)
			leave_form.student = Student.objects.get(user = request.user)
			leave_form.leave_from = getDate(request.POST['leave_from'])
			leave_form.leave_to = getDate(request.POST['leave_to'])
			leave_form.hometown = request.POST['hometown']
			leave_form.reason = request.POST['reason']
			leave_form.timestamp = datetime.datetime.now()
			leave_form.created_at = datetime.datetime.now().date()
			leave_form.modified_at = datetime.datetime.now().date()

			leave_form.created_by = Student.objects.get(user = request.user)
			leave_form.modified_by = Student.objects.get(user = request.user)

			if(leave_form.leave_from >=  leave_form.leave_to):
				error_message = "Please enter valid From and TO dates"
				return render(request,'mess/leave.html',{'form':form,'error_message':error_message, 'admin_status': get_admin_status(request)})
			leave_form.save()
			return render(request, 'mess/leave-ack.html', {'admin_status': get_admin_status(request)})
		else:
			error_message = "Please enter data in YYYY-MM-DD format"
			return render(request,'mess/leave.html',{'form':form,'error_message':error_message, 'admin_status': get_admin_status(request)})

	form =  MessLeaveForm()
	return render(request,'mess/leave.html',{'form':form,'error_message':'', 'admin_status': get_admin_status(request)})

@login_required
def leave_form(request):
	form = MessLeaveForm()
	return render(request,'mess/leave.html',{'form':form, 'admin_status': get_admin_status(request)})

@login_required
def mess_refund(request):
	if request.method == 'POST':
		form = MessRefundForm(request.POST)
		if form.is_valid():
			refund_form = form.save(commit=False)
			try:
				student = Student.objects.get(user = request.user)
			except Student.DoesNotExist:
				student = None
			if student is not None:
				mess_leaves = MessLeave.objects.all()
				user_mess_leaves = list(filter(lambda x: x.student.user == request.user, mess_leaves))
				user_mess_leaves.sort(key = lambda a: a.timestamp, reverse = True)
				print(user_mess_leaves)
				# try:
				# 	mess_leave = MessLeave.objects.get(student = student)
				# except MessLeave.DoesNotExist:
				# 	mess_leave = None
				days = 0
				ref_amount = 0
				delta1 = 0
				days = 0
				if user_mess_leaves:
					# refund_form.refund_from = getDate(request.POST['refund_from'])
					# refund_form.refund_to = getDate(request.POST['refund_to'])
					# print(user_leave_obj.ref_given)
					for leave in user_mess_leaves:
						if leave.ref_given is False:
							if leave.leave_from.month == datetime.datetime.now().date().month:
								delta1 = leave.leave_to - leave.leave_from
								if delta1.days - days >= 0 and delta1.days <= 5:
									days += delta1.days
									leave.ref_given = True
									leave.save()
									if days >=5 :
										# print('hi')
										# print(leave)
										# print('bye')
										days = 5
										break
								else:
									days = 5
									leave.ref_given = True
									# print('hello')
									# print(leave)
									# print('hello')
									leave.save()
									break
								# print(leave)
								# print('bug')
					if days > 0:
						refund_form.student = student
						refund_form.account_number = request.POST['account_number']
						refund_form.account_holder_name = request.POST['account_holder_name']
						refund_form.ifsc_code = request.POST['ifsc_code']
						refund_form.timestamp = datetime.datetime.now()
						refund_form.refund_amount = int(days) * 98
						refund_form.created_at = datetime.datetime.now().date()
						refund_form.modified_at = datetime.datetime.now().date()

						refund_form.created_by = Student.objects.get(user = request.user)
						refund_form.modified_by = Student.objects.get(user = request.user)
						refund_form.save()
						print(days)
						ref_amount = int(days) * 98
						return render(request, 'mess/refund-ack.html', {
						'refund_amount': ref_amount,
						'admin_status': get_admin_status(request)
						})
					elif days == 0:
						mess_obj = MessRefund.objects.get(student = student)
						ref_amount = mess_obj.refund_amount
						return render(request, 'mess/refund-ack.html', {
						'refund_amount': ref_amount,
						'already_refunded': 'We have already refunded',
						'admin_status': get_admin_status(request)
						})
				else:
					return render(request, 'mess/refund.html', {
					'message': 'You have not applied for mess leave',
					'form': form,
					'admin_status': get_admin_status(request)
					})
		else:
			error_message = "Please enter Valid data"
			return render(request,'mess/refund.html',{'form':form,'error_message':error_message,'admin_status': get_admin_status(request)})
	form =  MessRefundForm()
	return render(request,'mess/refund.html',{'form':form,'error_message':'','admin_status': get_admin_status(request)})

@login_required
def refund_form(request):
	form = MessRefundForm()
	return render(request,'mess/refund.html', {'form': form,'admin_status': get_admin_status(request)})


@login_required
def feedback_form(request):
	form = MessFeedbackForm()
	return render(request, 'mess/feedback.html',{'form':form,'admin_status': get_admin_status(request)})


@login_required
def submit_feedback(request):
	if request.method == 'POST':
		form = MessFeedbackForm(request.POST)
		feedback_form = form.save(commit=False)
		refund_form.student = Student.objects.get(user = request.user)
		feedback_form.feedback = request.POST['feedback']
		feedback_form.timestamp = datetime.datetime.now()
		feedback_form.created_at = datetime.datetime.now().date()
		feedback_form.modified_at = datetime.datetime.now().date()
		if form.is_valid():
			feedback_form = form.save(commit=False)
			refund_form.student = Student.objects.get(user = request.user)
			feedback_form.feedback = request.POST['feedback']
			feedback_form.timestamp = datetime.datetime.now()
			feedback_form.created_at = datetime.datetime.now().date()
			feedback_form.modified_at = datetime.datetime.now().date()
			feedback_form.created_by = Student.objects.get(user = request.user)
			feedback_form.modified_by = Student.objects.get(user = request.user)
			feedback_form.save()
			return render(request, 'mess/feedback-ack.html',{'admin_status': get_admin_status(request)})
		else:
			form =  MessRefundForm()
			return render(request,'mess/feedback.html',{'admin_status': get_admin_status(request)})

	form =  MessRefundForm()
	return render(request,'mess/feedback.html',{'admin_status': get_admin_status(request)})

@login_required
def applyMessRefund(request):
	if request.method == 'POST':
		form = MessLeaveForm(request.POST)
		refund_form = form.save(commit=False)
		refund_form.student = Student.objects.get(user = request.user)
		refund_form.ref_amount = request.POST['ref_amount']
		refund_form.timestamp = datetime.datetime.now()
		refund_form.created_at = datetime.datetime.now().date()
		refund_form.modified_at = datetime.datetime.now().date()

		refund_form.created_by = Student.objects.get(user = request.user)
		refund_form.modified_by = Student.objects.get(user = request.user)
		refund_form.save()
		return render(request, 'mess/refund-ack.html',{'admin_status': get_admin_status(request)})

	form =  MessRefundForm()
	return render(request,'mess/refund.html',{'form':form,'error_message':'','admin_status': get_admin_status(request)})
