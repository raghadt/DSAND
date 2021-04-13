import os
def find_files(suffix, path, files=[]):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    #  Handling cases:
    if path == None:
        return "no path found, kindly input a path"
    if suffix == None:
        return "no suffix found, kindly input a suffix"

    suffix+='/' + path
    
    try:
        suff = os.listdir(suffix)
    
    except:
        return "nothing found"

    for file in suff:
        new_path = suffix +  '/' + file
        
        if os.path.isfile(new_path) and  new_path[-2:]=='.c':
            files.append(new_path)
            
        elif os.path.isdir(new_path):
            files = find_files(suffix, file, files)
        
                
    return files
print('Test cases:')
print(find_files('.', 'testdir'))
print('------------------------------------------------')
print(find_files('.', ''))
print('------------------------------------------------')
print(find_files('.', 'testdir/subdir4'))
print('------------------------------------------------')
print(find_files('.', 'testdir/subdir5'))
print('------------------------------------------------')
print(find_files('.', 'testdir/subdi'))
print('------------------------------------------------')


