
from kloppy import wyscout
dataset = wyscout.load("data/wyscout")  # Load from a JSON file
events  = dataset.to_pandas()                         # plain DataFrame
events.head()
