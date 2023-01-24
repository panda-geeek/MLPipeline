import numpy as np
import pandas as pd

if __name__=='__main__':
    np_array = np.array([1, 2, 3])
    print("Sum of Numpy Array: ",np.sum(np_array))
    df = pd.DataFrame(np_array)
    print("Pandas Dataframe >>>>>>>>>>>>>>>>>:  ", df)