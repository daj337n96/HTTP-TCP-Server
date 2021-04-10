# HTTP-TCP-Server

This HTTP_TCP_server will display a webpage form promting the user to enter a text. The entered text will then be displayed on the webpage "You Entered: ".

data_to_client defines the HTTP string response to the client.
FORM defines the html string to be sent to display the webpage form.
FORM_REPLY defines the HTTP reply to the client after the text is entered.

Functions extract_object_POST and HTTP_response are used to retrieve the object from the client and send it back as a HTTP reponse to be displayed on the form.
Function server listens for any client attempting to connect and if so, creates a thread for the client.
Function handle_client will be called by the thread function to handle the clients connected.

Due to the browser limitattion on number of active tabs for the server, the function handle_client will be exited after 10 seconds.
