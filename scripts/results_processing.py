import pandas as pd
from pandas.plotting import table 
import matplotlib.pyplot as plt
from IPython.display import display

def main():
    dropout_0 = pd.read_csv('../results/0_drop_model_results.csv')
    dropout_02 = pd.read_csv('../results/02_drop_model_results.csv')
    dropout_04 = pd.read_csv('../results/04_drop_model_results.csv')
    dropout_06 = pd.read_csv('../results/06_drop_model_results.csv')
    dropout_08 = pd.read_csv('../results/08_drop_model_results.csv')

    # create table for validation perplexities
    validation = pd.DataFrame()
    validation['Epoch'] = dropout_0.iloc[:,0]
    validation['Dropout 0'] = dropout_0.iloc[:,2]
    validation['Dropout 0.2'] = dropout_02.iloc[:,2]
    validation['Dropout 0.4'] = dropout_04.iloc[:,2]
    validation['Dropout 0.6'] = dropout_06.iloc[:,2]
    validation['Dropout 0.8'] = dropout_08.iloc[:,2]
    validation.set_index("Epoch", inplace = True)

    # display table
    display(validation)

    # plot line chart
    val_lines = validation.plot.line()
    val_lines.set_ylabel("Validation perplexity")
    val_fig = val_lines.get_figure()
    val_fig.savefig("../results/validation_ppl_results.png")

    
    # create table for training perplexities
    training = pd.DataFrame()
    training['Epoch'] = dropout_0.iloc[:,0]
    training['Dropout 0'] = dropout_0.iloc[:,1]
    training['Dropout 0.2'] = dropout_02.iloc[:,1]
    training['Dropout 0.4'] = dropout_04.iloc[:,1]
    training['Dropout 0.6'] = dropout_06.iloc[:,1]
    training['Dropout 0.8'] = dropout_08.iloc[:,1]
    training.set_index("Epoch", inplace = True)

    # display table
    display(training)

    # plot line chart
    train_lines = training.plot.line()
    train_lines.set_ylabel("Training perplexity")
    train_fig = train_lines.get_figure()
    train_fig.savefig("../results/training_ppl_results.png")


    # manually create table for test perplexities
    test = pd.DataFrame({'Dropout 0': [95.25],
                        'Dropout 0.2': [81.78],
                        'Dropout 0.4': [77.92],
                        'Dropout 0.6': [78.81],
                        'Dropout 0.8': [101.28]})
    # view table
    display(test)

if __name__ == "__main__":
    main()