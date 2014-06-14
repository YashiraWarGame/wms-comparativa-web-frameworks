from django.db import models


class Challenge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    def __unicode__(self):
        return self.name

    def get_score(self):
        return Score.objects.get(challenge=self)

    def get_answers(self):
        return Answer.objects.filter(challenge=self)


class Score(models.Model):
    STATIC = 0
    DYNAMIC = 1
    SCORE_TYPE_CHOICES = (
        (STATIC, 'Static'),
        (DYNAMIC, 'Dynamic'),
    )
    challenge = models.OneToOneField(Challenge)
    score_type = models.PositiveSmallIntegerField(choices=SCORE_TYPE_CHOICES, default=STATIC)
    score = models.DecimalField(max_digits=4, decimal_places=2)

    def __unicode__(self):
        return str(self.score)


class Answer(models.Model):
    HASH = 0
    REGEXP = 1
    ANSWER_TYPE_CHOICES = (
        (HASH, 'Hash'),
        (REGEXP, 'Regular Expression'),
    )
    challenge = models.ForeignKey(Challenge)
    answer_type = models.PositiveSmallIntegerField(choices=ANSWER_TYPE_CHOICES, default=HASH)
    answer = models.CharField(max_length=256)

    def __unicode__(self):
        return self.answer