# Importing Training Data Functions

from training_data.training_data_api_requests import *
from training_data.training_data_json_to_dataframe_conversion import *

# Importing Testing Data Functions

from testing_data.testing_data_api_requests import *
from testing_data.testing_data_json_to_dataframe_conversion import *

# Importing Training Extension Data Functions

from training_data_extension.extension_data_json_to_dataframe_conversion import *
from training_data_extension.extension_data_api_requests import *

# Importing Data Cleaning Functions

from training_data.training_data_cleaning import *
from testing_data.testing_data_cleaning import *
from training_data_extension.extension_data_cleaning import *

# Data Analysis and the steps taken from that point onwards can be found in the Jupyter Notebook Files

import numpy as np

if __name__ == '__main__':

    # Generate Both Training Data Sets

    get_train_data()

    json_training_data_to_dictionary()

    # Generate Both Testing Data Sets

    get_test_data()

    json_test_data_to_dictionary()

    # Generate Both Training Extension Data Sets

    json_training_extension_data_to_dictionary()

    get_training_extension_data()

    # Clean the Generated Files

    training_data_cleaning()

    test_data_cleaning()

    extension_data_cleaning()

    print('MESSAGE: Run Complete')





