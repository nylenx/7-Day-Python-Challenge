if __name__ == '__main__':
    file = None
    try:
        file = open('./Day 6/data.txt')
        print(file.read())
    except FileNotFoundError:
        print("Error: file not found")
    except PermissionError:
        print("ERROR: permission denied")
    except Exception as e:
        print(f'An Unexpected error occured: {e}')
    finally:
        if file:
            file.close()