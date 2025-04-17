import requests

base_url = "https://ru.yougile.com"
token = 'hCY5coI9yxfqh+eB4TC2v7FXhNC-zfK7NkqU27JzPwWvdo+hCnMWWkktPhMh47fk'

def get_projects_list():
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : "Bearer " + token
    }
    resp = requests.get(base_url + '/api-v2/projects', headers=headers) # list of all projects
    return resp.json()


def create_projects(title):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + token
    }
    projects = {"title" : title}
    resp = requests.post(base_url + '/api-v2/projects', headers=headers, json=projects) # project creation
    return resp.json()


def edit_project(new_id, title):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + token
    }
    projects = {"title": title}

    requests.put(base_url + '/api-v2/projects/' + new_id,  headers=headers, json=projects)
    result = requests.get(base_url + '/api-v2/projects/' + new_id, headers=headers)
    return result.json()

def get_project_id(new_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + token
    }

    resp = requests.get(base_url + '/api-v2/projects', headers=headers)
    return resp.json()



def test_create_project():
    body = get_projects_list()
    len_before = body['paging']['count']

    title = "QA Engeneering"
    result = create_projects(title)
    new_id = result["id"]

    body = get_projects_list()
    len_after = body['paging']['count']

    assert len_after - len_before == 1
    assert body['content'][-1]["id"] == new_id



def test_get_projects_list():
    body = get_projects_list()
    assert len(body) > 0



def test_edit_project():
    title = "Engeneering QA"
    result = create_projects(title)
    new_id = result["id"]

    new_title = "Помощь куратора"
    edited = edit_project(new_id, new_title)
    assert edited['title'] == new_title


def test_get_project_id():
    title = "Автоматизаця"
    result = create_projects(title)
    new_id = result["id"]

    project = get_project_id(new_id)

    assert project["id"] == new_id
    assert project["title"] == title




















