import randomimport sysclass SECRET: 	'''	Class that generates shares given required number of shares k,n, field and an ASCII symbol as secret	'''		def __init__(self,k,n,field,char):		self.k = k		self.n = n		self.field = field		self.char = char				def _c2b(self):      	  """      	  Char to binary.      	  Returns a representation of an ASCII char on 8 bits with leading 0      	  """      	  ret = bin(ord(self.char)) # convert char to binary      	  ret = ret[2:len(ret)] #remove leading '0b'      	  for i in xrange(len(ret), 8): #pad zeroes to make each representation 1 byte long      	      ret = "0" + ret      	  return ret      	  		  	def _create_poly(self): 		''' 		creates random polynomial of degree k-1 with coefficients [secret, a1, a2, ..., a_{k-1}] 		'''		intercept = ord(self.char) # convert secret to integer		self.coeff = [0]*self.k #create a list of size k with values initialized to 0		self.coeff[0] = intercept #set the first coefficient equal to intercept / secret				for i in xrange(1,self.k):			self.coeff[i]=random.randrange(1,self.field); # random choose coefficients a1, ..., a_{k-1}		return self.coeff 					def create_points(self):		'''		Calculates n points of a polynomial of degree k-1 with intercept being the provided ASCII character.		'''		self.points = {} #create a dictionary where points on the polynomial will be stored.  Keys are abscissas and values are ordinates.		self._create_poly() 		for i in xrange(self.n):			x = i+1			value = 0	 		for j in xrange(self.k):	 			value+=self.coeff[j]*pow(x,j)	 		self.points[x] = value % self.field	 		return self.points   	