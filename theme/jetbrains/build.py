import sublate as sub

print("[+] JetBrains")

for theme in sub.data["colors"]:
    sub.render(f"resources/schemes/{theme['id']}.xml", data={
        "theme": theme,
    })
    sub.render(f"src/{theme['id']}.theme.json", data={
        "theme": theme
    })

sub.rm("build.py")
