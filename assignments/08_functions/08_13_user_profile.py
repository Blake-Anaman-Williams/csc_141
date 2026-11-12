def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

my_profile = build_profile(
    "Blake",
    "Williams",
    age=18,
    country="Ghana",
    major="Business Administration"
)

print(my_profile)