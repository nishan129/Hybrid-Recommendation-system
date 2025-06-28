from utils.helpers import *
from config.paths_config import*


similar_users=find_similar_user(11880,USER_WEIGHTS_PATH,USER2USERENCODE,USER2USERDECODE)
print(similar_users)

user_preference = get_user_preferences(11880, RATING_DF,DF_PATH)
print(user_preference)