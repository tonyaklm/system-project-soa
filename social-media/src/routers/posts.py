from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse
import models
from post_handle.PostHandler import post_handler
from start_session import get_session
from routers.users import user_authorization
from fastapi import Depends
import json
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/create-post", status_code=200, summary="Create new post",
             response_model=models.NewPostResponse, tags=['post'])
async def create_post(post_data: models.BaseNewPost, session: AsyncSession = Depends(get_session)):
    auth_data = models.BaseAuthorizationData(login=post_data.login, password=post_data.password)
    auth_response = await user_authorization(auth_data, session)
    if auth_response.status_code != 200:
        return JSONResponse(status_code=auth_response.status_code, content=json.loads(auth_response.body))
    json_post_data = json.loads(post_data.model_dump_json())
    del json_post_data["password"]
    del json_post_data["login"]
    json_post_data['user_id'] = json.loads(auth_response.body)['user_id']
    new_id = post_handler.CreatePost(json_post_data)
    return new_id


@router.put("/post", status_code=200, summary="Update post", tags=['post'])
async def update_post(post_data: models.BaseUpdatePost, session: AsyncSession = Depends(get_session)):
    auth_data = models.BaseAuthorizationData(login=post_data.login, password=post_data.password)
    auth_response = await user_authorization(auth_data, session)
    if auth_response.status_code != 200:
        return JSONResponse(status_code=auth_response.status_code, content=json.loads(auth_response.body))

    json_post_data = json.loads(post_data.model_dump_json())
    del json_post_data["password"]
    del json_post_data["login"]
    json_post_data['user_id'] = json.loads(auth_response.body)['user_id']
    return post_handler.UpdatePost(json_post_data)


@router.delete("/delete-post", status_code=204, summary="Delete post by its id", tags=['post'])
async def delete_post(post_data: models.BaseDeletePost, session: AsyncSession = Depends(get_session)):
    auth_data = models.BaseAuthorizationData(login=post_data.login, password=post_data.password)
    auth_response = await user_authorization(auth_data, session)
    if auth_response.status_code != 200:
        return JSONResponse(status_code=auth_response.status_code, content=json.loads(auth_response.body))
    json_post_data = json.loads(post_data.model_dump_json())
    del json_post_data["password"]
    del json_post_data["login"]
    json_post_data['user_id'] = json.loads(auth_response.body)['user_id']
    return post_handler.DeletePost(json_post_data)


@router.get("/get-post-by-id", status_code=200, summary="Get post by its id",
            response_model=models.PostItem, tags=['post'])
async def get_post_by_id(post_data: models.RequestGetPostById, session: AsyncSession = Depends(get_session)):
    auth_data = models.BaseAuthorizationData(login=post_data.login, password=post_data.password)
    auth_response = await user_authorization(auth_data, session)
    if auth_response.status_code != 200:
        return JSONResponse(status_code=auth_response.status_code, content=json.loads(auth_response.body))
    json_post_data = json.loads(post_data.model_dump_json())
    del json_post_data["password"]
    del json_post_data["login"]
    json_post_data['user_id'] = json.loads(auth_response.body)['user_id']
    return post_handler.GetPostById(json_post_data)


@router.get("/get-posts", status_code=200, summary="Get all posts for user",
            response_model=List[models.PostItem], tags=['post'])
async def get_posts(post_data: models.RequestGetPosts, session: AsyncSession = Depends(get_session)):
    auth_data = models.BaseAuthorizationData(login=post_data.login, password=post_data.password)
    auth_response = await user_authorization(auth_data, session)
    if auth_response.status_code != 200:
        return JSONResponse(status_code=auth_response.status_code, content=json.loads(auth_response.body))
    json_post_data = json.loads(post_data.model_dump_json())
    del json_post_data["password"]
    del json_post_data["login"]
    json_post_data['user_id'] = json.loads(auth_response.body)['user_id']
    return post_handler.GetPosts(json_post_data)
