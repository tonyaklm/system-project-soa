import time
import requests


def wait_for_http(url):
    retries = 10
    exception = None
    while retries > 0:
        try:
            requests.get(url)
            return
        except requests.exceptions.ConnectionError as e:
            exception = e
            print(f'Got ConnectionError for url {url}: {e} , retrying')
            retries -= 1
            time.sleep(2)
    raise exception


social_media_url = 'http://127.0.0.1:8000'
wait_for_http(social_media_url)


def test_post_user():
    user = {
        "first_name": "Петя",
        "last_name": "Петров",
        "date_of_birth": "02.02.2000",
        "mail": "mail",
        "phone_number": "8888888",
        "login": "user",
        "password": "user_password"
    }
    resp = requests.post(social_media_url + '/user/registration', json=user)
    # assert resp.status_code == 200, resp.text


def user_authentication():
    user_data = {
        "login": "user",
        "password": "user_password"
    }
    resp = requests.post(social_media_url + '/user/authentication', json=user_data)
    print(resp)
    return resp.json()["session_key"]


def test_post_new_post():
    post_data = {
        "title": "some_title",
        "content": "some_content"
    }
    headers = {"accept": "application/json",
               "session-key": user_authentication(),
               'Content-Type': 'application/json'}
    resp = requests.post(social_media_url + '/post/create', json=post_data, headers=headers)
    assert resp.status_code == 200


def get_posts():
    headers = {"accept": "application/json",
               "session-key": user_authentication(),
               'Content-Type': 'application/json'}
    resp = requests.get(social_media_url + '/post', headers=headers)
    assert resp.status_code == 200
    print(resp.content)
    items = resp.json()['items']
    max_post_id = 0
    for item in items:
        max_post_id = max(max_post_id, item['id'])
    return max_post_id


def test_get_post_not_found():
    headers = {"accept": "application/json",
               "session-key": user_authentication(),
               'Content-Type': 'application/json'}
    resp = requests.get(social_media_url + '/post/100', headers=headers)
    assert resp.status_code == 404


def test_like_error():
    new_like = {
        "post_id": get_posts() + 1
    }
    headers = {"accept": "application/json",
               "session-key": user_authentication(),
               'Content-Type': 'application/json'}
    resp = requests.post(social_media_url + '/statistics/like', json=new_like, headers=headers)
    assert resp.status_code == 404


def test_like_correct():
    new_like = {
        "post_id": get_posts()
    }
    headers = {"accept": "application/json",
               "session-key": user_authentication(),
               'Content-Type': 'application/json'}
    resp = requests.post(social_media_url + '/statistics/like', json=new_like, headers=headers)
    assert resp.status_code == 200


def test_view_correct():
    new_view = {
        "post_id": get_posts()
    }
    headers = {"accept": "application/json",
               "session-key": user_authentication(),
               'Content-Type': 'application/json'}
    for i in range(5):
        resp = requests.post(social_media_url + '/statistics/view', json=new_view, headers=headers)
        assert resp.status_code == 200
