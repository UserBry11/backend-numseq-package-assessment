def primes(num_limit):
    prime_list = []
    not_prime_list = []
    for num in range(num_limit):
        if num > 1:
            for x in range(2, num):
                if num % x == 0:
                    not_prime_list.append(num)
                    break

            else:

                prime_list.append(num)

    return prime_list


def is_prime(m):
    answer = False
    if m > 1:
        for x in range(2, m):
            if m % x == 0:
                break
        else:
            answer = True

        return answer
