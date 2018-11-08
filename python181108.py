
# coding: utf-8

# # Introdução ao Python 
# ##### Teoria da Computação Quântica 

# In[4]:


a = 10
print(a)
a = 'Kleber'
print(a)


# In[5]:


(2*3)%5


# In[6]:


3**3


# In[7]:


27**(1/3)


# In[9]:


abs(-1)*max(1,2,3,4,5)+min(1,2,3,4,5)+round(2.678)


# In[10]:


8//3


# In[11]:


get_ipython().run_line_magic('pinfo', 'pylab')


# In[12]:


get_ipython().run_line_magic('pylab', 'inline')


# In[13]:


pi


# In[14]:


cos(2*pi)


# In[16]:


sin(pi/6)


# In[17]:


log(e**5)


# In[18]:


log2(1024)-log10(1000)


# # Vetores e Matrizes

# In[19]:


array([1,2,3,4,5])


# In[20]:


arange(1,6)


# In[22]:


arange(0,21,2)


# In[23]:


arange(10)


# In[25]:


reshape(arange(25), (5,5))


# In[26]:


d = reshape(arange(25), (5,5))
det(d)


# In[29]:


m = array([[2, 5],[7, 3]])
det(m)


# In[30]:


m = array([[4, 1],[8, 3]])
det(m)


# In[33]:


zeros((2,2))


# In[31]:


ones((2,3))


# In[32]:


eye(3)


# In[34]:


rand(2,2)


# In[35]:


rand(2)


# In[37]:


a = eye(2)
b = array([[2,3],[4,5]])
dot(a,b)


# In[38]:


a = ones((2,2))
b = array([[2,3],[4,5]])
dot(a,b)


# In[39]:


transpose(b)


# In[40]:


inv(b)


# In[41]:


solve(b, inv(b))


# # Números Complexos

# In[43]:


a = 2+3j
print(a)


# In[48]:


complex(2,3)


# In[46]:


real(a)


# In[47]:


imag(a)


# In[49]:


abs(a)


# # Derivadas, Integral e Limite

# In[53]:


from sympy import *

x = symbols('x')
diff(x**2+x+5, x)


# In[54]:


pprint(x**2+x+5)


# In[55]:


integrate(1/(1+x**2), x)


# In[56]:


pprint(1/(1+x**2))


# In[58]:


limit(atan(x),x,oo)


# In[60]:


plot(sin(x), (x, -5, 5))


# In[64]:


from sympy.plotting import plot3d
y = symbols('y')

plot3d(y**2*sin(x), (x,0,2*pi), (y,0,20))

