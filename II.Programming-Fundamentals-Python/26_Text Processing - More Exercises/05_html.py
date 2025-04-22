title = input()
content = input()

print(f"<h1>\n    {title}\n</h1>\n<article>\n    {content}\n</article>")

while True:
    comments = input()
    if comments == "end of comments":
        break

    print(f"<div>\n    {comments}\n</div>")
