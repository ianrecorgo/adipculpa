def get_api_call_data(url):
    """
    Makes an API call to the given URL and returns the response.

    Args:
        url (str): The URL to make the API call to.

    Returns:
        The response from the API call.
    """

    # Make the API call.
    response = requests.get(url)

    # Check if the API call was successful.
    if response.status_code != 200:
        raise Exception("API call failed with status code {}".format(response.status_code))

    # Return the response from the API call.
    return response.json()
