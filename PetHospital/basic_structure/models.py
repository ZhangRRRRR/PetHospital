from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    sex = models.BooleanField
    birthday = models.DateTimeField('Birthday')

class Department(models.Model):
    name = models.CharField(max_length=200)
    duty = models.CharField(max_length=1000)
    leaderID = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Charge(models.Model):
    name = models.CharField(max_length=200)
    standard = models.CharField(max_length=1000)
    note = models.CharField(max_length=500)

class LaboratoryTest(models.Model):
    name = models.CharField(max_length=200)
    standard = models.CharField(max_length=1000)
    note = models.CharField(max_length=500)

# admission info for hospitalization
class Admission(models.Model):
    pet_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    doctor = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='doctor_id')
    nurse = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='nurse_id')
    admission_date = models.DateTimeField("Date of admission")

# record for hospitalization
class Record(models.Model):
    record_date = models.DateTimeField("Record Date")
    status = models.CharField(max_length=500)

class Hospitalization(models.Model):
    admissionID = models.ForeignKey(Admission, on_delete=models.CASCADE)
    recordID = models.ForeignKey(Record, on_delete=models.CASCADE)
    class Meta:
        unique_together = ("admissionID", "recordID")