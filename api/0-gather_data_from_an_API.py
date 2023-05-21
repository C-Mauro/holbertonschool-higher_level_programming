import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee information
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data["name"]

    # Fetch TODO list for the employee
    response = requests.get(todo_url)
    todo_data = response.json()

    # Calculate TODO list progress
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task["completed"]]
    num_done_tasks = len(done_tasks)

    # Display progress information
    print(f"Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task['title']}")

# Usage example
employee_id = 1
get_employee_todo_progress(employee_id)

