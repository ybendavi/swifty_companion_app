
import os
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from flask import Flask, redirect, abort, request, Response, jsonify
import time
from flask_cors import CORS

app = Flask(__name__)
oauth = None
token_expires_in = None
token_expiry_timestamp = None
token = None
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}}, expose_headers=["X-API-KEY"])

@app.before_request
def check_https_and_api_key():
    if request.method == "OPTIONS":
        response = jsonify({"status": "ok"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, X-API-KEY")
        response.headers.add("Access-Control-Allow-Methods", "GET")
        return response, 200
    # API key check
    api_key = request.headers.get("X-API-KEY")
    API_KEY = os.getenv("SERVER_SECRET")
    print(f"API_KEY: {API_KEY}")
    print(f"api_key: {api_key}")
    if api_key != API_KEY:
        print('abort')
        abort(401)

def get_oauth():
    global oauth
    global token_expires_in
    global token
    global token_expiry_timestamp

    if oauth is None or token is None or token_expiry_timestamp is None or time.time() >= token_expiry_timestamp:
        # Charger les variables d'environnement
        try:
            client_id = os.getenv("CLIENT_ID")
            client_secret = os.getenv("CLIENT_SECRET")
            token_url = os.getenv("AUTHORIZATION_ENDPOINT")
        except Exception as e:
            print(f"Error loading environment variables: {e}")
            return Response('{"error": "Environment variables not set"}', status=500, mimetype="application/json")
        if not client_id or not client_secret or not token_url:
            print("Missing environment variables")
            return Response('{"error": "Environment variables not set"}', status=500, mimetype="application/json")

        # Authentification OAuth2 (client_credentials grant)
        client = BackendApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)
        try:
            token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)
        except Exception as e:
            print(f"Error fetching token: {e}")
            return Response('{"error": "Failed to fetch token"}', status=500, mimetype="application/json")
        #token_expires_in = token['expires_in']
        #token_expiry_timestamp = time.time() + token["expires_in"]
        
        print(f"Token expires in: {token_expires_in} seconds")
    return oauth

@app.route('/search', methods=['GET'])
def search():
    #print('search')
    login = request.args.get('login')
    oauth = get_oauth()
    if isinstance(oauth, Response):
        return oauth
    user = get_user_by_login(oauth, login)
    time.sleep(1)
    if user['status_code'] != 200:
        return Response('{"error": "' + user['error'] + '"}', status=user['status_code'], mimetype="application/json")
    else:
        userid = user['userid']
        skills = get_skills(oauth, user_id=userid)
        projects = get_projects(oauth, user_id=userid)
        print(skills)
        return {
            "status_code": user['status_code'],
            "user": user['user'],
            "skills": skills,
            "projects": projects
        }
        


def interpret_status_code(status_code):
    messages = {
        400: "The request is malformed",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Page or resource is not found",
        422: "Unprocessable entity",
        500: "We have a problem with our server. Please try again later.",
        "Connection refused": "Most likely cause is not using HTTPS."
    }

    return messages.get(status_code, "Unknown error code")
def get_skills(oauth, user_id):
    response = oauth.get("https://api.intra.42.fr/v2/cursus_users", params={"filter[user_id]":user_id, "per_page": 100})
    #print(f"Response status code skill: {response.status_code}")
    #print(len(response.json()))
    data = response.json()
    skills = {}
    for i in range(len(data)):
        #print(data[i]["begin_at"])
        #print(data[i]["end_at"])
        #print(data[i]["cursus"]["name"])
        for skill in data[i]["skills"]:
            del skill["id"]
        skills[data[i]["cursus"]["name"]] = data[i]["skills"]
        #print("\n\n")
    return skills

def get_projects(oauth, user_id):
    response = oauth.get("https://api.intra.42.fr/v2/projects_users", params={"filter[user_id]":user_id, "per_page": 100})
    #print(f"Response status code project: {response.status_code}")
    projects = []
    for project in response.json():
        if project["status"] == "finished":
            projects.append(
                {"name": project['project']['name'],
                "final_mark": project['final_mark'],
                "status": project['status']
                })
    return projects

def get_user_by_login(oauth, login):
    response = oauth.get("https://api.intra.42.fr/v2/users", params={"filter[login]":login})
    if response.status_code != 200:
        return {
            "status_code": response.status_code,
            "error": interpret_status_code(response.status_code)
        }
    elif response.status_code == 200 and len(response.json()) > 0:
        json_response = response.json()[0] 
        user = {
            "login": json_response['login'],
            "email": json_response['email'],
            "first_name": json_response['first_name'],
            "last_name": json_response['last_name'],
            "image_url": json_response['image']['link'],
            "phone": json_response['phone'],
            "wallet": json_response['wallet'],
        }
        return {
            "status_code": response.status_code,
            "user": user,
            "userid": json_response['id']
        }
    else:
        print(response.json())
        print(f"login: {login}")
        return {
            "status_code": 201,
            "error": "User not found"
        }



def main():
    app.run(host='0.0.0.0', port=5000, debug=True)
    return

if __name__ == "__main__":
    main()
