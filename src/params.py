# will submit 3*2=6 jobs, each using a different learning rate and "configuration"
param2requests = {
    'learning_rate': [0.1, 0.2, 0.3],
    'configuration': [(1, 0), (0, 1)],  # inner collections must be of type tuple, not list
}


param2default = {
    'learning_rate': 0.1,
    'configuration': (1, 0),
}
