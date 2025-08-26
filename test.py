import requests
import json

def send_webhook(url, query_data):
    """
    Sends a POST request to a specified webhook URL with a JSON payload.

    Args:
        url (str): The webhook URL to which the request will be sent.
        query_data (str): The data to be sent in the 'query' field of the JSON body.

    Returns:
        None: Prints the status of the request and the response from the server.
    """
    # The webhook URL provided by you, sir.
    webhook_url = url

    # The data payload. The key is 'query' as you specified.
    # The value can be any string you need to send.
    payload = {
        "query": query_data
    }

    # Set the headers to indicate we are sending JSON data. A good practice.
    headers = {
        "Content-Type": "application/json"
    }

    print(f"Sending data to: {webhook_url}")
    print(f"Payload: {json.dumps(payload, indent=2)}")

    try:
        # Execute the POST request.
        response = requests.post(webhook_url, json=payload, headers=headers)

        print(response)
        # Print the response from the server, whether it's a success or failure message.
        print("Response from server:")
        try:
            # Try to print the response as JSON if possible.
            return  json.loads(json.dumps(response.json(), indent=2))
        except json.JSONDecodeError:
            # If it's not JSON, print it as plain text.
            print(response.text)
        print("done")

    except requests.exceptions.RequestException as e:
        # Handle potential network errors, like the URL being unreachable.
        print(f"\nAn error occurred while sending the request, sir.")
        print(f"Error: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    # The URL you provided.

    TARGET_URL = "https://lzh37mz8-5678.inc1.devtunnels.ms/webhook/n8n"
                  
    
    # The data you want to send in the 'query' variable.
    # Change this to whatever you need to test.
    

    while True:
        your_query = input(">> ")
        # Call the function to send the webhook.
        answer = send_webhook(TARGET_URL, your_query)
        if answer:
            print(answer.get("output"))

