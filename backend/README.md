# Not hotdog API

### Setup

##### Model

1. Package a trained model in in `hotdog.ipynb` in `../research` using `model.save("model")`

2. Copy the `model` folder to the root of this backend project. The `model` folder should have the following structure:

```
├── model
│   ├── assets
│   ├── variables
│   ├── keras_metadata.pb
│   ├── saved_model.pb
```

### Running

1. Run the Flask app with `gunicorn`

```
gunicorn -b :5000 -t 60 --chdir src --reload wsgi:app
```

2. Send a POST request with a `.jpg` file to the API to get predictions

```
curl -X POST -F image_file=@test.jpg http://localhost:5000
```

You should be getting a prediction 
