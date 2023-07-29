'''
This section imports onnx and onnxruntime to load the model and perform inference using our pre-trained machine learning model,
and numpy and pandas to manipulate data,
 pickle to load standard scaler fitted on out data set.
'''
import onnx
import onnxruntime as rt
import glob
import numpy as np
import pandas as pd
import pickle
import numpy as np
import pandas as pd
import warnings

'''
This function performs inference on the model to predict the KPIs and all units individual exergy losses. And sums them up to obtain total exergy loss.
It transforms the input data using a StandardScaler object, feeds it into the model, and calculates the total exergy loss from the output.
Finally, it returns the output with the total exergy loss column appended.
'''
def Inference(x,session,scaler):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        x_standard = scaler[0].transform(x).astype('float32')
        y = session.run(['outputs'], {'x': x_standard})[0]
        y = scaler[1].inverse_transform(y)
        total_exergy_loss = np.absolute(np.array([y[:, -4] + y[:, -3] + y[:, -2] + y[:, -1]]))
        total_exergy_loss = np.transpose(total_exergy_loss)
        y = np.hstack((y, total_exergy_loss))
        return y
    
'''
This part loads the scaler of dataset from a pickle file. So theres no need for dataset to scale the inputs.
'''
with open('scaler.pickle', 'rb') as f:
    # unpickle the object from the file
    scaler = pickle.load(f)
    

'''
This section loads a pre-trained model from file named model.onnx, and creates an inference session object.
'''
onnx_model_path = 'model.onnx'
model = onnx.load(onnx_model_path)
session = rt.InferenceSession(onnx_model_path)
np.set_printoptions(suppress=True)

gases = ['Methane', 'Ethane', 'Propane', 'Butane', 'Nitrogen', 'Ammonia', 'Chlorine', 'Ethylene', 'Propene', 'Isobutane']

'''
This section feeds the inputs into loaded model and obtains results such as the exergy losses, vapor fraction of compressor inlet and Minimum approach temprature 
'''
def predict(ins):
    ins=np.array(ins)
    ins[:10]=ins[:10]/np.sum(ins[:10])
    print('{:<10} {:<10}'.format('Gas', 'Molar Flow %'))
    print('-' * 25)
    for gas, mol_frac in zip(gases, ins[:10]):
        print('{:<10} {:<10.2%}'.format(gas, mol_frac))
    print('-' * 40)
    print('{:<30} {:<10.2f}'.format('MR1 molar flow', ins[10]))
    print('{:<30} {:<10.2f}'.format('Compressor inlet pressure', ins[11]))
    print('{:<30} {:<10.2f}'.format('Compressor outlet pressure', ins[12]))

    vapor_fraction, approach_temperature, exchanger_exergy_loss, compressor_exergy_loss, valve_exergy_loss, \
            aftercooler_exergy_loss, total_exergy_loss = Inference([ins],session,scaler)[0]
    print('\n\n --PREDICTIONS')
    print('-' * 40)
    print('{:<30} {:<10.2f}'.format('VF of compressor inlet', vapor_fraction))
    print('{:<30} {:<10.2f}'.format('Minimum approach temperature', approach_temperature))
    print('{:<30} {:<10.2f}'.format('Exchanger exergy loss', exchanger_exergy_loss))
    print('{:<30} {:<10.2f}'.format('Compressor exergy loss', compressor_exergy_loss))
    print('{:<30} {:<10.2f}'.format('Valve exergy loss', valve_exergy_loss))
    print('{:<30} {:<10.2f}'.format('Aftercooler exergy loss', aftercooler_exergy_loss))
    print('{:<30} {:<10.2f}'.format('Total exergy loss', total_exergy_loss))