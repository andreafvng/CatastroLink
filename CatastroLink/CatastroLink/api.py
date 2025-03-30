from google import genai
import os

api_key = os.getenv("GEMINI_API_KEY")

def get_matches(clients, hosts):
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    # Prepare the content to send as the request
    client_data = [{"name": client.name, "family_size": client.family_size, "pets": client.pets, 
                    "accommodations": client.accommodations, "location": client.location} for client in clients]
    
    host_data = [{"name": host.name, "family_size": host.family_size, "pets": host.pets, 
                  "accommodations": host.accommodations, "location": host.location} for host in hosts]
    
    content = f"""
    Clients: {client_data}
    Hosts: {host_data}
    Find the best matching hosts for each client based on family size, pets, accommodations, and location.
    """
    
    # Request from the Gemini API
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=content
    )

    # Parse and return the response
    return response.text