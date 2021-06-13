from TagMaker import TagMaker
from Tag_List import pb_tags

test_tweet = "police shown violently punched and pushed young protester with shield after he was maced and zip tied"

stem_test = TagMaker(test_tweet, pb_tags)

print(stem_test.tags())
