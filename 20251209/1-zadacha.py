import json

def create_user_profile(filename="user.json", **kwargs):
    profile = dict(kwargs)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    create_user_profile(name="Gandalf", email="gandalf@main.com", age=48, country="Middle Earth")
    print("User profile saved to user.json")

