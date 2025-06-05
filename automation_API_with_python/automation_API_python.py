import requests
import json
import random
import string

def main():


    url = "https://gorest.co.in/public/v2/users"
    auth = "Bearer 6e651006d36e494e4eac649b98f2efa2b1877e63f5a5da8562cfecc523499a33"
    header = {"Authorization" : auth}

   

   #TESTING POST REQUEST AND GET REQUEST BY USER ID
    user_id = post_request(url, header)
    user_id_get_request = get_request_by_user_id(url, header, user_id)
    assert user_id == user_id_get_request
   
   #TESTING GER REQUEST FOR ALL USERS
    get_request_all_users(url, header)

   #TESTING TO UPDATE THE USER
    put_request(url, header, user_id)

   #TESTING DELETE THE USER
    delete_request(url, header, user_id)
    
def random_email():
    random_email_string = ''.join(random.choices(string.ascii_letters + string.digits, k=9)) + "@test.com"
    return random_email_string 
        
#POST
def post_request(url, header):
    data = {
            "name": "Test Automation",
            "email": random_email(),
            "gender": "male",
            "status": "active"
        }
    response = requests.post(url, json=data, headers=header)
    json_data = response.json()
    
    assert response.status_code == 201
    
    print(f"The POST status code is {response.status_code}" )
    user_id = json_data["id"]
   
    return user_id


#GET ALL USERS
def get_request_all_users(url, header):
    response = requests.get(url, headers=header)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    
    assert response.status_code == 200

    print("The GET REQUEST FOR ALL USERS data body: ", json_str)

#GET USER BY ID
def get_request_by_user_id(url, header, user_id):
    call_url = url + f"/{user_id}"
    response = requests.get(call_url, headers=header)
    json_data = response.json()
    user_id_get_request = json_data["id"]

    assert response.status_code == 200
    
    return user_id_get_request

#PUT
def put_request(url, header, user_id):
    call_url = url + f"/{user_id}"
    data = {
            "name": "Test Automation",
            "email": random_email(),
            "gender": "male",
            "status": "inactive"
        }
    response = requests.put(call_url, json=data, headers=header)
    response_get = requests.get(call_url, headers=header)
    json_data = response_get.json()

    assert response.status_code == 200
    assert json_data["id"] == user_id
    assert json_data["name"] == "Test Automation"
    assert json_data["status"] == "inactive"

    print("The PUT status code: ", response.status_code)

def delete_request(url, header, user_id):
    call_url = url + f"/{user_id}"
    response = requests.delete(call_url, headers=header)
    
    assert response.status_code == 204
    
    print(f"The user with ID: {user_id} was deleted!")

if __name__ == "__main__":
    main()

