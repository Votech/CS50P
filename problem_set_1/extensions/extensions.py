def main():
    file_name = input("File name: ").strip().lower()
    file_name_split = file_name.rsplit(".", 1)
    file_name_extension = ""
    if len(file_name_split) == 2:
        file_name_extension = file_name_split[1]

    match file_name_extension:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("	application/zip")
        case _:
            print("application/octet-stream")


main()
