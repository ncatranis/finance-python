# finance-python
Experiments working with financial data

## Environment Setup
1. Get miniconda
2. Create the vitual environment
```
conda create -n finance-python python=3.10
conda activate finance-python
pip install -r requirements.txt
```
3. Configure your own `.env` file - this is not saved to git. See `.env.example` for necessary keys and `config.py` for how they get used.
This is a non-exhaustive list of what you will need
* An IEX API token - https://iexcloud.io/console/home, it should be the public key, not the secret, and start with `pk_`
4. In a console with your `finance-python` python environment active, run `jupyter-lab` in a console
5. Run the `StockExplorer.ipynb` notebook
