import requests

def get_posts():
    response = requests.get(f"{url}/posts")
    if response.status_code == 200:
        data = response.json()
        title_result = []
        body_result = []
        
        for _dict in data:
            title = _dict['title'].split()
            body = _dict['body'].split('\n')
            
            if len(title) > 6:
                title_result.append(_dict)
                    
            if len(body) > 3:
                body_result.append(_dict)
                
        print("Posts whose title contains more than 6 words:\n", title_result)
        print("\nPosts whose body contains more than 3 lines of description(\\n):\n", body_result, '\n')
    else:
        print("Failed get posts.")
        
def create_post():
    post = {
        "title": "New title", 
        "body": "New text",
        "userId": 10 
    }    
    response = requests.post(f"{url}/posts", json=post)
    
    if response.status_code == 201:
        print(f"Created post: {response.json()}")
    else:
        print("Post wasn't created.")
        
def update_post(post_id):
    post = {
        "title": "Updated title", 
        "body": "Updated text",
        "userId": 5
    }
    response = requests.put(f"{url}/posts/{post_id}", json=post)
    
    if response.status_code == 200:
        print(f"Updated post: {response.json()}")
    else:
        print("Post wasn't updated.")
        
def delete_post(post_id):
    response = requests.delete(f"{url}/posts/{post_id}")
    
    if response.status_code == 200:
        print(f"Post {post_id} deleted.")
    else:
        print("Post wasn't deleted.")
    
if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    
    get_posts()
    create_post()
    update_post(8)
    delete_post(2)
