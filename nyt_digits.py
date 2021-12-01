# %%
# To play the new NYT game 'Digits'
import operator

def solve_puzzle(target, numbers):
  """ Solve NY Times "digits" puzzle. Target is the goal number,
  numbers is a list of available numbers to combine via basic 
  operations (add, subtract, multiply, divide).
  Returns a list of solutions. Each solution shows the series of 
  steps needed to achieve the answer. Solutions are guaranteed to work, 
  but may not be unique because different step orderings will show
  up as different solutions.
  """
  # Recurse until all combinations are found or until target is found
  history_list = [[]]
  numbers_list = [numbers]
  solutions = []
  while len(numbers_list[0]) > 1:
    new_nums_list = []
    new_hists_list = []
    for nums, hist in zip(numbers_list, history_list):
      # Find combinations
      new_nums, new_hists = all_options(nums, hist)
      for nnl, nhl in zip(new_nums, new_hists):
        if target in nnl:
          # Success! 
          # print('Success!!')
          # Print the history
          print("Solution: %s"%(str(nhl)))
          solutions.append(nhl)
      # Build derived lists
      new_nums_list.extend(new_nums)
      new_hists_list.extend(new_hists)
    numbers_list = new_nums_list
    history_list = new_hists_list
  num_solutions = len(solutions)
  if num_solutions==0:
    print('No solutions exist for this puzzle!')
  else: 
    print('*A total of %i solutions were found!*'%num_solutions)
  return solutions


def all_options(numbers, history=[]):
  """ Numbers is a list of numbers which are options for combining
  History is the history of operations which led to this list of numbers.
  (This is a single list of strings)
  """
  new_numbers_list = []
  new_history_list = []
  for num in numbers:
    # first choice is num
    numbers_copy = numbers.copy()
    numbers_copy.remove(num)
    other_numbers = numbers_copy
    for other_num in other_numbers:
      other_numbers_copy = other_numbers.copy()
      other_numbers_copy.remove(other_num)
      remaining_numbers = other_numbers_copy
      if num >= other_num:
        larger, smaller = num, other_num
      else:
        larger, smaller = other_num, num
      for op_fcn, op_str in zip([operator.add, operator.sub, operator.mul, operator.truediv],['+','-','*','/']):
        # calculation is now set
        try:
          result = op_fcn(larger, smaller) 
        except ZeroDivisionError:
          result = -1 # non-valid value, won't get stored
        # Only non-negative integer results are valid
        if result >= 0 and result == round(result):
          # Valid result
          new_numbers = [result] + remaining_numbers.copy() 
          new_history = history.copy() + ['%i%s%i=%i' % (larger,op_str,smaller,result)]
          new_numbers_list.append(new_numbers)
          new_history_list.append(new_history)
    return new_numbers_list, new_history_list


# Try it!
solve_puzzle(6, [1,2,3])
# %%
