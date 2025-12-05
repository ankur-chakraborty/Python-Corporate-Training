def top_n_students(marks_dict, n=3):
    return sorted(marks_dict.items(), key=lambda x: x[1], reverse=True)[:n]

marks = {"Aman": 78, "Riya": 92, "Kabir": 85, "Neha": 92, "Ira": 67}
print(top_n_students(marks))
