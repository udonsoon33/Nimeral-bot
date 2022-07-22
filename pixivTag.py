from pixivpy3 import *

api = AppPixivAPI()
# (method) set_auth: (access_token: str, refresh_token: str | None = None) -> None
api.set_auth("JgRaoVOxsvYs4-cVNUIZaq4RmckMGKksmmxM_LRNxc8",
             "KiPxs-kUcYNJp5W-e45d-67U460xVw6F_m703UMwprY")


def get_tags(id):
    json_result = api.illust_detail(id)
    illust = json_result.illust
    return(illust.tags)


if __name__ == "__main__":
    print(">>> tags: %s" % get_tags(98918516))
