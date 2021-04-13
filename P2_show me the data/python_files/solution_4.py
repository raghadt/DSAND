class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user=None, group=None):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    #--- handling cases:

    if user == None:
        print("No input for user")
        return False
    elif group == None:
        print("No input for group")
        return False

    if not isinstance(group, Group):
        print("Invalid group")
        return False



    if user == group.get_name():
        return True
    
    if user in group.get_users():
        return True
    
    for group_name in group.get_groups():
        return is_user_in_group(user, group_name)
    
    return False
        
print(is_user_in_group("parent", parent)==True)
print(is_user_in_group("child", child)==True)
print(is_user_in_group("", child)==False)
print(is_user_in_group("invalidgroup", 'group')==False)
print(is_user_in_group("child")==False)


