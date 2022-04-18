def create_story(files):
    story = []
    for file_name in files:
        with open(file_name, encoding='utf-8') as file:
            text = file.readlines()
            story.append([file_name + '\n', str(len(text)) + '\n'] + text)
    print(story)
    story.sort(key=len)

    with open('story.txt', 'w', encoding='utf-8') as file:
        for texts in story:
            for string in texts:
                file.write(string)
            file.write('\n')


create_story(['1.txt', '2.txt', '3.txt'])