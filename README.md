# pyexergy
The aim of this project is the fast calculation of exergy loss and KPIs of the PRICO process by a fully connected DNN. The calculations of exergy loss was carried out using the method developed in (https://doi.org/10.1016/j.jclepro.2020.123161) and the main simulation and collection of data is done via python and HYSYS v8.8 interface.
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
## features and outputs of ML model 
In the main inference
### The features:
        the composition of coolant gas:
        [1-10](Methane%, Ethane%, Propane%, Butane%, Nitrogen%, Ammonia%, Chlorine%, Ethylene%, Propene%, Isobutane%),
        [11]MR1_molar_flow,(The refrigrant mole/s) 
        [12]Compressor inlet pressure
        [13]Compressor outlet pressure
### The labels:
        [1]vapor_fraction of the compressor inlet,
        [2]approach_temperature,
        [3]LNG_exergy_loss,
        [4]compressor_exergy_loss,
        [5]valve_exergy_loss and
        [6]aftercooler_exergy_loss
