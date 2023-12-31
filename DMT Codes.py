# -*- coding: utf-8 -*-
"""Master'sCodeForDMT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d0dm_7KPZK3mPPE4nLcv_HWFxaBVvcX2
"""

pip install mlxtend --upgrade

pip install mlextend

pip install squarify

pip install apyori

# Eclat

# Run the following command in the terminal to install the apyori package: pip install apyori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

transactions = []
for i in range(0, 7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

trans=np.array(transactions)

t=TransactionEncoder()
data=t.fit_transform(trans)
data=pd.DataFrame(data,columns=t.columns_,dtype=int)

# Training the Eclat model on the dataset
from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

# Visualising the results

## Displaying the first results coming directly from the output of the apriori function
results = list(rules)
# results

## Putting the results well organised into a Pandas DataFrame
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    return list(zip(lhs, rhs, supports))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support'])

    # l=[0.01,0.02,0.03,0.04,0.05]
## Displaying the results sorted by descending supports
resultsinDataFrame.nlargest(n = 10, columns = 'Support')

#Data manipulation libraries
import pandas as pd
import numpy as np

# Commented out IPython magic to ensure Python compatibility.
#Visualizations
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("dark")
import squarify
import matplotlib

#for market basket analysis (using apriori)
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#for preprocessing
from mlxtend.preprocessing import TransactionEncoder


#to print all the interactive output without resorting to print, not only the last result.
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
data = pd.read_csv('Market_Basket_Optimisation.csv',header=None)

#shape
data.shape
#head of data

data.head()


#tail of data

data.tail()

#converting into required format of TransactionEncoder()
trans=[]
for i in range(0,7501):
    trans.append([str(data.values[i,j]) for j in range(0,20)])

trans=np.array(trans)

print(trans.shape)

### Using TransactionEncoder

t=TransactionEncoder()
data=t.fit_transform(trans)
data=pd.DataFrame(data,columns=t.columns_,dtype=int)

data.shape
##here we also find nan as one of the columns so lets drop that column
#now lets check shape
data.shape

import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud

plt.rcParams['figure.figsize'] = (10, 10)
wordcloud = WordCloud(background_color = 'white', width = 1200,  height = 1200, max_words = 20).generate(str(dataset[0]))
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Most Popular Items bought first by the Customers',fontsize = 40)
plt.show()

# looking at the frequency of most popular items

plt.rcParams['figure.figsize'] = (18, 7)
sns.countplot(dataset[0])
plt.title('frequency of most popular items', fontsize = 30)
plt.xticks(rotation = 90 )
plt.show()

# applying apriori rules to our dataset

trans = list(trans)

color = plt.cm.rainbow(np.linspace(0, 1, 40))
dataset[0].value_counts().head(40).plot.bar(color = color, figsize=(13,5))
plt.title('frequency of most popular items', fontsize = 20)
plt.xticks(rotation = 90 )
plt.grid()
plt.show()

import networkx as nx
dataset['food'] = 'Food'
food = dataset.truncate(before = -1, after = 15)
food = nx.from_pandas_edgelist(food, source = 'food', target = 0, edge_attr = True)

import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.figsize'] = (13, 13)
pos = nx.spring_layout(food)
color = plt.cm.Set1(np.linspace(0, 15, 1))
nx.draw_networkx_nodes(food, pos, node_size = 15000, node_color = color)
nx.draw_networkx_edges(food, pos, width = 3, alpha = 0.6, edge_color = 'black')
nx.draw_networkx_labels(food, pos, font_size = 20, font_family = 'sans-serif')
plt.axis('off')
plt.grid()
plt.title('Top 15 First Choices', fontsize = 20)
plt.show()

# Getting the list of transactions from the dataset
transactions = []
for i in range(0, len(dataset)):
    transactions.append([str(dataset.values[i,j]) for j in range(0, len(dataset.columns))])

transactions[:1]

#lets verify whether nan is present in columns
'nan' in data.columns
#so its proved that nan is not in columns
data.head()
##Lets consider the top 20 items purchased freequently
r=data.sum(axis=0).sort_values(ascending=False)[:20]
#altering the figsize
plt.figure(figsize=(20,10))
s=sns.barplot(x=r.index,y=r.values)
s.set_xticklabels(s.get_xticklabels(), rotation=90)
# create a color palette, mapped to these values
my_values=r.values
cmap = matplotlib.cm.Blues
mini=min(my_values)
maxi=max(my_values)
norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in my_values]

#treemap of top 20 frequent items
plt.figure(figsize=(10,10))
squarify.plot(sizes=r.values, label=r.index, alpha=.7,color=colors)
plt.title("Tree map of top 20 items")
plt.axis('off')
#let us return items and ietmsets with atleast 5% support:
freq_items=apriori(data,min_support=0.05,use_colnames=True)
freq_items
#Now let's generate association rules

res=association_rules(freq_items,metric="lift",min_threshold=1.3)
res
frequent_itemsets = apriori(data, min_support = 0.05, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets

# getting th item sets with length = 2 and support more han 10%

frequent_itemsets[ (frequent_itemsets['length'] == 2) &
                   (frequent_itemsets['support'] >= 0.01) ]
# getting th item sets with length = 2 and support more han 10%

frequent_itemsets[ (frequent_itemsets['length'] == 1) &
                   (frequent_itemsets['support'] >= 0.01) ]
                   #Importing Libraries

from mlxtend.frequent_patterns import fpgrowth
#running the fpgrowth algorithm
res=fpgrowth(data,min_support=0.05,use_colnames=True)

res
res=association_rules(res,metric="lift",min_threshold=1)
res
import time
l=[0.01,0.02,0.03,0.04,0.05]
t=[]
for i in l:
    t1=time.time()
    apriori(data,min_support=i,use_colnames=True)
    t2=time.time()
    t.append((t2-t1)*1000)
l=[0.01,0.02,0.03,0.04,0.05]
f=[]
for i in l:
    t1=time.time()
    fpgrowth(data,min_support=i,use_colnames=True)
    t2=time.time()
    f.append((t2-t1)*1000)
l=[0.01,0.02,0.03,0.04,0.05]
z=[]
for i in l:
    t1=time.time()
    apriori(data,min_support=i,use_colnames=True)
    t2=time.time()
    z.append((t2-t1)*1000)
sns.lineplot(x=l,y=f,label="fpgrowth")
sns.lineplot(x=l,y=t,label="apriori")
sns.lineplot(x=l,y=z,label="Eclat")
plt.xlabel("Min_support Threshold")
plt.ylabel("Run Time in ms")

sns.lineplot(x=l,y=f,label="fpgrowth")
sns.lineplot(x=l,y=t,label="apriori")
sns.lineplot(x=l,y=z,label="Eclat")
plt.xlabel("Min_support Threshold")
plt.ylabel("Run Time in ms")