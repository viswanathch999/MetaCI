from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from metaci.build.utils import view_queryset
from metaci.plan.models import Plan, PlanRepository
from metaci.plan.forms import RunPlanForm
from metaci.repository.models import Repository


def plan_list(request):
    if request.user.is_staff:
        plans = Plan.objects.all()
    else:
        plans = Plan.objects.filter(public=True)
    context = {
        'plans': plans,
    }
    return render(request, 'plan/list.html', context=context)

def plan_detail(request, plan_id):
    query = {'id': plan_id}
    if not request.user.is_staff:
        query['public'] = True
    plan = get_object_or_404(Plan, **query)

    query = {'plan': plan}
    builds = view_queryset(request, query)

    context = {
        'builds': builds,
        'plan': plan,
    } 
    return render(request, 'plan/detail.html', context=context)
    
def plan_detail_repo(request, plan_id, repo_owner, repo_name):
    query = {'id': plan_id}
    if not request.user.is_staff:
        query['public'] = True
    planrepo = get_object_or_404(PlanRepository, repo__owner=repo_owner, repo__name=repo_name, plan__id=plan_id)
    query = {'plan': planrepo.plan, 'repo': planrepo.repo}
    builds = view_queryset(request, query)

    context = {
        'builds': builds,
        'plan': planrepo.plan,
        'planrepo': planrepo,
        'repo': planrepo.repo
    }
    return render(request, 'plan/plan_repo_detail.html', context=context)

@staff_member_required
def plan_run(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    context = {'plan': plan, 'planrepos': plan.planrepository_set.should_run().all()}
    return render(request, 'plan/run_select_repo.html', context=context)

@staff_member_required
def plan_run_repo(request, plan_id, repo_owner, repo_name):
    plan = get_object_or_404(Plan, id=plan_id)
    repo = get_object_or_404(Repository, owner=repo_owner, name=repo_name)
    # this is a little hackish, but it will cause a 404 if the planrepo or the plan are inactive, preventing runplanform from ever occuring.
    planrepo = get_object_or_404(PlanRepository, plan_id=plan.id, repo_id=repo.id, active=True, plan__active=True)
    if request.method == 'POST':
        form = RunPlanForm(plan, repo, request.user, request.POST)
        if form.is_valid():
            build = form.create_build()
            return HttpResponseRedirect(build.get_absolute_url())
    else:
        form = RunPlanForm(plan, repo, request.user, request.GET)
    context = {
        'form': form,
        'plan': plan,
        'repo': repo,
    }
    return render(request, 'plan/run.html', context=context)
