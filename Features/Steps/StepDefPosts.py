import requests
from behave import *

from Data.body import bodyPost
from Utils.configurations import *
from Utils.resources import *


@given(u'the typicode get posts details')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + GET_TYPICODE_POSTS
    context.headers = {"Content-Type": "application/json"}


@when(u'post endpoint is executed')
def step_impl(context):
    context.typicode_get_request = requests.get(context.url, headers=context.headers)


@then(u'post response should displayed correctly')
def step_impl(context):
    assert context.typicode_get_request.status_code == 200
    assert len(context.typicode_get_request.json()) > 0
    for each in context.typicode_get_request.json():
        assert "userId" in each
        assert isinstance(each["userId"], int)
        assert each["userId"] > 0
        assert "id" in each
        assert isinstance(each["id"], int)
        assert each["id"] > 0
        assert "title" in each
        assert each["title"] != ""
        assert "body" in each
        assert each["body"] != ""

@given(u'the typicode get single posts details')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + GET_TYPICODE_SINGLE_POSTS
    context.headers = {"Content-Type": "application/json"}


@when(u'single post endpoint is executed')
def step_impl(context):
    context.typicode_get_request = requests.get(context.url, headers=context.headers)


@then(u'single post response should be displayed correctly')
def step_impl(context):
    assert context.typicode_get_request.status_code == 200
    assert "userId" in context.typicode_get_request.json()
    assert type(context.typicode_get_request.json()["userId"]) == int
    assert context.typicode_get_request.json()["userId"] == 1
    assert "id" in context.typicode_get_request.json()
    assert type(context.typicode_get_request.json()["id"]) == int
    assert context.typicode_get_request.json()["id"] == 1
    assert "title" in context.typicode_get_request.json()
    assert type(context.typicode_get_request.json()["title"]) == str
    assert "body" in context.typicode_get_request.json()
    assert type(context.typicode_get_request.json()["body"]) == str

@given(u'the typicode get posts comments details')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + GET_TYPICODE_COMMENTS_POSTS
    context.headers = {"Content-Type": "application/json"}

@when(u'comments post endpoint is executed')
def step_impl(context):
    context.typicode_get_request = requests.get(context.url, headers=context.headers)


@then(u'comments post response should be displayed correctly')
def step_impl(context):
    assert context.typicode_get_request.status_code == 200
    assert len(context.typicode_get_request.json()) > 0
    for each in context.typicode_get_request.json():
        assert "postId" in each
        assert type(each["postId"]) == int
        assert context.typicode_get_request.json()[0]["postId"] == 1
        assert "id" in each
        assert type(each["id"]) == int
        assert each["id"] > 0
        assert "name" in each
        assert type(each["name"]) == str
        assert "email" in each
        assert type(each["email"]) == str
        assert "body" in each
        assert type(each["body"]) == str


@given(u'the typicode get post id details')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + GET_TYPICODE_POST_ID
    context.headers = {"Content-Type": "application/json"}


@when(u'post id endpoint is executed')
def step_impl(context):
    context.typicode_get_request = requests.get(context.url, headers=context.headers)


@then(u'comments should only display posts id 1')
def step_impl(context):
    assert context.typicode_get_request.status_code == 200
    assert len(context.typicode_get_request.json()) > 0
    for each in context.typicode_get_request.json():
        assert "postId" in each
        assert isinstance(each["postId"], int)
        assert each["postId"] == 1
        assert "id" in each
        assert isinstance(each["id"], int)
        assert each["id"] > 0
        assert "name" in each
        assert isinstance(each["name"], str)
        assert each["name"] != ""
        assert "email" in each
        assert isinstance(each["email"], str)
        assert each["email"] != ""
        assert "body" in each
        assert isinstance(each["body"], str)
        assert each["body"] != ""

@given(u'the typicode post comments details given {title} and {body}')
def step_impl(context, title, body):
    context.url = getConfig()['API']['endpoint'] + GET_TYPICODE_POSTS
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = bodyPost(title, body);


@when(u'comments with body post is executed')
def step_impl(context):
    context.typicode_get_request = requests.post(context.url, headers=context.headers)


@then(u'comments should contain the same {title} and {body}')
def step_impl(context, title, body):
    assert context.typicode_get_request.status_code == 201
    assert "id" in context.typicode_get_request.json()
    assert isinstance(context.typicode_get_request.json()["id"], int)
    assert context.typicode_get_request.json()["id"] != ""
