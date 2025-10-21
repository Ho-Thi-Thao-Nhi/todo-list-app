# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

# app.py

tasks = []

def add_task(name):
    tasks.append({"name": name, "completed": False})

if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
def list_tasks():
    print("Danh sách công việc:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task['name']}")
if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
    list_tasks()
