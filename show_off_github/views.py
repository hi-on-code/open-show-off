import json

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from github import Github
from github.NamedUser import NamedUser

# from social_django import social_auth_usersocialauth



# g = Github('s-surineni', ACCESS_TOKEN)

@login_required
def index(request):
    extra_data = request.user.social_auth.get(provider='github').extra_data
    g = Github(extra_data['login'], extra_data['access_token'])

    project_arr = [
        
    ]
    all_repos = g.get_user().get_repos()
    print('all_repos', all_repos)
    for a_repo in all_repos:
        print(a_repo)
        # g.AuthenticatedUser.AuthenticatedUser.get_repo(repo.url)
        current_repo = {}
        if a_repo.parent:
            parent_repo = (g.get_repo(a_repo.parent.url.split('repos/')[1]))
            # current_repo['id'] = parent_repo.id
            current_repo['id'] = parent_repo.id
            current_repo['name'] = parent_repo.name
            current_repo['stars'] = parent_repo.stargazers_count

        else:
            current_repo['id'] = a_repo.id
            current_repo['name'] = a_repo.name
            current_repo['stars'] = a_repo.stargazers_count
        project_arr.append(current_repo)



    return HttpResponse(json.dumps(project_arr))
