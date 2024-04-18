#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies a float by the given multiplier.
    '''
    def multiplier_function(x: float) -> float:
        return lambda x: x * multiplier
