import json

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from github import Github
from github.NamedUser import NamedUser

# from social_django import social_auth_usersocialauth



# g = Github('s-surineni', ACCESS_TOKEN)

@login_required
def index(request):
    # print('request', request.GET)
    # print('request', request.user)
    # print('request', dir(request.user))
    extra_data = request.user.social_auth.get(provider='github').extra_data
    print('request', request.user.social_auth.get(provider='github').extra_data)
    # print('request', dir(request.session))
    g = Github(extra_data['login'], extra_data['access_token'])
    # print('request', request.session)

    project_arr = [
        
    ]
    for a_repo in g.get_user().get_repos()[:10]:
        
        # print(a_repo.name, a_repo.stargazers_count, a_repo.url)
        # g.AuthenticatedUser.AuthenticatedUser.get_repo(repo.url)
        # print((a_repo.url.split('repos/')[1]))
        current_repo = {}
        if a_repo.parent:
            parent_repo = (g.get_repo(a_repo.parent.url.split('repos/')[1]))
            # current_repo['id'] = parent_repo.id
            current_repo['id'] = parent_repo.stargazers_count
            current_repo['name'] = parent_repo.name

        else:
            current_repo['id'] = a_repo.id
            current_repo['name'] = a_repo.name
        project_arr.append(current_repo)

        # print(dir(a_repo))


    return HttpResponse(json.dumps(project_arr))
