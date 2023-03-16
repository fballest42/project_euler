""" TinyStatytician class

"""

import numpy as np
import sys
import math

class TinyStatistician:
  """ A class that include some statyticians methods """

  def __init__(self):
    pass
          
  def mean(x):
    """ Method of the class TinyStatytician that calculate
        the mean of a list or matrix """
    if x == None:
      return None
    try:
      mean = 0
      for i in x:
        mean += i
      return mean / len(x)
    except Exception as exc:
      print("Error: {}: {}", format(type(exc).__name__, exc))
      return None
	
  def median(x):
    """Method of the class TinyStatytician that calculate
       the median of a list or matrix """
    if x == None:
      return None
    return TinyStatistician.percentile(x, 50)

  def quartile(x):
    return [TinyStatistician.percentile(x, 25), TinyStatistician.percentile(x,75)]

  def percentile(x, per):
    if x == None:
      return None
    try:
      sorted_x = np.sort(x)
      ln = len(sorted_x)
      if ln == 0:
        return None
      return sorted_x[math.ceil((ln * per) / 100) - 1]
    except Exception as exc:
      print("Error: {}: {}", format(type(exc).__name__, exc))
      return None


#https://github.com/MCCiupek/bootcamp_ML/blob/52048509b0eae4cac41cfd3e2a51018699084f25/Module00/ex01/TinyStatistician.py
