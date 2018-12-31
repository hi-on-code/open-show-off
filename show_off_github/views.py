import json
import logging

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from github import Github
from github.NamedUser import NamedUser

logger = logging.getLogger(__name__)

@login_required
def index(request):
    extra_data = request.user.social_auth.get(provider='github').extra_data
    g = Github(extra_data['login'], extra_data['access_token'])

    project_arr = [
        
    ]
    logger.info("Fetching user repos from github")
    logger.warn("Fetching user repos from github")
    # logger.warining("Fetching user repos from github")
    for a_repo in g.get_user().get_repos():
        a_repo = (g.get_repo(a_repo.parent.url.split('repos/')[1])) if a_repo.parent else a_repo
        current_repo = {}
        current_repo['avatar'] = a_repo.owner.avatar_url
        current_repo['description'] = a_repo.description
        current_repo['id'] = a_repo.id
        current_repo['name'] = a_repo.name
        current_repo['stars'] = a_repo.stargazers_count
        project_arr.append(current_repo)
    return HttpResponse(json.dumps(project_arr))
