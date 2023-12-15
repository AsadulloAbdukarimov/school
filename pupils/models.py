from django.db import models

# Create your models here.
class Exam_materials(models.Model):
    reference=models.TextField(verbose_name="Imtixon uchun Ma'lumot")
    links=models.URLField(verbose_name='Material uchun link', blank=True, null=True)
    material_dateTime=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='materials'
        ordering=('-material_dateTime',)

class Courses(models.Model):
    course_name=models.CharField(max_length=255, verbose_name='Kurs nomi')
    course_desc=models.CharField(max_length=200, verbose_name='Kurs haqida izoh ')
    course_teacher=models.CharField(max_length=200, verbose_name="Kurs o'qituvchisi")
    course_price=models.IntegerField(verbose_name='Kurs narxi', blank=True, null=True)

    class Meta:
        db_table='courses'

    def __str__(self):
        return f'{self.id}.{self.course_name}'


class BestPupils(models.Model):
    pupil_name=models.CharField(max_length=30, verbose_name='Ism')
    pupil_surname=models.CharField(max_length=30, verbose_name='Familyas')
    pupil_achievements=models.TextField(verbose_name='Yutuqlari')
    pupil_smm=models.URLField(verbose_name='Ijtimoiy tarmoqdagi sahifalari uchun link')

    class Meta:
        db_table='best_pupils'

    def __str__(self):
        return f'{self.id}. {self.pupil_name}'

