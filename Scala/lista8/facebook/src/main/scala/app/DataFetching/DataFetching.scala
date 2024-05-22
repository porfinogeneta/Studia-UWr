package app.DataFetching


object FacebookAdapter {
    private val myAppSecret = "EAAGM9YhZAOvABO2ZCYZCw8crd5csZCCPi15BjCf4VFHwlsWthwPk2DDxZBj1xi5QdFQymJg65eP2SViIXQEZBgNEZAspR2PyBTwFKdQHsqLguWwGcS08rZCOnHq7prNVRH5DFHv1AFKDuzlFrmHivt02vLKlEksRs6El9dFacScbJOMfNURRHbiFnVE5a2qY6Tx1oKUhOOSKIM8mId03lh4s5DUftAhifYTpPlD0QGsP124EZAmEHskpdKM6dZAuCZBtQZDZD" //any String (or Note1)
    class MyFacebookClient(currentAccessToken: String)
        extends DefaultFacebookClient(
        currentAccessToken,
        myAppSecret,
        Version.VERSION_5_0) {
    // //currentAccessToken is any String (or Note1)
    // ...
    }
    // ...
    // def getUser(accessToken: String, id: String) = ... {
    //     val client = new MyFacebookClient(accessToken)
    //     val user = client.fetchObject(id, classOf[User])
    //     user
    // }
}