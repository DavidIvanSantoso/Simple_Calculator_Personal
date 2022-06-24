from celery import shared_task


@shared_task
def is_prime(n):
    if n>1:
        for i in range (2,int(n/2)+1):
            if(n%i)==0:
                return False
        else:
            return True
    else:
        return False

@shared_task
def prime_celery(index):
    cnt=0
    num=0
    while(index!=cnt):
        num+=1
        if is_prime(num):
            cnt+=1
    return num
    
@shared_task
def is_palindrome_celery(index):
    count = 0
    num = 0
    while count != index:
        num += 1
        if is_prime(num):
            if str(num) == str(num)[::-1]:
                count += 1
    return num