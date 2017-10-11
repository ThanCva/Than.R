###We are just trying to create a tree model to identify the gendre by using the height, weight  and shoe size.
### this codes and idea was inspired by Siraj Raval


from sklearn import tree

X= [180,80,11] , [170,70,12], [145,23,9], [136,60,10],[190,50,12],[160,50,8],[165,70,7],[180,70,12],[200,110,15],[190,100,13],[150,50,6]

y=['male','male','female','female','male','male','female','female','male','male','female'
]

clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,y)

prediction= clf.predict([[140,70,8]])

print prediction

### you can run this on your python   