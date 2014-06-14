import hashlib
import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from challenge.models import Challenge, Answer


def index(request):
    return render(request, 'challenge/index.html', {'challenge_list': Challenge.objects.all()})


def detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    return render(request, 'challenge/detail.html', {'challenge': challenge})


def answer(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    user_answer = request.POST['answer']
    is_solved = False
    for a in challenge.get_answers():
        if a.answer_type == Answer.HASH:
            if a.answer == hashlib.sha1(user_answer).hexdigest():
                is_solved = True
                break
        elif a.answer_type == Answer.REGEXP:
            try:
                if re.match(a.answer, user_answer):
                    is_solved = True
                    break
            except re.error:
                is_solved = False
        else:
            is_solved = False

    if is_solved:
        return HttpResponseRedirect(reverse('challenge:solved', args=(challenge.id,)))
    else:
        return render(request, 'challenge/detail.html', {
            'challenge': challenge,
            'error_message': "Mal, intenta otra vez",
        })


# Proteger?
def solved(request, challenge_id):
    challenge = get_object_or_404(Challenge, pk=challenge_id)
    return render(request, 'challenge/solved.html', {'challenge': challenge, 'score': challenge.get_score()})
