friends = [
    ["James", "Malaysia", "Malacca"],
    ["Goh", "Australia", "Brisbane"],
    ["Sarah", "Malaysia", "Selangor"],
    ["Ahmad", "Malaysia", "Johor"],
    ["Emily", "Singapore", "Central"],
    ["Chen", "China", "Shanghai"],
    ["Priya", "India", "Mumbai"],
    ["James", "Australia", "Sydney"],
    ["Siti", "Malaysia", "Penang"],
    ["John", "United States", "California"]
]

def filterFriend(name="", home_country="", home_state=""):
    result = []
    for friend in friends:
        friend_name = friend[0]
        friend_country = friend[1]
        friend_state = friend[2]
        
        # Use conditions to check if friend matches all non-empty criteria
        match = True
        
        # Check name if provided (not empty)
        if name != "":
            if friend_name != name:
                match = False
        
        # Check home_country if provided (not empty)
        if home_country != "":
            if friend_country != home_country:
                match = False
        
        # Check home_state if provided (not empty)
        if home_state != "":
            if friend_state != home_state:
                match = False
        
        # Add friend to result if all criteria match
        if match:
            result.append(friend)

    return result

malaysian = filterFriend(home_country="Malaysia")
print("Friends from Malaysia: ", malaysian)

malaysian_penang = filterFriend(home_country="Malaysia", home_state="Penang")
print("Friends from Penang: ", malaysian_penang)

james_name = filterFriend(name = "James")
print("Friends named James: ", james_name)