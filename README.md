## BackendInterview
#### Task 1 REST
1. Import data to database.

2. Change type primary key from "int" to "UUID" and make sturture for support 2 language.

3. Generate REST API by ORM format output genaral REST API method (GET POST PUT PATCH and DELETE) 
    ```
    GET — R(etrieve) 
    POST — C(reate) 
    PUT — U(pdate) 
    PATCH - U(pdate)
    DELETE — D(elete) 
    ```  

4. This able serch and filter

        
#### Task 2 
In this challenge you should build an API for an application that stores and manages investments, it should have the following features
```
    1. __Creation__ of an investment with an owner, a creation date and an amount.
    1. The creation date of an investment can be today or a date in the past.
    2. An investment should not be or become negative.
    2. __View__ of an investment with its initial amount and expected balance.
        1. Expected balance should be the sum of the invested amount and the [gains][].
        2. If an investment was already withdrawn then the balance must reflect the gains of that investment
    3. __Withdrawal__ of a investment.
        1. The withdraw will always be the sum of the initial amount and its gains,
        partial withdrawn is not supported.
        2. Withdrawals can happen in the past or today, but can't happen before the investment creation or the future.
        3. [Taxes][taxes] need to be applied to the withdrawals before showing the final value.
    4. __List__ of a person's investments
        1. This list should have pagination.

```
#### Task 3 
1.
2.
3
4.