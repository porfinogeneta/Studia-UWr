package app.DataFetching


object FacebookAdapter {
    private val myAppSecret = "EAAGM9YhZAOvABORH5DFHv1AFKDuzlFrmHivt02vLKlEksRs6El9dFacScbJOMfNURRHbiFnVE5a2qY6Tx1oKUhOOSKIM8mId03lh4s5DUftAhifYTpPlD0QGsP124EZAmEHskpdKM6dZAuCZBtQZDZD" //any String (or Note1)
    
    class MyFacebookClient(currentAccessToken: String)
        extends DefaultFacebookClient(
        currentAccessToken,
        myAppSecret,
        Version.VERSION_5_0) {
                def this(accessToken: String) = this(accessToken, myAppSecret) // Default constructor with app secret
    }
    
    def getUser(accessToken: String, id: String) = ... {
        val client = new MyFacebookClient(accessToken)
        try {
            val user = client.fetchObject(id, classOf[User])
            Some(user)
        } catch {
            case e: FacebookException => 
            // Handle exception (e.g., invalid access token, user not found)
            None
        }
    }
}