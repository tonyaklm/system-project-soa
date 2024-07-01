from fastapi import APIRouter
from schemas import posts_schemas
from handle.post_handler import post_handler
from fastapi import Depends
import json
from tables.user import User
from utils.auth import get_user
from fastapi_pagination import Page, paginate

router = APIRouter(prefix="/post")


@router.post("/create", status_code=200, summary="Create new post",
             response_model=posts_schemas.NewPostResponse, tags=['post'])
async def create_post(post_data: posts_schemas.BaseNewPost, user: User = Depends(get_user)):
    json_post_data = json.loads(post_data.model_dump_json())
    json_post_data['user_id'] = user.id
    new_id = post_handler.CreatePost(json_post_data)
    return new_id


@router.put("/", status_code=200, summary="Update post", tags=['post'])
async def update_post(post_data: posts_schemas.BaseUpdatePost, user: User = Depends(get_user)):
    json_post_data = json.loads(post_data.model_dump_json())
    json_post_data['user_id'] = user.id
    return post_handler.UpdatePost(json_post_data)


@router.delete("/{post_id}", status_code=204, summary="Delete post by its id", tags=['post'])
async def delete_post(post_id: int, user: User = Depends(get_user)):
    json_post_data = {'user_id': user.id,
                      'post_id': post_id}
    return post_handler.DeletePost(json_post_data)


@router.get("/{post_id}", status_code=200, summary="Get post by its id",
            response_model=posts_schemas.PostItem, tags=['post'])
async def get_post_by_id(post_id: int):
    json_post_data = {'post_id': post_id}
    return post_handler.GetPostById(json_post_data)


@router.get("/", status_code=200, summary="Get all posts for user",
            response_model=Page[posts_schemas.PostItem], tags=['post'])
async def get_posts() -> Page[posts_schemas.PostItem]:
    posts = post_handler.GetPosts({})
    return paginate(posts)
