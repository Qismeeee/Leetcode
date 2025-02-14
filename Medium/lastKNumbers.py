class ProductOfNumbers(object):

    def __init__(self):
        self.prefixProduct = [1]  # Start with 1 to avoid empty product cases
        self.reset = False  # Flag to track if we need to reset the array due to 0s

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefixProduct = [1]
        else:
            self.prefixProduct.append(self.prefixProduct[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.prefixProduct):
            return 0
        else:
            return self.prefixProduct[-1] // self.prefixProduct[-k-1]


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(3)      
productOfNumbers.add(0)       
productOfNumbers.add(2)      
productOfNumbers.add(5)        
productOfNumbers.add(4)       
print(productOfNumbers.getProduct(2))  
print(productOfNumbers.getProduct(3)) 
print(productOfNumbers.getProduct(4))  
print(productOfNumbers.getProduct(2))
