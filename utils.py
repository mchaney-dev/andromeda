import numpy as np
import evaluate
import pickle

metric = evaluate.load('accuracy')

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

def pickle_dataset(dataset, path):
    pickle.dump(dataset, open(path, 'wb'))

def unpickle_dataset(path):
    return pickle.load(open(path, 'rb'))