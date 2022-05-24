
from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request):
    return render(request, 'planner/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'planner/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'planner/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('planner:topics')
    context = {'form':form}
    return render(request, 'planner/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('planner:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'planner/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(request.POST, request.FILES or None, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('planner:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'planner/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    post_to_delete = Entry.objects.get(id=entry_id)
    topic = post_to_delete.topic
    post_to_delete.delete()
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'planner/topic.html', context)

@login_required
def delete_topic(request, topic_id):
    topic_to_delete = Topic.objects.get(id=topic_id)
    topic_to_delete.delete()
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'planner/topics.html', context)




