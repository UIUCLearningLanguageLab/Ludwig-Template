"""
This file defines the hyper-parameters used for each Ludwig job.
By collecting multiple values per hyper-parameter in a list in param2requests, 
Ludwig will run jobs corresponding to all combination of hyper-parameter values. 
Any hyper-parameter not overwritten by param2requests will be assigned its default value using param2default.

Notes: 
- Ludwig requires that the two dicts in this file be named as they are below. Do not rename them.
- Do not use non-hashable objects as values in param2requests or param2default.

"""

# will submit 3*2=6 jobs, each using a different learning rate and hidden sizes
param2requests = {
    'learning_rate': [0.1, 0.2, 0.3],
    'hidden_sizes': [(16, 8), (16, 16)],  # inner collections must be of type tuple, not list
}


param2default = {
    'learning_rate': 0.1,
    'hidden_sizes': (16, 16),
}
