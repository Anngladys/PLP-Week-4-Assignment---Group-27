# data.py - Sample list of dictionaries
# You can imagine this data coming from a database, API, or file.
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "London"},
    {"name": "Charlie", "age": 35, "city": "Paris"},
    {"name": "David", "age": 25, "city": "Berlin"}
]

# --- 1. Manual Implementation ---
# Imagine you are typing this out character by character, recalling Python syntax.
def sort_list_of_dicts_manual(list_of_dicts, key, reverse=False):
    """
    Sorts a list of dictionaries by a specified key.
    Manual implementation.
    """
    return sorted(list_of_dicts, key=lambda d: d[key], reverse=reverse)

# Example usage for manual implementation:
print("--- Manual Implementation ---")
sorted_by_age_manual = sort_list_of_dicts_manual(data, 'age')
print("Sorted by age (manual):", sorted_by_age_manual)

sorted_by_name_desc_manual = sort_list_of_dicts_manual(data, 'name', reverse=True)
print("Sorted by name descending (manual):", sorted_by_name_desc_manual)
print("-" * 30)


# --- 2. AI-Suggested Code (Simulated GitHub Copilot Suggestion) ---
# Imagine you start typing "def sort_list_of_dicts_ai(" and Copilot instantly
# suggests the rest of the function and its implementation. You simply accept the suggestion.
def sort_list_of_dicts_ai(list_of_dicts, key, reverse=False):
    """
    Sorts a list of dictionaries by a specified key.
    AI-generated implementation (simulated).
    """
    return sorted(list_of_dicts, key=lambda d: d[key], reverse=reverse)

# Example usage for AI-suggested implementation:
print("--- AI-Suggested Implementation ---")
sorted_by_age_ai = sort_list_of_dicts_ai(data, 'age')
print("Sorted by age (AI):", sorted_by_age_ai)

sorted_by_city_ai = sort_list_of_dicts_ai(data, 'city')
print("Sorted by city (AI):", sorted_by_city_ai)
print("-" * 30)