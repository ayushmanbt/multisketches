# Implementation of TenSketch

This is a recreation of TenSketch taken from the paper [Multisketches](https://dl.acm.org/doi/pdf/10.1145/3319535.3363208)


### How to run this code

To get started you need a virtual environment. To create virtual environment just run -

**Windows**
```
python -m venv <path to env> 
```

**Linux**
```
python3 -m venv <path to env> 
```

And after that start the environment -

**Windows**
```
<path to env>\Scripts\activate 
```

**Linux**
```
source <path to env>/bin/activate
```

Next install all the required packages using - 

```
pip install -r requirements.txt
```

or

```
pip3 install -r requirements.txt
```

You will also need the NBIS Software from [here](https://www.nist.gov/itl/iad/image-group/products-and-services/image-group-open-source-server-nigos)

There is a fix we need to initiate for GCC 10 and above which is explained in this [pull request](https://github.com/lessandro/nbis/pull/1/commits)


The fingerprints required for this project are pulled from [this dataset](https://doi.org/10.48550/arXiv.1807.10609)

The mindtc command which converts jpg to xyt but we have BMP... so we need to convert it using mogrify

```
mogrify -format jpg *.BMP -depth 8 -strip -extent 512x480
```

To use mogrify install imagemagic.