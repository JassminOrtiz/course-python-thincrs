def hello_world():
    print("¡Hello world!")


def hello_world_name(first_name):
    print(f"Hola!, {first_name}!")


def hello_world_args(*args):
    first_name = args[0]
    second_name = args[1]
    third_name = args[2]

    print(f"Hola, {first_name} / {second_name} / {third_name} !")

def hello_world_keyword_args(first_person, second_person):
    print(f"Hola, {first_person} / {second_person}")


def hello_world_arbitrary_keyword_args(**kwargs):
    if kwargs.get('second_person') is None:
        print("No existe segunda persona")
    else:
        print(f"Hola, {kwargs['first_person']} / {kwargs['second_person']}!")


# hello_world()
# hello_world_name("Jassmin Alondra")
# hello_world_name("Brayton")
# hello_world_args("Alfonso", "Julieta", "Jorge")
# hello_world_keyword_args(first_person="Ofelia", second_person="Brenda")
hello_world_arbitrary_keyword_args(first_person="Ofelia", second_person="Brenda")
hello_world_arbitrary_keyword_args(first_person="Brayton")