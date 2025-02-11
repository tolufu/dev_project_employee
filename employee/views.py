from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeCreateForm,TrainingCreateForm,SkillCreateForm
from .models import Employee,TrainingMaster,SkillMaster,EmployeeTraining,EmployeeSkill
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# 一画面あたりの表示件数
page_cnt = 10

# Create your views here.
def index(request):
    employee_list = Employee.objects.all()
    
    # ページネーションを適用
    paginator = Paginator(employee_list, page_cnt)
    page_number = request.GET.get("page")  # URLクエリパラメータからページ番号を取得
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,  # ページネーションされたオブジェクトを渡す
    }
    return render(request, "employee/list.html", context)


def add(request):
    # 送信内容をもとに、フォームを作成。POSTでなければ空のフォームを表示。
    form = EmployeeCreateForm(request.POST or None)
    
    # method=POST、つまり送信ボタンをクリック時、入力内容に問題なければ
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("employee:index")

    # 通常時のページアクセスや入力内容に誤りがあればページを再表示
    context = {
        "form": form  # EmployeeCreateForm() ではなく、form 変数を渡す
    }
    return render(request, "employee/info/add.html", context)

def update(request, pk):
    #urlのpkをもとに、Employeeを取得
    employee = get_object_or_404(Employee, pk=pk)

    #フォームに取得したEmployeeを紐づける
    form = EmployeeCreateForm(request.POST or None, instance=employee)

    #method=POST、つまり送信ボタンをクリック時、入力内容に問題がなければ
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("employee:index")
    
    #通常時のページアクセスや入力内容に誤りがあればページを再表示
    context = {
        "form":form
    }
    return render(request, "employee/info/update.html", context)

def delete(request, pk):
    #urlのpkをもとに、Employeeを取得
    employee = get_object_or_404(Employee, pk=pk)

    #method=POST、つまり送信ボタンをクリック時、入力内容に問題がなければ
    if request.method == "POST":
        employee.delete()
        return redirect("employee:index")
    
    #通常時のページアクセスや入力内容に誤りがあればページを再表示
    context = {
        "employee":employee
    }
    return render(request, "employee/info/confirm_delete.html", context)

def detail(request, pk):
    #urlのpkをもとに、Employeeを取得
    employee = get_object_or_404(Employee, pk=pk)
    training_list = EmployeeTraining.objects.filter(employee=employee).select_related('training')
    skill_list = EmployeeSkill.objects.filter(employee=employee).select_related('skill')

    # 通常時のページアクセスや入力内容に誤りがあればページを再表示
    context = {
        "employee": employee,
        "training_list": training_list,  # 複数のトレーニングをリストで渡す
        "skill_list": skill_list  # 複数のスキルをリストで渡す
    }

    return render(request, "employee/detail.html", context)

def train_add_update(request, pk, training_id=None):
    employee = get_object_or_404(Employee, pk=pk)
    training_list = EmployeeTraining.objects.filter(employee=employee).select_related('training')

    if training_id:
        training_instance = get_object_or_404(EmployeeTraining, employee=employee, training__training_id=training_id)
        form = TrainingCreateForm(request.POST or None, instance=training_instance)
    else:
        form = TrainingCreateForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        training = form.save(commit=False)
        training.employee = employee

        # training フィールドの値が空でないか確認
        if not training.training_id:
            form.add_error("training", "トレーニングを選択してください。")
        else:
            training.save()
            return redirect("employee:detail", pk=employee.pk)

    context = {
        "form": form,
        "employee": employee,
        "training_list": training_list,
        "is_update": bool(training_id),
    }
    return render(request, "employee/training/add_update.html", context)

def skill_add_update(request, pk, skill_id=None):
    employee = get_object_or_404(Employee, pk=pk)
    skill_list = EmployeeSkill.objects.filter(employee=employee).select_related('skill')

    if skill_id:
        # 更新時（該当のトレーニングを取得）
        skill_instance = get_object_or_404(EmployeeSkill, employee=employee, skill_id=skill_id)
        form = SkillCreateForm(request.POST or None, instance=skill_instance)
    else:
        # 新規登録時（空のフォーム）
        form = SkillCreateForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        skill = form.save(commit=False)
        skill.employee = employee

        # training フィールドの値が空でないか確認
        if not skill.skill_id:
            form.add_error("skill", "スキルを選択してください。")
        else:
            skill.save()
            return redirect("employee:detail", pk=employee.pk)

    context = {
        "form": form,
        "employee": employee,
        "skill_list": skill_list,
        "is_update": bool(skill_id),  # 更新か新規登録か判定
    }
    return render(request, "employee/skill/add_update.html", context)

def train_delete(request, pk, training_id):
    employee = get_object_or_404(Employee, pk=pk)
    training_instance = get_object_or_404(EmployeeTraining.objects.select_related("training"), employee=employee, training__training_id=training_id)

    if request.method == "POST":
        training_instance.delete()
        return redirect("employee:detail", pk=employee.pk)

    context = {
        "employee": employee,
        "training": training_instance.training,
        "get_date": training_instance.get_date
    }
    return render(request, "employee/training/confirm_delete.html", context)

def skill_delete(request, pk, skill_id):
    employee = get_object_or_404(Employee, pk=pk)
    skill_instance = get_object_or_404(EmployeeSkill.objects.select_related("skill"), employee=employee, skill__skill_id=skill_id)

    if request.method == "POST":
        skill_instance.delete()
        return redirect("employee:detail", pk=employee.pk)

    context = {
        "employee": employee,
        "skill": skill_instance.skill,
        "get_date": skill_instance.get_date
    }
    return render(request, "employee/skill/confirm_delete.html", context)
