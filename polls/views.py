from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, Department


# Create your views here.
class IndexView(generic.ListView):
    
    template_name = 'polls/index.html'
    context_object_name = 'latest_department_list'
    

    def get_queryset(self):
        """
        
        """
        return Department.objects.all()

class QuestionsView(generic.ListView):
    model = Question
    template_name = 'polls/questions.html'
    
    def get_queryset(self, **kwargs):
        
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            department_id = self.kwargs['department_id']
        ).order_by('-pub_date')[:5]

    

class CreateQuestionView(generic.ListView):
    model = Department
    template_name = 'polls/newquestion.html'

    def get_context_data(self, **kwargs):
        number_of_questions = Question.objects.filter(department_id = self.kwargs['department_id']).count()

        department = get_object_or_404(Department,pk=self.kwargs['department_id'])

        my_context = {
            "department_id": self.kwargs['department_id'],
            "department_text": department.department_text,
            "max_number_questions": department.max_number_questions,
            "number_of_questions": number_of_questions
        }
        return my_context

class DetailView(generic.ListView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self, *args, **kwargs):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(id=self.kwargs['question_id'])


class ResultsView(generic.ListView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self, *args, **kwargs):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(id=self.kwargs['question_id'])


def vote(request, department_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        choice_id = request.POST.get("choice","")
        username = request.POST.get("username","")
        
        
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(department_id,question.id,)))
    #return HttpResponse("Estas votando en la pregunta %s." % question_id)

def createquestion(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    try:
        question_name = request.POST.get("question_name","")
        now = timezone.now()

        selected_department = department.question_set.create(department_id=department_id,question_text=question_name,pub_date=now)

        question = get_object_or_404(Question, pk=selected_department.id)

        choice1 = request.POST.get("choice1","")
        if choice1 != "":
            newchoice1 = question.choice_set.create(question_id=selected_department.id,choice_text=choice1)

        choice2 = request.POST.get("choice2","")
        if choice2 != "":
            newchoice2 = question.choice_set.create(question_id=selected_department.id,choice_text=choice2)

        choice3 = request.POST.get("choice3","")
        if choice3 != "":
            newchoice3 = question.choice_set.create(question_id=selected_department.id,choice_text=choice3)

        choice4 = request.POST.get("choice4","")
        if choice4 != "":
            newchoice4 = question.choice_set.create(question_id=selected_department.id,choice_text=choice4)

        choice5 = request.POST.get("choice5","")
        if choice5 != "":
            newchoice5 = question.choice_set.create(question_id=selected_department.id,choice_text=choice5)
    
    except (KeyError, Department.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/questions.html', {
            'department': department,
            'error_message': "You didn't select a department.",
        })

    else:
        selected_department.save()

        if choice1 != "":
            newchoice1.save()

        if choice2 != "":
            newchoice2.save()

        if choice3 != "":
            newchoice3.save()

        if choice4 != "":
            newchoice4.save()

        if choice5 != "":
            newchoice5.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:questions', args=(department_id,)))
    
def deletequestion (request,department_id,question_id):
    question = get_object_or_404(Question, pk=question_id)

    question.delete()

    return HttpResponseRedirect(reverse('polls:questions', args=(department_id,)))



