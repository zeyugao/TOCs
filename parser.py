import re

match_secion = re.compile(r'(第\d+章|第\w+章)(.*?)[.⋯]*(\d+)$')
match_subsection = re.compile(r'(\d{1,2}\.\d{1,2}(\.\d)?)(.*?)[.⋯]*(\d+)$')
match_attachments = re.compile(r'(附录\w|参考文献|索引)(.*?)[.⋯]*(\d+)$')

with open('book.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        section_result = match_secion.match(line)

        if section_result is not None:
            print(' '.join(section_result.groups()))
            continue

        subsection_result = match_subsection.match(line)
        if subsection_result is not None:
            print(' '.join([
                subsection_result.group(1),
                subsection_result.group(3),
                subsection_result.group(4)
            ]))
            continue

        attachments_result = match_attachments.match(line)
        if attachments_result is not None:
            print(
                ' '.join(attachments_result.groups()))
            continue

        raise Exception(line)
