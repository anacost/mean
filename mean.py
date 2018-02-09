def mean(num_list):
  try:
        mean = sum(num_list)/float(len(num_list))
        if isinstance(mean, complex):
            return NotImplemented
        return mean
  except ZeroDivisionError as detail:
        msg="\nCannot compute the mean value of an empty list"
        raise ZeroDivisionError(detail.__str__() + "\n" +  msg)
  except TypeError as detail :
        msg = "The algebraic mean of an non-numerical list is undefined.\
               Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)
