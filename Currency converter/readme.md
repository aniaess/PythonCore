##### The Currency Converter is a simple console program that calculates the amount of money you get by converting one currency to another.
The FloatRates site contains a special JSON page for each currency. Program makes requests to these pages and download the actual data on the exchange rates of the US dollar and the euro.
Currency converter reads from the input the currency you have, the currency you want to exchange your money for, and the amount of money you want to exchange  
If he already did calculations for this exchange target before, converter know the rate, so there is no need to connect to the Internet and only need to refer to the data in cache.

> USD\
> EUR\
> 20\
Checking the cache...\
Oh! It is in the cache!\
You received 16.52 EUR.\
> NOK\
> 45\
Checking the cache...\
Sorry, but it is not in the cache!\
You received 382.1 NOK.\
> SEK\
> 75\
Checking the cache...\
Sorry, but it is not in the cache!\
You received 624.66 SEK.\
> NOK\
> 55\
Checking the cache...\
Oh! It is in the cache!\
You received 467.02 NOK.\
> ISK\
> 91\
Checking the cache...\
Sorry, but it is not in the cache!\
You received 11708.38 ISK.\
