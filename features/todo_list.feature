# todo_list.feature

Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries |
      | Pay bills   |
    When the user lists all tasks
    Then the output should contain:
      | Buy groceries |
      | Pay bills   |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries |
      | Pay bills   |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Edit a task in the to-do list
    Given the to-do list contains tasks:
      | Task          | Status  | Description         |
      | Buy groceries | Pending | Need to buy fruits |
      | Pay bills     | Pending | Due by end of month|
    When the user edits task "Buy groceries" to "Buy groceries and vegetables"
    Then the to-do list should reflect the updated task name and description

  Scenario: Filter tasks by status in the to-do list
    Given the to-do list contains tasks:
      | Task          | Status  | Description         |
      | Buy groceries | Pending | Need to buy fruits |
      | Pay bills     | Done    | Paid online         |
    When the user filters tasks by status "Pending"
    Then the output should contain:
      | Buy groceries |
      | Need to buy fruits   |
