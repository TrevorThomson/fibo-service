
'''
Run the Fibo service locally
Usage:
    python fibo
'''

from fibo.service import create_service

if __name__ == '__main__':
    service = create_service()
    service.run()
