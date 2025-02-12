from django.db import models
from django.core.validators import RegexValidator

class NumValidator(RegexValidator):
    regex = r'^[0-9]+\Z'
    message = "ゼッケンNoは数字のみで入力してください。"
    
    
    def __call__(self, value):
        return super().__call__(value)

class Employee(models.Model):
    val = NumValidator()
    employee_id = models.CharField("社員番号", max_length=6, primary_key=True,validators=[val])
    last_name = models.CharField("姓", max_length=40)
    first_name = models.CharField("名", max_length=40)
    birth_date = models.DateField("誕生日")
    
    @property
    def employee_name(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "社員情報"
        verbose_name_plural = "社員情報一覧"

    def __str__(self):
        return self.employee_name


class TrainingMaster(models.Model):
    training_id = models.CharField("トレーニングID", max_length=8, primary_key=True)
    training_name = models.CharField("トレーニング名", max_length=40)

    class Meta:
        verbose_name = "トレーニングマスタ"
        verbose_name_plural = "トレーニングマスタ一覧"

    def __str__(self):
        return self.training_name


class SkillMaster(models.Model):
    skill_id = models.CharField("スキルID", max_length=8, primary_key=True)
    skill_name = models.CharField("スキル名", max_length=40)

    class Meta:
        verbose_name = "スキルマスタ"
        verbose_name_plural = "スキルマスタ一覧"

    def __str__(self):
        return self.skill_name

class EmployeeTraining(models.Model):
    employee = models.ForeignKey(Employee, verbose_name="社員番号", on_delete=models.CASCADE)
    training = models.ForeignKey(TrainingMaster, verbose_name="トレーニングID", on_delete=models.CASCADE)
    get_date = models.DateField("取得日")

    class Meta:
        unique_together = ('employee', 'training')
        verbose_name = "社員取得トレーニング"
        verbose_name_plural = "社員取得トレーニング一覧"

    def __str__(self):
        return f"{self.employee.employee_name} - {self.training.training_name}"


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(Employee, verbose_name="社員番号", on_delete=models.CASCADE)
    skill = models.ForeignKey(SkillMaster, verbose_name="スキルID", on_delete=models.CASCADE)
    get_date = models.DateField("取得日")

    class Meta:
        unique_together = ('employee', 'skill')
        verbose_name = "社員取得スキル"
        verbose_name_plural = "社員取得スキル一覧"

    def __str__(self):
        return f"{self.employee.employee_name} - {self.skill.skill_name}"