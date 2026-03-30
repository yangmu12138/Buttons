data_file_path="C:/Users/Administrator/Desktop/Buttons/buttons_1/related_data.md"
warning_file_path="C:/Users/Administrator/Desktop/Buttons/buttons_1/warning_status.md"

def write_to_md(content_list):
    content="\n".join(content_list)
    content="\n"+content 
    with open(data_file_path, 'a+', encoding='utf-8') as f:
        f.write(content)

def write_warnings(content_list):
    content="\n".join(content_list)
    content="\n"+content 
    with open(warning_file_path, 'a+', encoding='utf-8') as f:
        f.write(content)