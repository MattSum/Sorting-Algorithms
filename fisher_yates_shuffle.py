"""
Implementation of Fisher Yates shuffle algorithm also known as Knuth shuffle

"""
import random


def fisher_yates_shuffle(A: list) -> None:
      for i in range(len(A)-1, 0, -1):
            j = random.randint(0, i)
            A[j], A[i] = A[i], A[j]


if __name__ == '__main__':
      A = list(range(40))
      fisher_yates_shuffle(A)
      print(A)
