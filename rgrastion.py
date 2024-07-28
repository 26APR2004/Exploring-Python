
import numpy as np
import matplotlib.pyplot as plt #  to plot graph

# Coefficients bo and b1
def coef(x,y):
   n= np.size(x)
   # mean of x and y
   m_x=np.mean(x)
   m_y=np.mean(y)

   # formula exection is start
   upper=np.sum(x*y)-n*m_x*m_y
   lower=np.sum(x*x)-n*m_x*m_x

   b1=upper/lower
   b0=m_y-b1*m_x
   return b0,b1

# to predict new data
def newdata(x,b1,b0):
    y=b0 + b1*x
    return y

# To draw regrestion line
def regrasation_line(x,y,b0,b1):
    plt.scatter(x, y, color = "r",marker = "o", s = 30)
    y_pred = b0 + b1*x
    plt.plot(x, y_pred, color = "b")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()



def main():
   # declaring data
    x=np.array([1,2,3,4,5])
    y=np.array([1.2,1.8,2.6,3.2,3.8])
    
    # call of coef() function
    b0,b1=coef(x,y)
    print("coefeciant b0={} and b1={}".format(b0,b1))
    # call newdata() function to predict on new data
    new_x=float(input("enter the x value"))
    new_y=newdata(new_x,b1,b0)
    print("for week {} is value of y is:{}".format(new_x,new_y))
    # call of  regrasation_line() function
    regrasation_line(x, y, b0, b1)

if __name__ == "__main__":
    main()