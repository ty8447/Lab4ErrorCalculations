#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Lab 4 Error Calculations
#by Cole Rabe



#Setup the data variables


massCart = (499.5/1000) #Convert the mass from grams to kilograms
massCartUncertainty = (0.1/1000) #Convert the uncertainty from grams to kilograms

#Put the data from the slow run from logger pro into variables
slowVelInitial = 0.8341 #Units: m/s
slowVelFinal = -0.7877 #Units: m/s
slowVelStDevInitial = 0.02306 #Units: m/s
slowVelStDevFinal = 0.01518 #Units: m/s

#Put the data from the slower run from logger pro into variables
slowerVelInitial = 0.5976 #Units: m/s
slowerVelFinal = -0.5542 #Units: m/s
slowerVelStDevInitial = 0.02277 #Units: m/s
slowerVelStDevFinal = 0.01274 #Units: m/s

#Put the data from the slowest run from logger pro into variables
slowestVelInitial = 0.2940 #Units: m/s
slowestVelFinal = -0.2381 #Units: m/s
slowestVelStDevInitial = 0.02615 #Units: m/s
slowestVelStDevFinal = 0.01008 #Units: m/s

print ("Success")
print ("Data Variables Set!")
print ("massCart ",massCart,"kg")
print ("massCartUncertainty ",massCartUncertainty,"kg")


# In[29]:


#Calculations for the slow run

slowMomentumInitial = (massCart*slowVelInitial) #Calculate initial slow momentum
slowMomentumFinal = (massCart*slowVelFinal) #Calculate final slow momentum
slowUncertaintyInitial = (((massCartUncertainty/massCart)+(slowVelStDevInitial/slowVelInitial))*(slowMomentumInitial)) #Calculate initial slow uncertainty
slowUncertaintyFinal = (((massCartUncertainty/massCart)+(slowVelStDevFinal/slowVelFinal))*(slowMomentumFinal)) #Calculate final slow uncertainty
slowMomentum = (slowMomentumFinal - slowMomentumInitial) #Calculate the total slow momentum
slowUncertainty = (slowUncertaintyInitial + slowUncertaintyFinal) #Calculate the total slow uncertainty

#Print Output
print ("Success")
print ("Momentum for the slow collision: ",slowMomentum,"kg*m/s") #Print Slow Momentum
print ("Uncertainty for the slow collision: ± ",slowUncertainty,"kg*m/s") #Print Slow Uncertainty


# In[30]:


#Calculations for the slower run#Calculations for the slow run

slowerMomentumInitial = (massCart*slowerVelInitial) #Calculate initial slower momentum
slowerMomentumFinal = (massCart*slowerVelFinal) #Calculate final slower momentum
slowerUncertaintyInitial = (((massCartUncertainty/massCart)+(slowerVelStDevInitial/slowerVelInitial))*(slowerMomentumInitial)) #Calculate initial slower uncertainty
slowerUncertaintyFinal = (((massCartUncertainty/massCart)+(slowerVelStDevFinal/slowerVelFinal))*(slowerMomentumFinal)) #Calculate final slower uncertainty
slowerMomentum = (slowerMomentumFinal - slowerMomentumInitial) #Calculate the total slower momentum
slowerUncertainty = (slowerUncertaintyInitial + slowerUncertaintyFinal) #Calculate the total slower uncertainty

#Print Output
print ("Success")
print ("Momentum for the slower collision: ",slowerMomentum,"kg*m/s") #Print Slower Momentum
print ("Uncertainty for the slower collision: ± ",slowerUncertainty,"kg*m/s") #Print Slower Uncertainty


# In[31]:


#Calculations for the slowest #Calculations for the slow run

slowestMomentumInitial = (massCart*slowestVelInitial) #Calculate initial slowest momentum
slowestMomentumFinal = (massCart*slowestVelFinal) #Calculate final slowest momentum
slowestUncertaintyInitial = (((massCartUncertainty/massCart)+(slowestVelStDevInitial/slowestVelInitial))*(slowestMomentumInitial)) #Calculate initial slowest uncertainty
slowestUncertaintyFinal = (((massCartUncertainty/massCart)+(slowestVelStDevFinal/slowestVelFinal))*(slowestMomentumFinal)) #Calculate final slowest uncertainty
slowestMomentum = (slowestMomentumFinal - slowestMomentumInitial) #Calculate the total slowest momentum
slowestUncertainty = (slowestUncertaintyInitial + slowestUncertaintyFinal) #Calculate the total slowest uncertainty

#Print Output
print ("Success")
print ("Momentum for the slowest collision: ",slowestMomentum,"kg*m/s") #Print Slowest Momentum
print ("Uncertainty for the slowest collision: ± ",slowestUncertainty,"kg*m/s") #Print Slowest Uncertaintyrun

