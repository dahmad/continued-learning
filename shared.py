from glob import glob

directory_origin = 'sources'
directory_target = 'notes'
file_format_origin = '.pdf'
file_format_target = '.yml'

file_paths_origin = sorted(glob(f"{directory_origin}/*{file_format_origin}"))
file_paths_target = sorted(glob(f"{directory_target}/*{file_format_target}"))