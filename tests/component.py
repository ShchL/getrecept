import pytest
import requests

def test_root_get():
    res = requests.get('http://localhost:80/').json()
    pytest.assume('id' in res.keys())
    pytest.assume('info' in res.keys())
    pytest.assume(type(res['id']) == int)


def test_list_get():
    res = requests.get('http://localhost:80/list/?q=345').json()
    res = res[0]
    pytest.assume(res['id']=='345')
    pytest.assume(res['info']['title']=='Cook the Book Party Planner: Pasta with Sardines')
    pytest.assume(res['info']['image']=="https://spoonacular.com/recipeImages/345-556x370.jpg")
    print(res['info']['image'])
    