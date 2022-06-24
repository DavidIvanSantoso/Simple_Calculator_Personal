from urllib import response

from django.http import HttpResponse
from services.tasks import is_palindrome_celery, prime_celery


def prime(request,index):
    result=prime_celery(index)
    response='<html><p>Prime Index %s. </p></html>' %result
    return HttpResponse(response)

def primepalindrome(request,index):
    result=is_palindrome_celery(index)
    response='<html><p>Prime Palindrome %s. </p></html>' %result
    return HttpResponse(response)