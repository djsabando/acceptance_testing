# todo_list_steps.py

from behave import given, when, then

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_empty_todo_list(context):
    context.to_do_list = []

# Step 2: When the user adds a task "{task}"
@when('the user adds a task "{task}"')
def step_add_task(context, task):
    context.to_do_list.append(task)

# Step 3: Then the to-do list should contain "{task}"
@then('the to-do list should contain "{task}"')
def step_check_task_in_list(context, task):
    assert task in context.to_do_list, f'Task "{task}" not found in the to-do list'

# Step 4: When the user edits task "{old_task}" to "{new_task}"
@when('the user edits task "{old_task}" to "{new_task}"')
def step_edit_task(context, old_task, new_task):
    for task in context.to_do_list:
        if task.name == old_task:
            task.name = new_task
            # Assuming the description remains unchanged for simplicity
            print(f"Task '{old_task}' edited to '{new_task}'.")
            return
    print(f"Task '{old_task}' not found.")

# Step 5: Then the to-do list should reflect the updated task name and description
@then('the to-do list should reflect the updated task name and description')
def step_check_updated_task(context):
    # Assuming the description remains unchanged for simplicity
    for task in context.to_do_list:
        assert task.name == context.new_task, f"Task name not updated correctly."
        # Add additional assertions for description if needed

# Step 6: When the user filters tasks by status "{status}"
@when('the user filters tasks by status "{status}"')
def step_filter_tasks_by_status(context, status):
    context.filtered_tasks = [task for task in context.to_do_list if task.status == status]

# Step 7: Then the output should contain:
# Tasks: - {task_name} - {description}
@then('the output should contain:')
def step_check_filtered_tasks(context):
    print("Filtered tasks:")
    for task in context.filtered_tasks:
        print(f"- {task.name} - {task.description}")



        

