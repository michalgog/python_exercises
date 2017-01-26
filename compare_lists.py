'''
Compare common start and end of two lists.
'''


def common_start_end_list(list1, list2):
    starts_match = list1[0] == list2[0]
    ends_match = list1[-1] == list2[-1]

    return starts_match and ends_match


print(common_start_end_list([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))


'''
Add html tag to the text.
'''


def add_html_tag(text, tag):
    return "<%s> %s </%s>" % (tag, text, tag)

print(add_html_tag("my title", "title"))
print(add_html_tag("my title", "strong"))
