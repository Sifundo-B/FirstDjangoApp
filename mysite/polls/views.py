from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Case
from django.views.generic import ListView, DetailView

# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('pub_date')[:5]
    context = {'latest_questions':latest_questions}
    return render (request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("This is the detail view of the question: %s" % question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#home view for posts. Posts are displayed in a list
class IndexView(ListView):
 template_name='polls/home.html'
 context_object_name = 'case_list'
 def get_queryset(self):
  return Case.objects.all()
#Detail view (view post detail)
class PostDetailView(DetailView):
 model=Case
 template_name = 'polls/case-detail.html'
#New post view (Create new post)
def postview(request):
 if request.method == 'POST':
  form = Case(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = Case()
 return render(request,'polls/case.html',{'form': form})
#Edit a post
def edit(request, pk, template_name='polls/edit.html'):
    post= get_object_or_404(Case, pk=pk)
    form = Case(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})
#Delete post
def delete(request, pk, template_name='polls/confirm_delete.html'):
    post= get_object_or_404(Case, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('home')
    return render(request, template_name, {'object':post})