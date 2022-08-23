import requests
import json
from Application.models import *
from Application.forms import *
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict


# Create your views here.
def session_login():
    session = requests.Session()
    session.headers = {'Content-Type': 'application/json',
                       'Authorization': 'Basic ZXJzaW5kcml2ZXByb2plY3QxQGdtYWlsLmNvbTpXUW8xNjUzMTk='}
    return session


def home_page(request):
    return render(request, 'home-page.html')


def tickets_upgrade(request):
    session = session_login()
    tickets_response = session.get('https://nevisoft.zendesk.com/api/v2/tickets')
    tickets_response_json = json.loads(tickets_response.text)
    tickets = tickets_response_json['tickets']
    for ticket in tickets:
        if not Tickets.objects.filter(id=ticket['id']).exists():
            obj = Tickets(**ticket)
            obj.save()
    return JsonResponse({"status": 'success'})


def comments_upgrade(request):
    session = session_login()
    tickets = Tickets.objects.all()
    for ticket in tickets:
        comments_response = session.get(f"https://nevisoft.zendesk.com/api/v2/tickets/{ticket.id}/comments")
        comments_response_json = json.loads(comments_response.text)
        comments = comments_response_json['comments']
        for comment in comments:
            if not Comments.objects.filter(id=comment['id']).exists():
                obj = Comments(**comment)
                obj.ticket = ticket
                obj.save()
    return JsonResponse({"status": 'success'})


def tickets_list(request):
    tickets = Tickets.objects.all()
    return render(request, 'tickets-list.html', {'tickets': tickets})


def ticket_detail(request, ticket_id=None, *args, **kwargs):
    next_url = request.POST.get('next') or None
    if ticket_id:
        instance = get_object_or_404(Tickets, id=ticket_id)
        form = TicketsForm(request.POST or None, instance=instance)
    else:
        form = TicketsForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url:
            return redirect(next_url)
        form = TicketsForm()
    return render(request, 'form.html',
                  context={'form': form})


def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Tickets, id=ticket_id)
    ticket.delete()
    return JsonResponse({'status': 'success'})


def comments_list(request):
    comments = Comments.objects.all()
    return render(request, 'comments-list.html', {'comments': comments})


def comment_detail(request, comment_id=None, *args, **kwargs):
    next_url = request.POST.get('next') or None
    if comment_id:
        instance = get_object_or_404(Comments, id=comment_id)
        form = CommentsForm(request.POST or None, instance=instance)
    else:
        form = CommentsForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url:
            return redirect(next_url)
        form = CommentsForm()
    return render(request, 'form.html',
                  context={'form': form})


def comment_delete(request, ticket_id):
    comment = get_object_or_404(Comments, id=ticket_id)
    comment.delete()
    return JsonResponse({'status': 'success'})


