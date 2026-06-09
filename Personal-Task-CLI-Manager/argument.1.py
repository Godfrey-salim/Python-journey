from join import list_task, delete_task, update_task, add_task,search_task
import argparse
def main():
    parser = argparse.ArgumentParser(description = "Personal Task CLI Manager")
    subparsers = parser.add_subparsers(dest="command")
    
    # list
    subparsers.add_parser("list", help="List incomplete tasks")
    subparsers.add_parser("list-all", help="List all tasks")

    # add
    p = subparsers.add_parser("add", help="Add a task")
    p.add_argument("description", help="Task description")

    # delete
    p= subparsers.add_parser("delete", help="delete a task")
    p.add_argument("id", type=int, help="task id")

    # complete
    p = subparsers.add_parser("complete", help="completed task")
    p.add_argument("id", type=int, help="completed task id")

    # search
    p = subparsers.add_parser("search", help="Task searched")
    p.add_argument("keyword", help="search keyword")

    # update
    p = subparsers.add_parser("update", help="update a task")
    p.add_argument("id", type=int, help="task id")
    p.add_argument("description", help="new descripton")

    menu = parser.parse_args()

    if menu.command == "add":
        add_task(menu.description)
    elif menu.command == "delete":
        delete_task(menu.id)
    elif menu.command == "search":
        search_task(menu.keyword)
    elif menu.command == "list":
        list_task()
    elif menu.command == "list-all":
        list_task(show_all=True)
    elif menu.command == "update":
        update_task(menu.id, menu.description)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()