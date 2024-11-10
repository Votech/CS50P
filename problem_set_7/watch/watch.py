import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match_src = re.search(r'src="(.+?)"', s)
    if match_src:
        src = match_src.group(1)
        match_id = re.search(r"embed/(.+?)$", src)
        if match_id:
            id = match_id.group(1)
            return f"https://youtu.be/{id}"
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    main()
