PKUnicorn
=====================
# Introduction
PKunicorn helps you to allocate your investment strategy in stock market. This tool will give you some statistical information, and tell you which stock you are supporsed to choose with different investment strategies! Now we plan to initially use two investment strategies. One is **CAPM approach**, the other is **Coupla Based-Pairs Trading Approach**. And we are going to add more strategies!
# Investment Strategy
## [CAPM Approach](https://www.quantconnect.com/tutorials/strategy-library/capm-alpha-ranking-strategy-on-dow-30-companies#CAPM-Alpha-Ranking-Strategy-on-Dow-30-Companies-Algorithm) 
The capital asset pricing model (**CAPM**) describes the relationship between systematic risk and expected return for assets, typically stocks. The formula for calculating the expected return of an asset given its risk is as follows:

<a href="https://www.codecogs.com/eqnedit.php?latex=\[r_a&space;=&space;r_f&space;&plus;&space;\beta_a*(r_m&space;-&space;r_f)&space;&plus;&space;\epsilon&space;\]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\[r_a&space;=&space;r_f&space;&plus;&space;\beta_a*(r_m&space;-&space;r_f)&space;&plus;&space;\epsilon&space;\]" title="\[r_a = r_f + \beta_a*(r_m - r_f) + \epsilon \]" /></a>

where:

<a href="https://www.codecogs.com/eqnedit.php?latex=\[r_f&space;=&space;Risk&space;Free&space;Rate\]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\[r_f&space;=&space;Risk&space;Free&space;Rate\]" title="\[r_f = Risk Free Rate\]" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\[\beta&space;=&space;Beta&space;of&space;the&space;security\]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\[\beta&space;=&space;Beta&space;of&space;the&space;security\]" title="\[\beta = Beta of the security\]" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\[r_m&space;=&space;Expected&space;market&space;return\]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\[r_m&space;=&space;Expected&space;market&space;return\]" title="\[r_m = Expected market return\]" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\[\epsilon&space;=&space;Tracking&space;error\]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\[\epsilon&space;=&space;Tracking&space;error\]" title="\[\epsilon = Tracking error\]" /></a>


This formula can be better understood if we refactor the formula as seen below:

<a href="https://www.codecogs.com/eqnedit.php?latex=\[(r_a&space;-&space;r_f&space;)&space;=&space;\beta_a*(r_m&space;-&space;r_f)&space;&plus;&space;\epsilon&space;\]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\[(r_a&space;-&space;r_f&space;)&space;=&space;\beta_a*(r_m&space;-&space;r_f)&space;&plus;&space;\epsilon&space;\]" title="\[(r_a - r_f ) = \beta_a*(r_m - r_f) + \epsilon \]" /></a>

The left side of the equation gives us the difference between the asset return and risk free rate, the "excess return". If we regress the market excess return against the asset excess return the slope represents the "beta" of the asset. Therefore, beta can also be calculated by the equation:

<a href="https://www.codecogs.com/eqnedit.php?latex=\[\beta&space;=&space;\frac{Cov(r_a,r_b)}{var(r_b)}\]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\[\beta&space;=&space;\frac{Cov(r_a,r_b)}{var(r_b)}\]" title="\[\beta = \frac{Cov(r_a,r_b)}{var(r_b)}\]" /></a>

So beta can be described as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\[\beta&space;=&space;\rho&space;_a,_b*\frac{\sigma&space;_a}{\sigma_b}\]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\[\beta&space;=&space;\rho&space;_a,_b*\frac{\sigma&space;_a}{\sigma_b}\]" title="\[\beta = \rho _a,_b*\frac{\sigma _a}{\sigma_b}\]" /></a>

The formula above indicates that beta can be explained as "correlated relative volatility". To make this simpler, beta can be calculated by doing a simple linear regression which can be viewed as a factor to explain the return, and the tracking error can represent alpha. To make this theory more convenient for our algorithm, we change the above formula into the following form:

<a href="https://www.codecogs.com/eqnedit.php?latex=\[r_a&space;=&space;\beta*r_m&space;&plus;&space;r_f*(1-\beta)&space;&plus;&space;\epsilon\]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\[r_a&space;=&space;\beta*r_m&space;&plus;&space;r_f*(1-\beta)&space;&plus;&space;\epsilon\]" title="\[r_a = \beta*r_m + r_f*(1-\beta) + \epsilon\]" /></a>

**<a href="https://www.codecogs.com/eqnedit.php?latex=r_f*(1-\beta)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_f*(1-\beta)" title="r_f*(1-\beta)" /></a>** on the right hand side of the equation is a very small item, making it negligible in the context of the Dow 30 companies. If we regress the stocks return with the return of the benchmark, the slope and intercept will be beta and alpha.
## [Coupla Based-Pairs Trading Approach](https://www.quantconnect.com/tutorials/strategy-library/pairs-trading-copula-vs-cointegration)
**Being edited......**
# Team Members
[@LY](https://github.com/PerfectBlue-ly)   [@JPT](https://github.com/brycejpt)   [@]()   [@]()   [@]()   [@]() 
#Reference Documentation
[CAPM Approach](https://www.quantconnect.com/tutorials/strategy-library/capm-alpha-ranking-strategy-on-dow-30-companies#CAPM-Alpha-Ranking-Strategy-on-Dow-30-Companies-Algorithm) 

[Coupla Based-Pairs Trading Approach](https://www.quantconnect.com/tutorials/strategy-library/pairs-trading-copula-vs-cointegration)
