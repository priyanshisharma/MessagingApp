# MessagingApp

REST APIs have been generate to send and receive anonymous and unanonymous users.

Users shall register at 
`'/account/register` by filling email, username, password, password 2 (for confirmation )
then can then login at
`'/account/login` by filling their email and password

This will generate a token which will help access other functions, and also ability send messages to registered users.

A registered user can send amessage to username_A using his token by going to
`/<username_A>/create`
Entering "text" is compulsory for the same, entering "author" is optional.

Username A can view his list by going to `/<username_A>/list` using his token.
He/She can view and delete particular message by the following URLs
`'<int:pk>/delete'`
`'<int:pk>/detail'`
using his/her token.
