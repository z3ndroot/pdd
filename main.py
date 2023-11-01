from models import Base


def main():
    Base.metadata.drop_all()
    Base.metadata.create_all()


if __name__ == '__main__':
    main()
