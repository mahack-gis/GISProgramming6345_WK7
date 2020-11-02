#!/usr/bin/env python
# coding: utf-8

# In[4]:


def sed(ps, rs, f1, f2):   #takes pattern str, replacement str, 2 filenames
    try:
        fin = open(source, 'r')    #opens source file and reads
    except:
        print('Something went wrong with source.')
    try:
        fout = open(dest, 'w')     #opens destination file and writes to it
    except:
        print('Something went wrong with destination.')
    for line in fin:
        line = line.replace(ps, rs)
        fout.write(line)
    fin.close()
    fout.close()


# In[7]:


def main():
    ps = 'the'
    rs = 'tho'
    source = 'emma.txt'
    dest = source + '.replaced'
    sed(ps, rs, source, dest)


# In[8]:


if _name_ == '_main_':
    main()


# In[ ]:




