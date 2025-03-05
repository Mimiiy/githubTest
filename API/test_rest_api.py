import requests

ENDPOINT = "https://todo.pixegami.io/"

def test_get_endpoint():
    response_endpoint = requests.get(ENDPOINT)
    original_endpoint_data = response_endpoint.json()
    assert response_endpoint.status_code == 200


def test_task():
    payload = {
  "user_id": "test_user",
   #"task_id": "test_task_id", client side generated.
  "content": "test_user_content",
  "is_done": False
}
    #create task
    create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
    create_task_data = create_task_response.json()
    assert create_task_response.status_code == 200

    #get task id
    data_task_id = create_task_data['task']['task_id']
    get_task_id_response = requests.get(ENDPOINT + f"/get-task/{data_task_id}")
    get_task_id_data = get_task_id_response.json()
    assert get_task_id_data["content"] == payload["content"]
    assert get_task_id_data["user_id"] == payload["user_id"]


    #list tasks 
    data_user_id = create_task_data['task']['user_id']
    get_list_tasks_response = requests.get(ENDPOINT + f"/list-tasks/{data_user_id}")
    get_list_data = get_list_tasks_response.json()
    assert get_list_tasks_response.status_code == 200

    #update tasks
    updated_payload= {
    "user_id": payload["user_id"], 
    "task_id": data_task_id,
    "content": "test_user_content",
    "is_done": True,
    }

    updated_response = requests.put(ENDPOINT + "/update-task", json=updated_payload)
    updated_response = updated_response.json()
    assert updated_response.status_code == 200

    #get the updated task
    get_updated_response = requests.get(ENDPOINT + f"/get-task/{data_task_id}")
    formatted_get_updated_response = get_updated_response.json()
    assert get_updated_response.status_code == 200
    assert formatted_get_updated_response["task_id"] == get_task_id_data["task_id"] #unique key created from server side is still the same
    assert formatted_get_updated_response["is_done"] == True #change verified
    assert formatted_get_updated_response["content"] == payload["content"] == updated_payload["content"] #no chages to content

    