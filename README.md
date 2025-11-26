# AI Based Customer Chat Bot for Food Delivery Applications
The project aims to create an AI bot that addresses customer concerns regarding their usage of a food delivery app (such as Swiggy and Zomato) and provide solutions.
The project pipeline is as follows
1.	The Front End (Android Mobile App):
o	This is the user interface and the part which the customer interacts with.
o	It transfers the customer query to the server (backend of the app).
o	It is made using Android Studio.
2.	Spring Boot Gateway:
o	This handles the connection from the mobile app, which is fast and stable.
o	Its main job is to receive the request and forward it to the python the Python service). It manages the security and reliability of the internal network traffic.
3.	Python FastAPI and LLM
o	It receives the request and contacts the Large Language Model (LLM) to generate a helpful, human-like response.
o	Since generating a good answer can take a moment, we added an 60 second network timeout to ensure the process never fails.

Example Inputs and Outputs

The following examples confirm that the entire connection pipeline, from the android app’s input to the LLM response in the app is functional.
Input (User Question)	Output (Bot Response)	Status
What is the status of my order?	I'd be happy to check that for you! Your order, #1, is currently marked as 'Out for Delivery' and should arrive within the next 30 minutes.	SUCCESS
Can I get the phone number of the driver?	I apologize, for privacy reasons I cannot share the driver's direct number. Would you like me to send them a message to call you back?	SUCCESS
How long will the pizza take?	Your pizza order should arrive within the next 45 minutes."	SUCCESS

