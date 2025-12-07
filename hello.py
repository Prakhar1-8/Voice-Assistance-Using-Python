import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim
import folium
import webbrowser
import os

def track_mobile_number(phone_number):
    """Simulate mobile number tracking (demo purposes only)"""
    try:
        
        parsed_number = phonenumbers.parse(phone_number)
        
        service_provider = carrier.name_for_number(parsed_number, "en")
        
        # Get geographical location (country/city)
        location = geocoder.description_for_number(parsed_number, "en")
        
        # Print basic information
        print(f"\nTracking information for: {phone_number}")
        print(f"Country/City: {location}")
        print(f"Service Provider: {service_provider}")
        
        # Get approximate coordinates (this is a simulation)
        # In real applications, you would need actual GPS data
        geolocator = Nominatim(user_agent="geo_tracker")
        location_data = geolocator.geocode(location)
        
        if location_data:
            # Create a map (simulation)
            my_map = folium.Map(location=[location_data.latitude, location_data.longitude], zoom_start=10)
            folium.Marker([location_data.latitude, location_data.longitude],
                          popup=f"Approximate location of {phone_number}").add_to(my_map)
            
            # Save the map to HTML
            map_file = "phone_location.html"
            my_map.save(map_file)
            
            # Open in browser
            print("\nOpening approximate location in browser...")
            webbrowser.open(f'file://{os.path.abspath(map_file)}')
        else:
            print("\nCould not determine exact coordinates for this location")
            
    except Exception as e:
        print(f"\nError: {e}")
        print("Please check if the phone number is valid and in international format (+[country code][number])")

if __name__ == "__main__":
    print("MOBILE NUMBER TRACKING DEMONSTRATION")
    print("====================================")
    print("NOTE: This is for educational purposes only")
    print("Actual phone tracking requires proper authorization\n")
    
    phone_num = input("Enter phone number in international format (e.g., +919876543210): ")
    track_mobile_number(phone_num)
