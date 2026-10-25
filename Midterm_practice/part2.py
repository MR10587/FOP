# TASK 1
# def read_file(filename):
#     with open(filename, "r") as f:
#         fisherman_name = f.readline.strip()

#         fishes = []

#         for line in f:
#             fish = {
#                 "name": line[0],
#                 "weight": int(line[1])
#             }

#             fishes.append(fish)

#         return fisherman_name, fishes

# def print_data(fisherman_name, fishes):
#     print("\n" + fisherman_name)
#     print("-" * 48)

#     print(f"{"Name":>10}{"Weight":<10}")

#     for fish in fishes:
#         print(f"{fish["name"]:>10}{fish["weight"]:<10}")

# def find_sum(fishes):
#     return sum(fish["weight"] for fish in fishes)

# def amount_of_fish(fishes):
#     return len(fishes)

# TASK 2
# def parse_country_file(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as f:
#             lines = []
#             for line in f:
#                 line = line.strip()
#                 if line:
#                     lines.append(line)
#     except:
#         return None, []
        
#     if not lines:
#         return None, []
        
#     country_name = lines[0]
#     cities = []
#     idx = 1
#     while idx < len(lines):
#         try:
#             city_name = lines[idx]
#             population = int(lines[idx+1])
#             area = float(lines[idx+2])
#             rivers = int(lines[idx+3])
            
#             cities.append({
#                 'name': city_name,
#                 'population': population,
#                 'area': area,
#                 'rivers': rivers
#             })
#             idx += 4
#         except:
#             break
            
#     return country_name, cities

# def find_city_with_most_rivers(cities):
#     if not cities:
#         return None
#     top_city = cities[0]
#     for city in cities:
#         if city['rivers'] > top_city['rivers']:
#             top_city = city
#     return top_city

# def calculate_total_population(cities):
#     total = 0
#     for city in cities:
#         total += city['population']
#     return total

# def print_country_report(country_name, cities, most_rivers_city, total_pop):
#     print(f"--- Report for {country_name} ---")
#     print(f"Total Population of main cities: {total_pop}")
#     if most_rivers_city:
#         print(f"City with the most rivers: '{most_rivers_city['name']}' ({most_rivers_city['rivers']} rivers)")
#     print()

# def analyze_countries(file1, file2):
#     c1_name, c1_cities = parse_country_file(file1)
#     c2_name, c2_cities = parse_country_file(file2)
    
#     c1_top_river = find_city_with_most_rivers(c1_cities)
#     c1_total_pop = calculate_total_population(c1_cities)
#     if c1_name:
#         print_country_report(c1_name, c1_cities, c1_top_river, c1_total_pop)
        
#     c2_top_river = find_city_with_most_rivers(c2_cities)
#     c2_total_pop = calculate_total_population(c2_cities)
#     if c2_name:
#         print_country_report(c2_name, c2_cities, c2_top_river, c2_total_pop)
        
#     if c1_name and c2_name:
#         if c1_total_pop > c2_total_pop:
#             print(f"Result: {c1_name} has a larger city population than {c2_name}.\n")
#         elif c2_total_pop > c1_total_pop:
#             print(f"Result: {c2_name} has a larger city population than {c1_name}.\n")
#         else:
#             print("Result: Both countries have the exact same combined city population.\n")

# TASK 3
# def parse_trainer_file(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as f:
#             lines = []
#             for line in f:
#                 line = line.strip()
#                 if line:
#                     lines.append(line)
#     except:
#         return None, []
        
#     if not lines:
#         return None, []
        
#     trainer_name = lines[0]
#     patients = []
#     idx = 1
#     while idx < len(lines):
#         try:
#             surname = lines[idx]
#             first_name = lines[idx+1]
#             phone = lines[idx+2]
#             age = int(lines[idx+3])
#             height = float(lines[idx+4])
#             start_weight = float(lines[idx+5])
#             weight_lost = float(lines[idx+6])
            
#             patients.append({
#                 'full_name': f"{first_name} {surname}",
#                 'phone': phone,
#                 'age': age,
#                 'height': height,
#                 'current_weight': round(start_weight - weight_lost, 2),
#                 'weight_lost': weight_lost
#             })
#             idx += 7
#         except:
#             break
            
#     return trainer_name, patients

# def find_oldest_patient(patients):
#     if not patients:
#         return None
#     oldest = patients[0]
#     for patient in patients:
#         if patient['age'] > oldest['age']:
#             oldest = patient
#     return oldest

# def find_max_weight_cutter(patients):
#     if not patients:
#         return None
#     cutter = patients[0]
#     for patient in patients:
#         if patient['weight_lost'] > cutter['weight_lost']:
#             cutter = patient
#     return cutter

# def evaluate_and_compare_trainers(file1, file2):
#     t1_name, t1_patients = parse_trainer_file(file1)
#     t2_name, t2_patients = parse_trainer_file(file2)
    
#     oldest_t1 = find_oldest_patient(t1_patients)
#     oldest_t2 = find_oldest_patient(t2_patients)
    
#     cutter_t1 = find_max_weight_cutter(t1_patients)
#     cutter_t2 = find_max_weight_cutter(t2_patients)
    
#     if t1_name:
#         print(f"=== Trainer Group: {t1_name} ===")
#         if oldest_t1:
#             print(f"Oldest Patient: {oldest_t1['full_name']} ({oldest_t1['age']} years old)")
#         if cutter_t1:
#             print(f"Top Weight Loser: {cutter_t1['full_name']} (Lost: {cutter_t1['weight_lost']} kg, Current Weight: {cutter_t1['current_weight']} kg)")
#         print()
        
#     if t2_name:
#         print(f"=== Trainer Group: {t2_name} ===")
#         if oldest_t2:
#             print(f"Oldest Patient: {oldest_t2['full_name']} ({oldest_t2['age']} years old)")
#         if cutter_t2:
#             print(f"Top Weight Loser: {cutter_t2['full_name']} (Lost: {cutter_t2['weight_lost']} kg, Current Weight: {cutter_t2['current_weight']} kg)")
#         print()
            
#     if oldest_t1 and oldest_t2:
#         if oldest_t1['age'] > oldest_t2['age']:
#             print(f"Global Winner: Trainer {t1_name} has the oldest patient ({oldest_t1['full_name']}, {oldest_t1['age']} y/o).")
#         elif oldest_t2['age'] > oldest_t1['age']:
#             print(f"Global Winner: Trainer {t2_name} has the oldest patient ({oldest_t2['full_name']}, {oldest_t2['age']} y/o).")
#         else:
#             print(f"Global Winner: Both trainers share the oldest patient age bracket ({oldest_t1['age']} years old).")
