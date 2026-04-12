import os

def main():
    token = os.getenv('TOKEN')
    if not token:
        raise ValueError('No TOKEN provided. Please set the TOKEN environment variable.')
    print(f'Using token: {token}')

if __name__ == '__main__':
    main()