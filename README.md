# babbab 

The two purposes of `babbab` are: 

1. To be the *simplest* tool for Data Analysts/Statisticians to **analyze** A/B tests.
2. To return the *simplest* results for Stakeholders/Non-Statisticians to **understand**.

`babbab` an acronym of **BA**yesian **B**eta-**B**inomial **A**/**B** testing (`BaBBAB`), but it's spelled in lowercase (`babbab`) because it doesn't like shouting. 


## Install

This should work in vanilla Python +3.8. 

```bash
pip install babbab
```

## A quick example

Lets say we sell subscriptions to a paper magazine and want to conduct a simple A/B test. 

We want to change the background color of our app from grey to green because we want to know if changing the background color will increase sales. To do so, we assign 50% of our users to the new app design with a green background (The Variant Group), while other 50% stay in the old grey design (the Control group). We managed to pull these 4 numbers out our tracking into Python:

```python
control_sold_subscriptions = 200 
control_users = 40316
variant_sold_subscriptions = 250
variant_users = 40567
```

Because `babbab` is awesome you can just run:

```python
import babbab as bab

plot, statement, trace = bab.quick_analysis(control_sold_subscriptions, 
                                            control_users, 
                                            variant_sold_subscriptions, 
                                            variant_users)
```

And get [everything you need](https://github.com/multilayer-io/babbab/blob/main/notebooks/should_be_pytest.ipynb).

1. In `plot` you will find a matplotlib figure. You can change the title and labels in the `quick_analysis` function. 
2. In `statement`, you will get a string that is intended to be interpreted verbatim by Non-Statisticians. 
3. In `trace`, you will get an [arviz InferenceData](https://python.arviz.org/en/latest/api/generated/arviz.InferenceData.html) object, in case you want to explore the run further. 

In the signature of `quick_analysis` you can configure the statistics and the aesthetics of most of this.  



## Motivation

A/B tests (or controlled experiments) are an increasingly popular way of incrementally improving websites, desktop, and mobile apps. At [Multilayer](https://multilayer.io) we have analyzed probably hundreds, with a miriad of different tools and statistical methodologies.

In our experience, when companies A/B tests the biggest problems they encounter are around interpreting the results and acting appropiately on them. There are plenty of statistical libraries out there that do A/B testing right (babbab actually uses [PyMC](https://www.pymc.io/welcome.html) in the background). However, sharing statistics (like p-values) with non-statisticians can lead to confusion and [misuse](https://en.wikipedia.org/w/index.php?title=Misuse_of_p-values&oldid=1064797942) of results. 

What `babbab` tries to cover is the "last mile" of the A/B test analysis: Interpreting and communicating the results for them to be actionable.


### In other words - Why `babbab` is awesome

- Get 4 numbers in, get a statistically valid statement that you can repeat to your manager verbatim, and a plot you can understand. 
- Get 4 numbers in + some labels, and you will get the above *and* a plot you can share *and* a statement you can C&P in the company chat.
- Add a bit more work, and you have your own custom built AB testing dashboard/tool.

Stop worrying about your peers and yourself misinterpreting stats. 

## TODO list 

Still a lot to basic docs to do.

- Add example results (plot, statement) to the README
- Add example with labels to README 
- Add docstrings

Maybe?

- Sphinx or RTD Documentation
