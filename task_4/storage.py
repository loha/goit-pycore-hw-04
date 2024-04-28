from uuid import uuid4

def add_user_to_store(name, phone):
  new_user = {
    "id": str(uuid4()),
    "name": name,
    "phone": phone,
  }
  users.append(new_user)
  return new_user

def find_all_users_from_store():
  return users

def update_user_by_id(id, new_name, new_phone):
  user_data = get_user("id", id)

  if user_data:
    user_data["name"] = new_name
    user_data["phone"] = new_phone
    return True
  else:
    return False

def get_user_phone_by_name(name):
  user_data = get_user("name", name)

  if user_data:
    return user_data["phone"]
  
  return user_data

def get_user(search_column, value):
  for user in users:
    if user[search_column] == value:
      return user
  
  return None
  

users: list = []