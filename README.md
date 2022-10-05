# Consumer-Review-Detection

Online shopping is all over the internet. All our needs are just a click away. The biggest online shopping website is Amazon. Amazon is known not only for its variety of products but also for its strong recommendation system.

Consumers increasingly rely on reviews for product information. However, the usefulness of online reviews is impeded by fake reviews that give an untruthful picture of product quality. Therefore, better detection of fake reviews is needed.

We creating a machine learning model that can predict whether an online review is fraudulent or not and giving potential buyers the confidence to buy the product based on consumer review.


## Technologies

This project utilizes a lot of different add ons, please make sure you have all these and they are up to date:

* [Google Colab](https://colab.research.google.com//) - For the notebook creation and running of the code.

* [pandas 1.4.3](https://github.com/pandas-dev/pandas/blob/main/README.md) - For reading the csv files and other operations.

* [scikit-learn](https://scikit-learn.org/stable/index.html) - Tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction

* [numpy](https://https://numpy.org/) - Loaded in, not used in the framework, but could be used in future editions.

* [Matplotlib 4.0](https://matplotlib.org/) - For plotting graphs and charts that appear below the code.

* [sqlalchemy v1.4.32](https://github.com/sqlalchemy/sqlalchemy) - For running SQL operations for the database.

* [Holoviews](https://holoviews.org/) - For streamlit data visulization

* [hvplot v0.8.0](https://github.com/holoviz/hvplot#readme) - For creating interactive and more detailed plots.

* [language-tool](https://pypi.org/project/language-tool-python/) - To detect grammar errors and spelling mistakes.

![image](https://user-images.githubusercontent.com/105394703/193184354-0d034e41-599d-41c9-9bfd-2cef182bfb09.png)


### Algorithms performed

* [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

* [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

* [Support Vector Machine](https://scikit-learn.org/stable/modules/svm.html)


### Convert json to CSV using following commands
```
url = "https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Home_Entertainment_v1_00.tsv.gz"
reviews_df = pd.read_csv("amazon_reviews_us_Home_Entertainment_v1_00.csv",sep="\\t",engine = "python",na_values=["\\N"])
```


# Contributors

- [Theena Dang](https://github.com/Th33na)
- [Drew Herrera](https://github.com/drew94591)
- [Agnes Maria](https://github.com/agnesmaria1)
- [Nayana Narayanan](https://github.com/nayananarayananp)
- [Matthew Stream](https://github.com/MC-Stream)
- [Hugo Velazquez](https://github.com/HugoWLA)

# License
[MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)
