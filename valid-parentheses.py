
def isValid(s: str) -> bool:
    open_to_close = {
      '(' : ')',
      '{' : '}',
      '[' : ']'
    }
    open_set = set(['(', '{', '['])
    stack = []
    for charac in s:
      if charac in open_set: # if the character is an open bracket
        print(charac)
        stack.append(charac)
      else: # if its the closed bracket and stack is non-empty
        if len(stack) and open_to_close[stack[-1]] == charac:
          stack.pop()
        else:
          return False
    if len(stack): # once we exhaust all the characs in string, then check for length of the stack
      return False
    return True

# SOlution 2

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            match c:
                case '(' | '[' | '{':
                    stack.append(c)

                case ')' | ']' | '}':
                    if len(stack) is 0:
                        return False
                    
                    top = stack.pop()
  
                    if c is ')' and top is not '(':
                        return False
                    
                    elif c is ']' and top is not '[':
                        return False
                    
                    elif c is '}' and top is not '{':
                        return False

                case _:
                    return False
        
        if len(stack) is not 0:
            return False

        return True

a = isValid("()[]{}")
print(a)