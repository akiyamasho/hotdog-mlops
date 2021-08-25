# "Research" repository for hotdog/not-hotdog classifier

"Hotdog or not hotdog, that is the question."
- Prince Hamlet

### Setup

##### Dataset Preparation

1. Download the dataset from the [Not Hot Dog Kaggle Dataset](https://www.kaggle.com/dansbecker/hot-dog-not-hot-dog)

2. Extract the dataset into `data/`. The dataset folder should look like this:

├── data
│   ├── test
│   │   ├── hot_dog
│   │   ├── not_hot_dog
│   └── train
│   │   ├── hot_dog
│   │   ├── not_hot_dog

##### Running

1. Create and source a `python3` `virtualenv`. This repository was tested on `python` 3.8.9.

```
python3 -m venv env
source env/bin/activate
```

NOTE: You can use `conda` as you wish as well.

2. Install the requirements

```
pip install -r requirements.txt
```

3. You can now run the notebook

### References

- [Kyaw Saw Htoon's Overcoming The Hot Dog Dilemma](https://medium.com/@kyawsawhtoon/overcoming-the-hot-dog-dilemma-40b515fcf155)
