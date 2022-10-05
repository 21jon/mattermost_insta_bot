import mattermost
import os

token = None

with open(os.path.abspath("./secrets")) as f:
    token = f.read().replace("\\n", "").strip()

print(token)

# login
mm = mattermost.MMApi("https://computerclubmso.cloud.mattermost.com/api")
#mm.login("user@example.com", "my-pw")
# alternatively use a personal-access-token/bot-token.
mm.login(bearer=token)


# do stuff (print info about your user)


mm.create_post(channel_id="ichepx3rupgk9yyreb8wak99qy", message="hi")
# custom endpoint call (put server config)



# logout
mm.revoke_user_session()