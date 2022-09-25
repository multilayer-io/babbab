# babbab 

The two purposes of `babbab` are: 

- To be the *simplest* tool for Data Analysts/Statisticians to *analyze* AB tests.
- To return the *simplest* results for Stakeholders/Non-Statisticians to *understand*.

`babbab` an acronym of BAyesian Beta-Binomial AB testing (`BABBAB`), but it's spelled in lowercase (`babbab`) because it doesn't like shouting. 


## Install

This should work in vanilla Python +3.8. 

```bash
pip install babbab
```

## A quick example

Lets assume we are testing changing the background color of our app from grey to green. Lets say we sell subscriptions to a paper magazine. We want to know if changing the background color will increase sales. To do so, we assign 50% of our users to the new app design with a green background (The Variant Group), while other 50% stay in the old grey design (the Control group). We managed to pull these 4 numbers out our tracking into Python:

```python
control_sold_subscriptions = 200 
control_users = 40316
variant_sold_subscriptions = 250
variant_users = 40567
```

Because `babbab` is awesome you can just run:

```python
import babbab as bab

plot, statement, trace = bab.quick_analysis(control_sold_subscriptions, control_users, variant_sold_subscriptions, variant_users)
```

And get everything you need.

1. In `plot` you will find a matplotlib figure. You can change the title and labels in the `quick_analysis` function. 
2. In `statement`, you will get a string that is intended to be interpreted verbatim by Non-Statisticians. 
3. In `trace`, you will get an [arviz InferenceData](https://python.arviz.org/en/latest/api/generated/arviz.InferenceData.html) object, in case you want to explore the run further. 

In the signature of `quick_analysis` you can configure the statistics and the aesthetics of most of this.  



## Motivation

AB tests (or controlled experiments) are an increasingly popular way of incrementally improving websites, desktop, and mobile apps. At [Multilayer](https://multilayer.io) we have analyzed probably hundreds, with a miriad of different tools and statistical methodologies.

In our experience, when encountered with the typical AB test conducted in a website or mobile app, the biggest problem companies encounter is around interpreting the results. There are plenty of statistical libraries out there that do AB testing right (babbab actually uses [PyMC](https://www.pymc.io/welcome.html) in the background). However, sharing statistics (like p-values) with non-statisticians (and sometimes even with Statisticians) can lead to confusion and [misuse](https://en.wikipedia.org/w/index.php?title=Misuse_of_p-values&oldid=1064797942) of results. 

What `babbab` covers is the "last mile" of the analysis: Communicating the results for them to be actionable.


### In other words - Why `babbab` is awesome

- Get 4 numbers in, get a statistically valid statement you can repeat to your manager and a plot you can understand. 
- Get 4 numbers in + some labels, and you will get the above *and* a plot you can share *and* a statement you can C&P in the company chat.
- Add a bit more work, and you have your own custom built AB testing dashboard/tool.

Stop worrying about your peers and yourself misinterpreting stats. 

