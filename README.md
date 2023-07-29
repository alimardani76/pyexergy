# pyexergy                                           
The aim of this project is the fast calculation of exergy loss and KPIs of the PRICO process by a fully connected DNN. The calculations of exergy loss were carried out using the method developed in (https://doi.org/10.1016/j.jclepro.2020.123161) and the main simulation and collection of data is done via Python and HYSYS v8.8 interface.
## usage
Clone the full software package which includes the pre-trained model. The command is as follows:
```bash
git clone https://github.com/alimardani76/pyex
```
installing the presiquites:
cd to the directory where requirements.txt is located. 
activate your virtualenv. This command will install the packages according to the configuration file requirements.txt.
```bash
pip install -r requirements.txt 
```
## Usage of ML model 
The main_inference, notebook file simulates the PRICO process using calculations by our pre-trained model initiated in init.py. The features and the labels of the model are listed in the section below:
### The features:
        the composition of coolant gas:
        [1-10](Methane%, Ethane%, Propane%, Butane%, Nitrogen%, Ammonia%, Chlorine%, Ethylene%, Propene%, Isobutane%),
        [11]MR molar flow (kgmole/s) 
        [12]Compressor inlet pressure (kPa)
        [13]Compressor outlet pressure (kPa)
### The labels:
        [1]vapor_fraction of the compressor inlet,(-)
        [2]approach_temperature(C)
        [3]LNG_exergy_loss(MW)
        [4]compressor_exergy_loss(MW)
        [5]valve_exergy_loss(MW)
        [6]aftercooler_exergy_loss(MW)
