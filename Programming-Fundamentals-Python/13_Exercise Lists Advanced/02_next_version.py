current_version_str = input().split('.')
joined_version_str = ''.join(current_version_str)
incremented_version_num = int(joined_version_str) + 1
incremented_version_str = str(incremented_version_num)
new_version_list = list(incremented_version_str)
print('.'.join(new_version_list))
