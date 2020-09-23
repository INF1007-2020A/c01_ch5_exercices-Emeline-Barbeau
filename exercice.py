#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

from typing import List


def convert_to_absolute() -> float:
    nbr = input("Entrez un nombre: ")
    return abs(float(nbr))


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    result = []

    for letter in prefixes :
        result.append(letter + suffixes)

    return result
#    return [letter + suffixe for letter in prefixes] only one line

# Code trouvé sur internet - comme demandé en cours
def prime_integer_summation() -> int:
    result = 2  #Start with 2 car est nbr premier mais n'entre pas dans while
    current_nbr = 2

    while current_nbr < 100 :   
        i = 2

        while (i < current_nbr) and (current_nbr % i) != 0 :
            i += 1
            if i == current_nbr :
                result += current_nbr

        current_nbr += 1

    return result


def factorial(number: int) -> int:
    i = 1
    result = 1

    while i <= number :
        result *= i
        i += 1

    return result
 #  return math.factorial(number)   


def use_continue() -> None:

    for i in range(1, 11, 1) :
        if(i == 5) : 
            continue
        else :
            print(i)


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
