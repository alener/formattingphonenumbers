# Some conclusions about ths develop: TDD in ths particular way

 

In the first commit I had a minimun viable app with only a little large function and other code non-functional

When I wrote some interesting test (not trivial) I had to descompose this function and write anothers for this purpose

In this way, I could have keep descomposing functions for make more test, more really unitary test

For example, the actual test are interesting but are not desacompling from the code, because when it running, execute the mainly code

In order to do that, i would have to descompose even more the actual functions

Another interesting test, would be check if the required format is works and for do that I would have to descompose functions too.




## In conclusion, how would it be this way:



1. write a minimun viable app  (if it small)


2. try to make some interesting tests


3. for do that, little by little descompose code in small and "unitary" functions
   

4. At the end of this way you get a very maintanable, debuggeable an testeable code