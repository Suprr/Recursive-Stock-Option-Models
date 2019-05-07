# Put.py
1. Ensure Python can be run in the directory this sits and place input files in the same directory.
2. Run the American call option pricer:
```python put.py <INPUTFILE>```

# Call.py
1. Ensure Python can be run in the directory this sits and place input files in the same directory.
2. Run the Asian put option pricer:
```python call.py <INPUTFILE>```

## Inputs.txt
Input file must follow format as seen in inputs.txt:

```risk-free interest rate,time in years,timesteps,sigma (volatility of returns),spot price,strike price```

Note: each field is tab-separated
Note: To test multiple inputs: press enter (add a new line character) at the end of each line of input as seen in inputs.txt
