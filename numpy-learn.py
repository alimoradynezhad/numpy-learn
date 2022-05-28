#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
a =np.array((1,2,3,4,5))
a


# In[4]:


a


# In[5]:


a.shape


# In[6]:


a.ndim


# In[7]:


a.size


# In[9]:


b = np.array([1,2,3,4,5,6,7,8,9])
b


# In[10]:


b.sum()


# In[26]:


a.dtype


# In[13]:


a.dtype


# In[15]:


a.astype(np.float64)


# In[19]:


c= a.sum()
d =b.sum()
e =c+d
e


# In[20]:


lst = [[0,1,2,3,4], [5,6,7,8,9]]
lst


# In[22]:


y = np.array(lst)
y


# In[23]:


y.dtype


# In[24]:


y.shape


# In[27]:


y.ndim


# In[28]:


y.size


# In[29]:


x = y+a
x


# In[30]:


a


# In[40]:


f =np.array([1,2,3,4,5])
f


# In[41]:


t = y +f
t


# In[42]:


y.shape


# In[43]:


y.dtype


# In[44]:


y.astype(np.float32)


# In[45]:


y


# In[46]:


y[0]


# In[47]:


y[1]


# In[51]:


p= y[1]+ y[0]
p


# In[52]:


p[2:]


# In[53]:


y[-1:]


# In[54]:


y[4:]


# In[55]:


p[4:]


# In[56]:


p[::2]


# In[57]:


st = np.array(['ali', 'reza', 'mohamad'])
st


# In[58]:


import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)


# In[59]:


arr1 = np.array([1,2,3,4,5,6])
arr2 = arr1.copy()
arr1[0] = 7


# In[60]:


arr1


# In[61]:


arr2


# In[62]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


# In[63]:


arr2.shape


# In[65]:


arr2.reshape(3, 2)


# In[66]:


arr2.reshape(2,3)


# In[67]:


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)


# In[70]:


arr4 = np.array([1,2,3])
arr5 = np.array([4,5,6])
resultvstack = np.vstack((arr4, arr5))
resultvstack


# In[71]:


import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)


# In[72]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)


# In[73]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)


# In[74]:


import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))


# In[75]:


arr =np.array([5,8,7,6,2,10,0,45,78,2,4,1,2])
arr2 =np.sort(arr)
arr2


# In[76]:


import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))


# In[77]:


import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))


# In[ ]:




