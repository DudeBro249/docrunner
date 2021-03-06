from docrunner.utils.language import create_language_environment
import os
from typing import List, Optional

from ..utils.file import get_code_from_markdown, write_file


def run_javascript(
    directory_path: Optional[str] = None,
    markdown_path: Optional[str] = None,
    multi_file: Optional[bool] = None,
    startup_command: Optional[str] = None,
):
    code_snippets = get_code_from_markdown(
        language='javascript',
        markdown_path=markdown_path,
    )
    if not code_snippets:
        return None

    directory_path = create_language_environment(
        language='js',
        directory_path=directory_path,
    )

    filepath: str = None
    if multi_file:
        filepaths: List[str] = []
        for i in range(0, len(code_snippets)):
            filepath = f'{directory_path}/file{i + 1}.js'
            write_file(
                filepath=filepath,
                lines=code_snippets[i],
            )
            filepaths.append(filepath)
    else:
        all_lines = ''.join(code_snippets)
        filepath = f'{directory_path}/main.js'
        write_file(
            filepath=filepath,
            lines=all_lines,
        )
    
    if startup_command:
        startup_command = startup_command.replace('"', '')
        os.system(startup_command)
        return

    if multi_file:
        for filepath in filepaths:
            os.system(f'node {filepath}')
    else:
        os.system(f'node {filepath}')
