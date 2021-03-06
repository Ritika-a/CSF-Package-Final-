# svhndata package
Building the *svhndata* package to get [The Street View House Numbers (SVHN) Dataset](http://ufldl.stanford.edu/housenumbers/) ready for machine learning modeling for different frameworks.

![alt text][svhn-image]

[svhn-image]:http://ufldl.stanford.edu/housenumbers/32x32eg.png "image from Stanford webpage"

### Features
The *svhndata* package will:

- download the SVHN Matlab files from the Stanford University website.
- load the Matlab files
- set the training and testing.
  - return x_train, y_train, x_test, y_test.
  - it has an option to add extra data.
  - option to get labels one hot encoded
- rescale image pixes to 0-1
- change dimensions of data for _tensorflow_ , _pytorch_ , and _keras_ .


### Libraries Needed
We used python 3.5. Therefore any future version should work.
We used a couple of libraries to create this package. 
Some already come automatically installed in python3. 

The following libraries should be install in your machine:

__Numpy__
```
pip install numpy
```
```
conda install -c anaconda numpy
```
__wget__
```
pip install wget
```
__install everything__
```
pip install -r requirements.txt
```

### Installation
Type the following commands in your terminal.
```
git clone https://github.com/CeL124/CSF-Package-Final-.git

cd CSF-Package-Final-

python3 setup.py install 
```


### Sample code
```python
from svhndata.SvhnLoader import SvhnData
from svhndata.SvhnFormatter import change_range, change_dim

sv = SvhnData()
sv.load_data()

xtrain, ytrain, xtest, ytest = sv.get_data(onehot=True)

xtrain = change_dim(xtrain, framework='tensorflow')
xtest = change_dim(xtest, framework='tensorflow')

xtrain, ytrain = change_range(30000, xtrain, ytrain)
```
#### output
```
checking if directory exists...
directory data-Svhn already exists!

Checking if data files exist...
File train_32x32.mat already exists!
File test_32x32.mat already exists!
File extra_32x32.mat already exists!
****************************************

Loading the data. Please wait...

Image dimensions ready for tensorflow: (73257, 32, 32, 3)
--------------------------------------------------
Image dimensions ready for tensorflow: (26032, 32, 32, 3)
--------------------------------------------------

Data range has been changed. New shape below
----------------------------------------
New shape for images (30000, 32, 32, 3)
----------------------------------------
New shape for labels (30000, 10)
****************************************
```
