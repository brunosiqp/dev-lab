# Simple Python client to consume the Java "API"
# For demo purposes, we just simulate consuming the Java backend

tasks = ["Learn Java", "Build frontend", "Test Python client"]

def list_tasks():
    print("Tasks from backend API:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task removed: {task}")
    else:
        print(f"Task not found: {task}")

if __name__ == "__main__":
    list_tasks()
    add_task("Run Python tests")
    list_tasks()
    remove_task("Build frontend")
    list_tasks()
