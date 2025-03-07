import requests

ENDPOINT = "https://todo.pixegami.io/"

def test_create_task():
    payload = create_payload()
    #create task
    create_task_response = create_task(payload)
    create_task_data = create_task_response.json()
    assert create_task_response.status_code == 200

    #get task id
    task_id = create_task_data['task']['task_id']
    get_task_id_response = get_task(task_id)
    get_task_id_data = get_task_id_response.json()
    assert get_task_id_data["content"] == payload["content"]
    assert get_task_id_data["user_id"] == payload["user_id"]

    #ltest list tasks api
    data_user_id = create_task_data['task']['user_id']
    get_list_tasks_response = requests.get(ENDPOINT + f"/list-tasks/{data_user_id}")
    get_list_data = get_list_tasks_response.json()
    assert get_list_tasks_response.status_code == 200


def test_update_task():
    #create a new task
    payload = create_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()['task']['task_id']

    #update the task data
    updated_payload = {
    "user_id": payload["user_id"],
    "task_id": task_id,
    "content": "my updated content",
    "is_done": True
    }

    #request to update task data 
    update_task_response = requests.put(ENDPOINT + "/update-task", json=updated_payload)
    update_task_data = update_task_response.json()
    assert update_task_response.status_code == 200

    #get the updated task
    get_update_response = requests.get(ENDPOINT + f"/get-task/{task_id}")
    get_update_data = get_update_response.json()
    assert get_update_response.status_code == 200
    assert get_update_data["task_id"] == updated_payload ["task_id"] == task_id #unique key created from server side does not change
    assert get_update_data["is_done"] == True #change verified
    assert get_update_data["content"] == updated_payload["content"] #content stays the same

def test_delete_task_ID():

  payload_new= create_payload() #create a task
  get_response_data = create_task(payload_new).json()

  #extract task id
  task_id = get_response_data['task']['task_id']

  #delete task
  delete_task_response = requests.delete(ENDPOINT + f"/delete-task/{task_id}", json=payload_new)
  delete_task_response.status_code == 200
  get_del_task_id = get_task(task_id) #get task
  assert get_del_task_id.status_code == 404 #should not be successful

#helper functions
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def create_payload():
  return {
  "user_id": "test_user",
  "task_id": "test_task_id",
  "content": "test_user_content",
  "is_done": False
}