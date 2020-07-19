from django.db import models
from university.models import *
from django.utils import timezone
from django.db.models import signals

# Create your models here.
def delete_review(sender, instance, **kwargs):
    uni = instance.university
    prog = instance.program

    reviews = Review.objects.all()

    reviews_uni = [x for x in reviews if x.university.id == uni.id]
    reviews_prog = [x for x in reviews if x.program.id == prog.id]

    u_mean = 0.0;
    prog_mean = 0.0;

    for rev in reviews_uni:
        u_mean += rev.uni_calification

    for rev in reviews_prog:
        prog_mean += rev.prog_calification


    if(len(reviews_uni) != 0):
        u_mean /= len(reviews_uni)
    if (len(reviews_prog) != 0):
        prog_mean /= len(reviews_prog)

    u_mean = round(u_mean, 1)
    prog_mean = round(prog_mean, 1)

    uni.rating = u_mean
    uni.save()
    prog.prog_calification = prog_mean
    prog.save()


def create_review(sender, instance, created, **kwargs):
    if created:
        uni = instance.university
        prog = instance.program

        reviews = Review.objects.all()

        reviews_uni = [x for x in reviews if x.university.id == uni.id]
        reviews_prog = [x for x in reviews if  x.program.id == prog.id]

        u_mean = 0.0;
        prog_mean = 0.0;

        for rev in reviews_uni:
            u_mean+=rev.uni_calification

        for rev in reviews_prog:
            prog_mean+=rev.prog_calification

        u_mean/=len(reviews_uni)
        prog_mean/=len(reviews_prog)

        u_mean = round(u_mean, 1)
        prog_mean = round(prog_mean, 1)

        uni.rating = u_mean
        uni.save()
        prog.prog_calification = prog_mean
        prog.save()


class Review(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    uni_description = models.CharField(max_length=400)
    prog_description = models.CharField(max_length=400)
    uni_calification = models.FloatField(default=0.0)
    prog_calification = models.FloatField(default=0.0)
    create_date = models.DateField(default=timezone.now)


signals.post_save.connect(receiver=create_review, sender=Review)
signals.post_delete.connect(receiver=delete_review, sender=Review)







