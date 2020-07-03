from database import create_tables, view_cars, view_family, view_children, insert_car, insert_child, insert_parent


menu = """\n\nPlease select one of the following!
1) View your family parents.
2) Insert into family parent table.
3) View family car.
4) Insert into family car.
5) View children of parent.
6) Insert new child of parent.
7) Exit

Your Selection: """

welcome = "Welcome to your family tree!"

print(welcome)

create_tables()


def prompt_family_view():
    family = view_family()
    for _id, name, salary, location in family:
        print(f'{_id}, {name}, {salary}, {location}')


def prompt_car_view():
    cars = view_cars()
    for _id, model, parent_id in cars:
        print(f'{_id}, {model}, {parent_id}')


def prompt_children_view():
    children = view_children()
    for child in children:
        print(f'{child[1]}: {child[5]}, {child[6]}')


def prompt_insert_parent():
    name = input("Enter parent's name: ")
    salary = input("Enter parent salary: ")
    location = input("Enter parent location: ")
    insert_parent(name, salary, location)


def prompt_insert_car():
    model = input("Enter car  model: ")
    parent_id = int(input("Enter parent id: "))
    insert_car(model, parent_id)


def prompt_insert_child():
    child_name = input("Enter child name: ")
    age = input("Enter child's age: ")
    parent_id = int(input("Enter parent id: "))
    insert_child(child_name, age, parent_id)


while (selection := input(menu)) != "7":
    if selection == "1":
        prompt_family_view()
    elif selection == "2":
        prompt_insert_parent()
    elif selection == "3":
        prompt_car_view()
    elif selection == "4":
        prompt_insert_car()
    elif selection == "5":
        prompt_children_view()
    elif selection == "6":
        prompt_insert_child()
    else:
        print("This is not a valid option!")

print("Have a nice day!")
