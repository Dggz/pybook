from testingtdd.blog import BlogPostHistory


blogger = BlogPostHistory(
    "New car from Dacia",
    "Dacia announced a new car yesterday. It is priced even lower than before"
)

print(f"The current post is {blogger.get_properties()}")
answear = input("Do you want to change anything? y/n:")

if answear == 'y':
    n_title = input("New title: ")
    blogger.change_title(n_title)
    n_desc = input("New description: ")
    blogger.change_description(n_desc)
else:
    print("Saving post!")

exit("Finished!")
