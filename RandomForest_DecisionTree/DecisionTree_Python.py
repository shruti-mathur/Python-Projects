from random import seed
from random import randrange
from csv import reader
from math import sqrt

# Load a csv file
def load_data(filename):
    dataset = []
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

def str_to_float(dataset):
    for row in dataset:
        for col in range(len(row)):
            row[col] = float(row[col])
            
def cross_validation(dataset, n_folds):
    folds = []
    fold_size = int(len(dataset) / n_folds)
    dataset_copy = list(dataset)
    
    for i in range(n_folds):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        folds.append(fold)
    return folds

# Calculating accuracy percentage
def accuracy_metrics(actual,predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

# Evaluate an algo using a coss validation split
def evaluate_algorithm(dataset,n_folds,algorithm, *args):
    scores = []
    folds = cross_validation(dataset,n_folds)
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train,[])      # Why have we passed empty list??
        test = []
    # add each row in given subsample to the test set
        for row in fold:
            row_copy = list(row)
            row_copy[-1] = None
            test.append(row_copy)
            
        predicted = algorithm(train,test, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metrics(actual,predicted)
        scores.append(accuracy)
        
    return scores

# Split a dataset bases on a attribute and an attribute value
# We can summarize this as the index of an attribute to split and the value by
# which to split rows on that attribute. This is just a useful shorthand for 
# indexing into rows of data.
def test_split(index,value,dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left,right

def gini_index(class_values,groups):
    gini = 0.0
    
    # for each class
    for class_value in class_values:
        for group in groups:
            size = len(group)
            
            # to avoid divide by zero
            if size == 0:
                continue
            
            # avg of all class values
            p = [row[-1] for row in group].count(class_value) / float(size)
            gini += p*(1.0 - p)
            
    return gini


# get_split()
# exhaustive and greedy algorithm
def get_split(dataset, n_features):    
# we must check every valueon each attribute as a candidate split
# evaluate the cost of split and find best possible split we could make

    class_value = list(set([row[-1] for row in dataset]))
    b_score,b_value,b_index,b_group = 999,999,999,None
    features = []
    
    while len(features) < n_features:
        index = randrange(len(dataset[0]) - 1)
        if index not in features:
            features.append(index)
                
                
    for index in features:
        for row in dataset:    
            groups = test_split(index,row[index],dataset)
            gini = gini_index(class_value,groups)
            
            if gini < b_score:
                b_index,b_value,b_score,b_group = index, row[index], gini, groups
            
    return {'value':b_value,'index':b_index,'groups':b_group}

def to_terminal(groups):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes),key=outcomes.count)

def split(depth,node,max_depth,min_size, n_features):
    
    left, right = node['groups']
    del(node['groups'])
    
    # we check if either left or right group of rows is empty and if so we create 
    # a terminal node using what records we do have.
    # Check for no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    
    # We then check if we have reached our maximum depth and if so we create a terminal node.
	# check for max depth
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left),to_terminal(right)
        return
    
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left, n_features)
        split(depth+1,node['left'],max_depth,min_size, n_features)
        
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(left, n_features)
        split(depth+1,node['right'],max_depth,min_size, n_features)
        
def build_tree(train, max_depth, min_size, n_features):
    root = get_split(train, n_features)
    split(1,root,max_depth,min_size, n_features)
    
    return root

def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
        
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']
        
def subsample(dataset, ratio):
    sample =[]
    n_sample = round(len(dataset) * ratio)
    
    while len(sample) < n_sample:
        index = randrange(len(dataset))
        sample.append(dataset[index])
    return sample

def bagged_predict(trees, row):
    predictions = [predict(tree, row) for tree in trees]
    return max(set(predicitons), key = predicitons.count)


def random_forest(train,test,max_depth,min_size,sample_size,n_tress,n_features):
    trees = []
    
    for i in range(n_trees):
        sample = subsample(train, sample_size)
        tree = build_tree(train,max_depth,min_size,n_features)
        trees.append(tree)
        
    predictions = [bagged_predict(trees, row) for row in test]
    return predictions

seed(1)


# load and prepare data
filename = 'german_credit.csv'
dataset = load_data(filename)
str_to_float(dataset)

n_folds = 5
max_depth = 10
min_size = 1
sample_size = 1.0
n_features = int(sqrt(len(dataset[0])-1))

for n_trees in [1,5,10]:
    scores = evaluate_algorithm(dataset, random_forest, n_folds, max_depth,min_size,sample_size,n_trees,n_features)
    print('Trees: %d' % n_trees)
    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
    