class user:

  user_list = []

  def _init_(self, firstname, lastname,username,password) :

   self.firstname = firstname
   self.lastname = lastname
   self.username = username
   self.password = password

def store_user(self):

     user.user_list.append(self)

def delete_user(self):

      user.user_list.remove(self)

@classmethod
def display_users(cls):
    return cls.user_list

@classmethod
def find_by_username(cls,username):
   for user in cls.user_list:
       if user.password == username:
           return user
        
@classmethod
def user_exist(cls,username):
    for user in cls.user_list:
        if user.username == username:
            return True
            return False