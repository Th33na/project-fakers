# Consumer-Review-Detection

Online shopping is all over the internet. All our needs are just a click away. The biggest online shopping website is Amazon. Amazon is known not only for its variety of products but also for its strong recommendation system.

Consumers increasingly rely on reviews for product information. However, the usefulness of online reviews is impeded by fake reviews that give an untruthful picture of product quality. Therefore, better detection of fake reviews is needed.

We are set on creating a machine learning model that can predict whether an online review is fraudulent or not and giving potential buyers the confidence to buy the product based on consumer review.


## Technologies

This project utilizes a lot of different add ons, please make sure you have all these and they are up to date:

* [Google Colab](https://colab.research.google.com//) - For the notebook creation and running of the code along with visualization.

* [pandas 1.4.3](https://github.com/pandas-dev/pandas/blob/main/README.md) - For reading the csv files and other operations.

* [scikit-learn](https://scikit-learn.org/stable/index.html) - Tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction

* [JSON](https://www.json.org/json-en.html) - Used for serializing structured data and exchanging it over a network, typically between a server and web applications.

* [Matplotlib 4.0](https://matplotlib.org/) - For plotting graphs and charts that appear below the code.

* [joblib](https://joblib.readthedocs.io/en/latest/#) - Tools to provide lightweight pipelining in Python.

* [Holoviews](https://holoviews.org/) - For Colab data visulization

* [hvplot v0.8.0](https://github.com/holoviz/hvplot#readme) - For creating interactive and more detailed plots.

* [Word Clouds](https://www.wordclouds.com/) - Visual representations of words that give greater prominence to words that appear more frequently.

![image](https://user-images.githubusercontent.com/105394703/193184354-0d034e41-599d-41c9-9bfd-2cef182bfb09.png)

![image](https://user-images.githubusercontent.com/105394703/194219443-706b99d6-7c75-4ff0-926a-a2c911993529.png)



### Algorithms performed

* [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

* [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

* [Support Vector Machine](https://scikit-learn.org/stable/modules/svm.html)


### Convert json to CSV using following commands
```
url = "https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Home_Entertainment_v1_00.tsv.gz"
reviews_df = pd.read_csv("amazon_reviews_us_Home_Entertainment_v1_00.csv",sep="\\t",engine = "python",na_values=["\\N"])
```
### Open Google Colab using following commands
```
https://colab.research.google.com/drive/1kYUoVm7P6hW7s0ii8jrFyliRJ3bZqd47?usp=sharing
```

### How to run it locally using following commands
```
pip install streamlit
```
on your local terminal clone our repo then 
```
streamlit run faker.py
```
or you can play with our [Fakers Application](https://th33na-project-fakers-faker-hgbyfc.streamlitapp.com/)

# Contributors

- [Theena Dang](https://github.com/Th33na)
- [Drew Herrera](https://github.com/drew94591)
- [Agnes Maria](https://github.com/agnesmaria1)
- [Nayana Narayanan](https://github.com/nayananarayananp)
- [Matthew Stream](https://github.com/MC-Stream)
- [Hugo Velazquez](https://github.com/HugoWLA)

# License
[MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)
