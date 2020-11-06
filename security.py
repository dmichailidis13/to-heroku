from models.user import UserModel


#username_mapping = {u.username: u for u in users}     We don't use them anymore because we 
#														have the methods from User class													
#userid_mappind = {u.id: u for u in users}

def authenticate(username,password):

	user = UserModel.find_by_username(username)
	if user is not None and user.password == password:
		return user 

def identity(payload):
	user_id = payload['identity']
	return UserModel.find_by_id(user_id)
