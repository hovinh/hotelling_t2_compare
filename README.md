# Introduction

Hotelling's T2 is widely used as a multi-variate chart for monitoring purpose, say, quality control in manufacturing domain. It alleviates the difficulty in monitoring many sensors at the same time. Intuitively, it combines standardized deviation of individual sensor (or feature in Machine Learning domain) from the general mean, weighted by their correlation pair, to a single numerical value.  

Surprisingly, there is no standard package for Hotelling's T2 in the year 2021, to my best knowledge. This is an attempt to compare all available source codes in various scenarios and rank them based on criterion set by me. 

## Package Listing

All packages listed here are code adapted from public repo I found in Github, hence belong to their corresponding author. 

- <a href="https://github.com/dionresearch/hotelling"> Francois Dion</a>.


## Environmental Setup

You create a virtual environment for this project by entering Anaconda Prompt, navigating to this directory:
```bash
conda env create -f environment.yml
```

Once succeed, you have a new conda virtual env named "edu_dtw". Alternatively, one can install them manually:
```bash
conda create -n hotelling_t2_compare python=3.6
pip install hotelling
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=hotelling_t2_compare
```
> Note: I encountered an error in pip's dependency solver, yet you can move on to run the test cases. Likely it still works, so you don't need spend time troubleshooting. 

## Getting-started
To be updated.


## Contact
Feel free to contact me via email: hxvinh.hcmus@gmail.com. Contributions are welcome.