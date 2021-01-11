# Song Prediction

## YearPredictionMSD Data Set 
## Python for data analysis

* Ariel TEDGUI
* Valentin TASSEL


## Projet goal
The Million Song Dataset (MSD) is a freely-available collection of audio features and metadata for a million contemporary popular music tracks. 
The purpose being to predict the release year of a song from audio features.

Songs in the dataset are mostly western, commercial tracks ranging from 1922 to 2011, with a peak in the year 2000s.

Due to the large spectrum of possible values (89 years), we decide that it was better to predict the decade of the release year. We thus did a classification.

## Dataset description
There are 90 attributes :
* TimbreAverage[1-12]
* TimbreCovariance[1-78]
These features were extracted from the 'timbre' features from The Echo Nest API. The authors took the average and covariance over all 'segments' and each segment was described by a 12-dimensional timbre vector.

## Models 
To predict the release decade of a song from audio feature, we used 4 different supervised classification machine learning models, in order to establish a benchmark and compare the results.

* K-NN Classifier :  k-nearest neighbors algorithm is a non-parametric machine learning method [Learn More Here](https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/ "Learn More Here").

* Random Forest Classifier : Random forests is a supervised learning algorithm. It can be used both for classification and regression. It is also the most flexible and easy to use algorithm. [Learn More Here](https://www.datacamp.com/community/tutorials/random-forests-classifier-python "Learn More Here").

* XG Boost Classifier : XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework [Learn More Here](https://xgboost.readthedocs.io/en/latest/ "Learn More Here").

* Neural Network : Neural networks are a series of algorithms that mimic the operations of a human brain to recognize relationships between vast amounts of data. [Learn More Here](https://en.wikipedia.org/wiki/Artificial_neural_network "Learn More Here").

## Django API
We created a Django API to test our model.
In order to test the API, run the following commands :
```
1. cd DjangoAPIFolder
2. python -m pip install virtualenv
3. python -m virtualenv Env64
4. source Env64/bin/activate
5. pip install -r requirements.txt
6. python manage.py runserver
```
The server is running on port 8000.
To test the model, you need to make a POST request to /api/prediction with the data in the body of the request.


<br/>*You can take a look at our explanation slides in Slides.pdf and take a look at our notebook that serves for our model benchmarking and data exploration.*
