# data.py
import random


#Generating dashboard counter data
def generate_dashboard_counters():
    return {
        'pending': random.randint(1, 100),
        'allocated': random.randint(1, 100),
        'exited': random.randint(1, 100)
    }


#Generating prisoner data
def generate_prisoner():
    # Prisoner's requirements
    all_requirements = ["Drug Testing", "Counseling", "Job Training", "Education",
                 "Healthcare", "Security", "Transportation", "Family Visits"]

    # Picking random requirements
    num_requirements = random.randint(2, 4)
    needs = random.sample(all_requirements, num_requirements)

    # all the prisoner info
    return {
        "name": f"Prisoner {random.randint(100, 999)}",
        "id": f"PR-{random.randint(1000, 9999)}",
        "age": random.randint(18, 65),
        "needs": needs,
        "category": random.choice(['A', 'B', 'C']),
        "gender": random.choice(['Male', 'Female'])
    }


#Generating the RHU data
def generate_rhus(num=10):
    rhus = []

    #All the services the RHU provide
    all_services = ["Drug Testing", "Counseling", "Job Training", "Education",
                    "Healthcare", "Security", "Transportation", "Family Visits",
                    "Mental Health", "Religious", "Education"]

    #All the names of the different RHUs
    names = ["Hope House", "Bridge House", "New Start", "Pathway Centre",
             "Second Chance", "Harmony Hall", "Fresh Start", "Renewal House"]

    for i in range(num):
        #Picking random services
        num_services = random.randint(3, 6)
        services = random.sample(all_services, num_services)

        #Creating different RHUs at different locations
        rhu = {
            "name": f"{random.choice(names)} {random.randint(1, 5)}",
            "location": random.choice(["Newcastle", "Sunderland", "Durham", "Middlesbrough"]),
            "capacity": random.randint(10, 40),
            "services": services,
            "score": 0
        }
        rhus.append(rhu)

    return rhus


#Matching prisoners to the RHU based on the prisoner's licenses
def match_prisoner_to_rhus(prisoner, rhus):
    matched = []

    for rhu in rhus:
        # Count how many needs match services
        match_count = 0
        for need in prisoner["needs"]:
            if need in rhu["services"]:
                match_count += 1

        # Calculate match percentage
        total_needs = len(prisoner["needs"])
        if total_needs > 0:
            match_percent = int((match_count / total_needs) * 100)
        else:
            match_percent = 0

        #Adding to score each RHUs
        rhu_copy = rhu.copy()
        rhu_copy["score"] = match_percent
        matched.append(rhu_copy)

    #Sort by best match first
    matched.sort(key=lambda x: x["score"], reverse=True)
    return matched


#Release table data
def generate_release_table_data(count=10):
    data = []

    for i in range(count):
        data.append({
            'license': f"LIC-{random.randint(100, 999)}",
            'prison_id': f"PR-{random.randint(1000, 9999)}",
            'release_date': f"{random.randint(1, 28)}/{random.randint(1, 12)}/2024",
            'days_remaining': random.randint(1, 90)
        })

    return data


#Getting random RHU name
def get_random_RHU():
    names = ["Hope House", "Harmony Hall", "New Beginnings Center",
             "Second Chance Hostel", "Bridge House", "Pathway Centre"]
    return random.choice(names)