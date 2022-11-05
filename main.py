""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
import config

session = InstaPy(username=config.username,
                  password=config.password,
                  headless_browser=False,
                  )

with smart_run(session, False):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # activity
    session.like_by_tags(["chapadadosveadeiros"], amount=2)

