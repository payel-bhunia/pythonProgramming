class Newclass:
    def __init__(self):
        print('instance created')
    def __del__(self):
        print('instance deleted')


def create_instance():
    obj = Newclass()
    print('created')


if __name__ == '__main__':
    create_instance()