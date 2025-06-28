from utils.helpers import *
from config.paths_config import*
from pipeline.prediction_pipeline import hybrid_recomndation


# similar_users=find_similar_user(11880,USER_WEIGHTS_PATH,USER2USERENCODE,USER2USERDECODE)
# print(similar_users)

# user_preference = get_user_preferences(11880, RATING_DF,DF_PATH)
# print(user_preference)

# user_recommended_animes = get_user_recommedations(similar_users,user_preference,DF_PATH,SYNOPSIS_DF, RATING_DF)
# print(user_recommended_animes)
user_id = 11880
            
recommendations = hybrid_recomndation(user_id)

print(recommendations)