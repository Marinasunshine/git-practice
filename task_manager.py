import random

def create_task(title, description):
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    equation = f"{a}x + {b} = 0"
    task = {'title': title, 'description': description, 'equation': equation}
    
    print(f"Создана новая задача: {title}")
    
    return task
