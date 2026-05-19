Program Listing for precision2e.py

import math

#       This program computes:  ln(sum)/ ln(product)     #
#       using two values chosen by person running          #
#       the program                                                              #
 
#       Input values for this execution                                #
a = 13
a = int(a)
b = 31
b = int(b)

ab = a * b

eps = 10
eps = int(eps)
eps = 1 / eps

i = 0

#       Python natural log values for inputs            #
acta = math.log(a)
actb = math.log(b)
actab = math.log(ab)

numer = acta + actb
denom = actab
ratio = numer / denom

print ("")
print ("=======================================================")

print ("               Run Parameters                ")

print ("=======================================================")
print ("")
print ("A =", a,            "ln A = ", math.log(a))
print ("B =", b,            "ln B = ", math.log(b))
print ("")
print ("ln B + Ln B = ", numer)
print ("ln(A*B) =     ", denom)

print ("Ratio is =    ", ratio)
print ("=======================================================")
print ("")

#         This loop controls precision level.                              #
#         First pass is for epsilon = 1/100                                  #
#         Future passes for 1/10 of previous precision level    #

for j in range(1, 10, 1):

   alog = 0
   blog = 0
   ablog = 0

   aterm = 0
   bterm = 0
   abterm = 0

   asw = 'n'
   bsw = 'n'        
   absw = 'n'

   eps = eps * 0.1

   print ("---------------------- ", "Test #", j,"------------------")
   print ("The value of epsilon is ", eps)
   print ("")

#           This loop determines when the ln series for each number #
#           first comes within epsilon of the Python ln value.                #

   for i in range(1, 600000, 1):
       pow = (2*i)-1
       coeff = 1 / pow
       term = coeff * ((a - 1)/(a + 1))** pow
       alog = alog + term
       term = coeff * ((b - 1)/ (b + 1)) ** pow
       blog = blog + term
       term = coeff * ((ab - 1) / (ab + 1)) ** pow
       ablog = ablog + term    

       alogs = 2 * alog
       blogs = 2 * blog
       ablogs = 2 * ablog

       lnnum = alogs + blogs
       lnden = ablogs
       ratio = lnnum / lnden        

       if abs(alogs - acta) <= eps and asw == 'n':
              print ("")
              print ("ln ", a, " less than epsilon at term ", i)
              print ("     Python value for ln(A) is: ", acta)
              print ("     Series value for ln(A) is: ", alogs)
              print ("")

              print ("     Numerator =   ", lnnum)
              print ("     Denominator = ", lnden)
              print ("     Ratio is =    ", ratio)

              absdiff = abs(lnnum - lnden)
              print ("     Abs Differ =  ", absdiff)
              aterm = i

              print ("")      
              asw = 'y'              

       if abs(blogs - actb) <= eps and bsw == 'n':
               print ("")
               print ("ln ", b, " less than epsilon at term ", i)
               print ("     Python value for ln(B) is: ", actb)
               print ("     Series value for ln(B) is: ", blogs)
               print ("")

               print ("     Numerator =   ", lnnum)
               print ("     Denominator = ", lnden)
               print ("     Ratio is =    ", ratio)

               absdiff = abs(lnnum - lnden)
               print ("     Abs Differ =  ", absdiff)

               bterm = i
               print ("")        
               bsw = 'y'                            

       if abs(ablogs - actab) <= eps and absw == 'n':
               print ("")
               print ("ln AB less than epsilon at term ", i)
               print ("     Python value for ln(AB) is: ", actab)

               print ("     Series value for ln(AB) is: ", ablogs)
               print ("")

               print ("     Numerator =   ", lnnum)
               print ("     Denominator = ", lnden)
               print ("     Ratio is =    ", ratio)

               absdiff = abs(lnnum - lnden)
               print ("     Abs Differ =  ", absdiff)

               abterm = i                
               print ("")
               absw = 'y'

             

       if i >= 1000000:
               break
               quit()        

           

       if asw == 'y' and bsw == 'y' and absw == 'y':
               print ("")
               numterms = aterm + bterm
               print ("Terms for ln ", a, " = ", aterm)
               print ("Terms for ln ", b, " = ", bterm)                
               print ("")

               print ("Sum terms for numerator =        ", numterms)
               print ("Terms for denominator =          ", abterm)
               ratio = abterm / numterms
               print ("Ratio of terms - Denom / sum Numer = ", ratio)

               maxterm = max(aterm,bterm)
               ratio = abterm / maxterm            
               print ("Ratio of terms - Denom / max Numer = ", ratio)
               print ("")

               print ("Program ending at term ", i)
               print ("")
               print ("")

               break
               quit()

 
