# benchmarck-python-framework

The main goal is not to compare framework to each other but to show bottleneck and specificities of each framework.

This is an experiment done in the PyCon sprint. It has no goals to serve as a real benchmark tooling

Each framework should implement:
- A simple API endpoint that return a simple uniq char
- An API endpoint that stock data into the sqlit database
- An API endpoint that retrieve data from a sqlite database
- An API endpoint that return a file of 2MB
- An API endpoint that return a file of 10MB
