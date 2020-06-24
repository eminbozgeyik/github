import requests


class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '7846dce252b4cbff31140f7aac603ec3272ae309'

    def getUser(self,username):
        response = requests.get(self.api_url+'/users/'+username)
        return response.json()
    
    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()

    def createRepository(self,name):
        response = requests.post(self.api_url+'/user/repos?access_token='+self.token, json={
            "login": "octocat",
            "id": 1,
            "node_id": "MDQ6VXNlcjE=",
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": "",
            "url": "https://api.github.com/users/octocat",
            "html_url": "https://github.com/octocat",
            "followers_url": "https://api.github.com/users/octocat/followers",
            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "organizations_url": "https://api.github.com/users/octocat/orgs",
            "repos_url": "https://api.github.com/users/octocat/repos",
            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
            "received_events_url": "https://api.github.com/users/octocat/received_events",
            "type": "User",
            "site_admin": False,
            "name": "name",
            "company": "GitHub",
            "blog": "https://github.com/blog",
            "location": "San Francisco",
            "email": "octocat@github.com",
            "hireable": False,
            "bio": "There once was...",
            "twitter_username": "monatheoctocat",
            "public_repos": 2,
            "public_gists": 1,
            "followers": 20,
            "following": 0,
            "created_at": "2008-01-14T04:33:35Z",
            "updated_at": "2008-01-14T04:33:35Z"
        })
        return response.json()

github = Github() 

while True:
    secim = input('1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSecim: ')

    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
        elif secim == '2':
            username = input('username: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            name = input('repository name: ')
            result = github.createRepository(name)
            print(result)
        else:
            print('Yanlis secim')
