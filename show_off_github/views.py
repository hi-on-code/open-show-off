import json
import logging

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from github import Github
from github.NamedUser import NamedUser
import github

logger = logging.getLogger(__name__)

@login_required
def index(request, userName=None):
    print('view', 'index in show_off_github')
    print('urls', request.path_info)
    extra_data = request.user.social_auth.get(provider='github').extra_data
    if not userName:
        userName = extra_data['login']
    g = github.MainClass.Github(extra_data['login'], extra_data['access_token'])
    project_arr = []
    logger.info("Fetching user repos from github")
    logger.warn("Fetching user repos from github")
    # logger.warining("Fetching user repos from github")
    ret_val = g.search_issues(query='author:{}'.format(userName), type='pr')
    uniq_ids = []
    for pr in ret_val:
        current_repo = {}
        a_repo = pr.repository
        if a_repo.stargazers_count < 5:
            continue
        current_repo['id'] = a_repo.id
        if a_repo.id in uniq_ids:
            continue
        uniq_ids.append(a_repo.id)
        current_repo['name'] = a_repo.name
        current_repo['stars'] = a_repo.stargazers_count
        current_repo['description'] = a_repo.description
        current_repo['avatar'] = a_repo.owner.avatar_url
        current_repo['html_url'] = a_repo.html_url
        project_arr.append(current_repo)
    project_arr = sorted(project_arr, key=lambda val: val['stars'],
                         reverse=True)
    return HttpResponse(json.dumps(project_arr))


def get_user_name(request):
    return HttpResponse(
        json.dumps(request.user.social_auth.get(provider='github')
                   .extra_data['login']))
