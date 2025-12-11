from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import F, Sum, Count
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models.functions import Coalesce

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last ten published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by("-pub_date")[:10]

    def get_context_data(self, **kwargs):
        """
        Add additional context for the template.
        """
        context = super().get_context_data(**kwargs)

        # Get total polls count (including unpublished)
        total_polls = Question.objects.count()

        # Calculate total votes across all questions
        total_votes = Choice.objects.aggregate(
            total=Coalesce(Sum('votes'), 0)
        )['total']

        # Add question stats to each question
        for question in context['latest_question_list']:
            question.total_votes = question.choice_set.aggregate(
                total=Coalesce(Sum('votes'), 0)
            )['total']

        context.update({
            'total_polls': total_polls,
            'total_votes': total_votes,
        })

        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        """
        Add total_votes to question context.
        """
        context = super().get_context_data(**kwargs)
        question = context['question']

        # Calculate total votes for this question
        total_votes = question.choice_set.aggregate(
            total=Coalesce(Sum('votes'), 0)
        )['total']

        # Add as attribute to question object
        question.total_votes = total_votes

        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        """
        Add voting statistics and percentages to context.
        """
        context = super().get_context_data(**kwargs)
        question = context['question']

        # Get all choices for this question
        choices = question.choice_set.all()

        # Calculate total votes
        total_votes = choices.aggregate(total=Sum('votes'))['total'] or 0

        # Calculate percentage for EACH choice and add it as an attribute
        for choice in choices:
            if total_votes > 0:
                # This adds the percentage attribute to each choice object
                choice.percentage = (choice.votes / total_votes) * 100
            else:
                choice.percentage = 0

        # Find the most popular choice
        most_popular_choice = None
        if total_votes > 0 and choices.exists():
            most_popular_choice = max(choices, key=lambda c: c.votes)

        # Add to question object
        question.total_votes = total_votes
        question.most_popular_choice = most_popular_choice

        # Add choices with percentages to context
        context['choices'] = choices

        return context

def vote(request, question_id):
    """
    Handle voting for a specific question.
    This remains a function-based view as it handles POST data.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with error message
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "You didn't select a choice."
            },
        )
    else:
        # Use F() to avoid race conditions
        selected_choice.votes = F('votes') + 1
        selected_choice.save()

        # Refresh the choice object to get updated votes
        selected_choice.refresh_from_db()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))