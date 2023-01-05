from fastapi import FastAPI, Path, Query, HTTPException, status

from typing import Optional
from data.inventory import inventory
from data.posts import posts
from models.post import Post, UpdatePost


app = FastAPI()


#1. Simple Route
@app.get("/")
def home():
    return {
        "data": "Hello World"
    }


#2. Url Parameter
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory.get(item_id)


#3. Url Parameter Using Path
@app.get("/get-item-test/{item_id}")
def get_item(item_id: int = Path(None, description="Provide Item ID", gt=0, lt=2)):
    return inventory.get(item_id)


#4. Query Parameter
@app.get("/get-item-by-name")
def get_item(name: str):
    for item_id in inventory:
        if name == inventory[item_id]['name']:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found")


#5. Query Parameters with default value (optional)
@app.get("/get-item-by-name-test1")
def get_item(name: Optional[str] = "Laptop"):
    for item_id in inventory:
        if name == inventory[item_id]['name']:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found")


#6. Multiple Query Parameters
@app.get("/get-item-by-name-test2")
def get_item(name: Optional[str]=None, test: int=None):
    print("name: ", name)
    print("test: ", test)
    for item_id in inventory:
        if name == inventory[item_id]['name']:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item Not Found")


#7. Combine Url and Query Parameters
@app.get("/get-item-by-id-and-name/{item_id}")
def get_item(item_id: int, name: Optional[str]=None):
    # Todo: Don't have time to implement that shit logic :)
    return {'item_id': item_id, 'name':name}


#8. Post Request
@app.post("/create-post/{post_id}")
def create_post(post_id: int, post: Post):
    if post_id in posts:
        raise HTTPException(status_code=400, detail="Post Alreadt exists.")
    posts[post_id] = post
    return posts[post_id]


#9. Put Request
@app.put("/update-post/{post_id}")
def update_post(post_id: int, post: UpdatePost):
    if post_id not in posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    posts[post_id].title = post.title if post.title else posts[post_id].title
    posts[post_id].content = post.content if post.content else posts[post_id].content
    posts[post_id].post_by = post.post_by if post.post_by else posts[post_id].post_by
    return posts[post_id]


#9. Delete Request
@app.delete("/delete-post")
def delete_post(post_id: int=Query(..., description="Provide Post ID you want to delete")):
    if post_id not in posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")
    del posts[post_id]
    return {"success": "Post successfully delete!"}