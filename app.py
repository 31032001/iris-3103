import sklearn.datasets
import streamlit as st
st.title("Iris Classifier- API")

sl = st.slider('Sepal Length', 4.3, 7.9, 0.5)
sw = st.slider('Sepal Width', 2.0, 4.4, 0.5)
pl = st.slider('Petal Length', 1.0, 6.9, 0.5)
pw = st.slider('Petal Width', 0.1,2.5, 0.5)

from sklearn.datasets import load_iris

iris = load_iris()

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3)

model = kmeans.fit(iris.data)

result = model.predict([[sl,sw,pl,pw]])
result = iris.target_names[result[0]]
st.title(result)


