class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      self.height = None
      self.left = None
      self.right = None
      # TODO complete Node initialization

    def calc_height(self): #Probably dont need so many lines. Don't care, it works splendidly!
      if self.right is not None and self.left is not None:
        self.height = 1 + max(self.left.height,self.right.height)
      elif self.right is not None:
        self.height = 1 + self.right.height
      elif self.left is not None:
        self.height = 1 + self.left.height
      else:
        self.height = 1
    
    def calc_balance(self):
      if self.right is not None and self.left is not None: #If two children are present
        if self.right.height > self.left.height:
          bal = self.right.height - self.left.height
        elif self.left.height > self.right.height:
          bal = -1 * (self.left.height-self.right.height)
        else:
          bal = 0
      elif self.left is not None: #Only one child is present, right child.
        bal = -1 * self.left.height
      elif self.right is not None: #Only one child is present, left child
        bal = self.right.height
      else: #No children are present
        bal = 0
      if bal >= 2 or bal <= -2:
        print('Tree out of balance!')
      return bal
    
  def __init__(self):
    self.__root = None
    # TODO complete initialization


  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    print('Inserting',value)
    self.__root = self.__recins(value,self.__root)
    

  def __recins(self,val,pos):
    if pos is None: #BASE CASE
      print('Node is None')
      pos = self.__BST_Node(val)
      print('created Node with val',val)
      pos.height = 1
      return pos
    #EVERYTHING DOWN IS RECURSIVE CASE
    if pos.value == val:
      print('Already in tree!')
      raise ValueError
    if pos.value > val:
      print('Less than',pos.value)
      pos.left = self.__recins(val,pos.left)
      pos.calc_height()
    elif pos.value < val:
      print('Greater than',pos.value)
      pos.right = self.__recins(val,pos.right)
      pos.calc_height()
    return self.balanced(pos)

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__recrem(value,self.__root)

  def __recrem(self,val,pos):
      if pos is None: #BASE 1
        print('Value not located in tree')
        raise ValueError
      if pos.value == val: #BASE 2
        print('Found value!')
        if pos.left is not None and pos.right is not None:
          r = self.__smallest(pos.right)
          pos.value = r.value
          pos.right = self.__recrem(r.value,pos.right)
          pos.calc_height()
          return self.balanced(pos)
        elif pos.left is None:
          pos = pos.right
        else:
          pos = pos.left
        return pos
      elif pos.value > val:
        pos.left = self.__recrem(val,pos.left)
        pos.calc_height()
      else:
        pos.right = self.__recrem(val,pos.right)
        pos.calc_height()
      return self.balanced(pos)

  def balanced(self,pos):
    bal = pos.calc_balance()
    if bal >= 2 or bal <= -2:
      print('Attempting to balance tree at node',str(pos.value)+'...')
      if (pos.right is not None) and (pos.calc_balance() == 2) and (pos.right.calc_balance() == -1): #RIGHT-LEFT KINK ( ͡° ͜ʖ ͡°)
          print('Kink right-left!')
          pos.right = self.__rotateright(pos.right)
          pos.right.calc_height()
          pos = self.balanced(pos)
      if (pos.left is not None) and (pos.calc_balance() == -2) and (pos.left.calc_balance() == 1): #LEFT-RIGHT KINK
          print('Kink left-right!')
          pos.left = self.__rotateleft(pos.left)
          pos.left.calc_height()
          pos = self.balanced(pos)
      if bal == 2 and (pos.right.calc_balance() > 0 or pos.right.calc_balance() == 0):
        print('Leaning right')
        print('Attempting rotation')
        pos = self.__rotateleft(pos)
        pos.right.calc_height()
        pos.left.calc_height()
        pos.calc_height()
        print('Finished rotation')     
      if bal == -2 and (pos.left.calc_balance() < 0 or pos.left.calc_balance() == 0):
        print('Leaning left')
        print('Attempting rotation')
        pos = self.__rotateright(pos)
        pos.right.calc_height()
        pos.left.calc_height()
        pos.calc_height()
        print('Finished rotation')
    return pos

  def __rotateright(self,pos):
    hold = pos
    floater = pos.left.right
    pos = pos.left
    pos.right = hold
    pos.right.left = floater
    return pos

  def __rotateleft(self,pos):
    hold = pos
    floater = pos.right.left
    pos = pos.right
    pos.left = hold
    pos.left.right = floater
    return pos
  
  def __smallest(self,pos):
    smallest = pos
    while pos.left is not None:
      pos = pos.left
    return pos
    
    
  #------------vTRAVERSALSv------------
  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    else:
      holder = []
      output = str(self.__rec_IOTraversal(self.__root,holder))
      output = output[:1]+' '+output[1:-1]+' '+output[len(output)-1:]
      output = output.replace("'","")
      output = output.replace('"',"")
      return output

  def __rec_IOTraversal(self,pos,holder):
      if pos is None:
        return
      self.__rec_IOTraversal(pos.left,holder)
      holder.append(pos.value)
      self.__rec_IOTraversal(pos.right,holder)
      return holder

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    else:
      holder = []
      output = str(self.__rec_PrOTraversal(self.__root,holder))
      output = output[:1]+' '+output[1:-1]+' '+output[len(output)-1:]
      output = output.replace("'","")
      output = output.replace('"',"")
      return output

  def __rec_PrOTraversal(self,pos,holder):
      if pos is None:
        return
      holder.append(pos.value)
      self.__rec_PrOTraversal(pos.left,holder)
      self.__rec_PrOTraversal(pos.right,holder)
      return holder

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    else:
      holder = []
      output = str(self.__rec_POTraversal(self.__root,holder))
      output = output[:1]+' '+output[1:-1]+' '+output[len(output)-1:]
      output = output.replace("'","")
      output = output.replace('"',"")
      return output

  def __rec_POTraversal(self,pos,holder):
        if pos is None:
          return
        self.__rec_POTraversal(pos.left,holder)
        self.__rec_POTraversal(pos.right,holder)
        holder.append(pos.value)
        return holder

  #------------^TRAVERSALS^------------
  
  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root is None:
      return 0
    return self.__root.height

  def to_list(self):
    holder = []
    #result = self.__rec_IOTraversal(self.__root,holder)
    #My IOTraversal method works literally the exact same way as the new __rec_list method.
    #To follow the specifications though, I wrote another method. But I left this here to show that I realize the below recursive call is kind of useless.
    result = self.__rec_list(self.__root,holder)
    return result

  def __rec_list(self,pos,holder):
    if pos is None:
      return
    self.__rec_list(pos.left,holder)
    holder.append(pos.value)
    self.__rec_list(pos.right,holder)
    return holder

  def __str__(self):
    return str(self.in_order())

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
