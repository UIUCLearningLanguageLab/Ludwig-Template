"""
This file defines the hyper-parameters used for each Ludwig job.
By collecting multiple values per hyper-parameter in a list in param2requests, 
Ludwig will run jobs corresponding to all combination of hyper-parameter values. 
Any hyper-parameter not overwritten by param2requests will be assigned its default value using param2default.

Notes: 
- Ludwig relies on the dictionaries below to be named as-is. Do not rename them.
- Do not use dictionaries or other non-hashable objects as values in param2requests or param2default.

"""

# will submit 3*2=6 jobs, each using a different learning rate and "configuration"
param2requests = {
    'learning_rate': [0.1, 0.2, 0.3],
    'configuration': [(1, 0), (0, 1)],  # inner collections must be of type tuple, not list
}


param2default = {
    'learning_rate': 0.1,
    'configuration': (1, 0),
}
