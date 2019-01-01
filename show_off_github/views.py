import json
import logging

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from github import Github
from github.NamedUser import NamedUser
import github

logger = logging.getLogger(__name__)

@login_required
def index(request):
    extra_data = request.user.social_auth.get(provider='github').extra_data
    # g = Github(extra_data['login'], extra_data['access_token'])
    g = github.MainClass.Github(extra_data['login'], extra_data['access_token'])
    project_arr = []
    logger.info("Fetching user repos from github")
    logger.warn("Fetching user repos from github")
    # logger.warining("Fetching user repos from github")

    
    # /user
    # GET: github.MainClass.Github.get_user()
    # PATCH: github.AuthenticatedUser.AuthenticatedUser.edit()


    # /user/repos
    # GET: github.AuthenticatedUser.AuthenticatedUser.get_repos()
    # POST: github.AuthenticatedUser.AuthenticatedUser.create_repo()


    # for a_repo in g.get_user().get_repos():
    #     current_repo = {}
    #     a_repo = ((g.get_repo(a_repo.parent.url.split('repos/')[1]))
    #               if a_repo.parent
    #               else a_repo)
    #     if a_repo.stargazers_count < 5:
    #         continue
    #     current_repo['id'] = a_repo.id
    #     current_repo['name'] = a_repo.name
    #     current_repo['stars'] = a_repo.stargazers_count
    #     current_repo['description'] = a_repo.description
    #     current_repo['avatar'] = a_repo.owner.avatar_url
    #     project_arr.append(current_repo)
    #     print(current_repo)
    # project_arr = sorted(project_arr, key=lambda val: val['stars'],
    #                      reverse=True)

    # /search/issues
    # GET: github.MainClass.Github.search_issues()
    # repositories = g.search_repositories(query='language:python')
    # for repo in repositories:
    #     print(repo)
    ret_val = g.search_issues(query='author:s-surineni', type='pr')

    for pr in ret_val:
        print(pr)
        print(pr.repository)
        print(dir(pr.repository))
        # print(dir(pr))
        current_repo = {}
        a_repo = pr.repository
        if a_repo.stargazers_count < 5:
            continue
        current_repo['id'] = a_repo.id
        current_repo['name'] = a_repo.name
        current_repo['stars'] = a_repo.stargazers_count
        current_repo['description'] = a_repo.description
        current_repo['avatar'] = a_repo.owner.avatar_url
        project_arr.append(current_repo)
        print(current_repo)
    project_arr = sorted(project_arr, key=lambda val: val['stars'],
                         reverse=True)
    print(ret_val.get_page(0))
    return HttpResponse(json.dumps(project_arr))
