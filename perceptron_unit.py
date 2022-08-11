#Author: Nasim Faridnia



class perceptron_unit:
  def __init__(self,gate,alpha, w1,w2, total_iter = 100):
      self.gate = gate
      self.alpha = alpha
      self.w1 = w1
      self.w2 = w2
      self.error = None
      self.total_iter = total_iter
      self.data_list = {"and": [[1,1,1] , [1,0,0], (0,1,0), (0,0,0)],
                        "or": [[1,1,1] , [1,0,1], [0,1,1], [0,0,0]],
                        "nand": [[1,1,0] , [1,0,1], [0,1,1], [0,0,1]],
                        "nor": [[1,1,0] , [1,0,0], [0,1,0], [0,0,1]]
                        }


  def learningAlgorithm(self):
    """ Find optimal weights"""
    #choose the inputs and targets of the matching gate
    data = self.data_list[self.gate]
    self.error = 0

    for i in range(self.total_iter):
      print("\n epoch = ", i+1)
      list_error = [] #list errors in each epoch
      
      for datapoint in data:
        print("data point=",datapoint)
        x1 = datapoint[0]
        x2 = datapoint[1]
        target = datapoint[2]

        #calculate input vector
        y_in = self.w1 * x1 + self.w2 * x2 


        #calculate activation function which is a step function
        if y_in > 0:
          output = 1
        else:
          output = 0

        #check error
        if output !=target:
          self.error = 1
          #update weights
          self.w1 = self.w1 + self.alpha * target * x1
          self.w2 = self.w2 + self.alpha * target * x2

        else:
          self.error = 0

        #add datapoint error to list of epoch errors
        list_error.append(self.error)
        print("error list=", list_error)####
        print("x1 = {0} \t\t x2 = {1}\t\t target = {2}\t\t output = {3}\t\ty_in={4}\t w1= {5}\t\t w2 = {6}\t\t error = {7}".format(
          x1 , x2, target,output,y_in, self.w1 ,self.w2, self.error))
        print("\n")

      #if no errors in one epoch then stop algorithm
      if 1 not in list_error:
        print("no error in epoch")
        break

      print("\n --------------------------------------------------------------------------")

    

    


  def result (self):
    """show results"""

    print("w1 = {0}, w2 = {1}".format(self.w1, self.w2))


  


        

