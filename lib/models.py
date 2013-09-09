from model_utils.managers import InheritanceManager


class AlwaysInheritanceManager(InheritanceManager):
    """
    Use this manager for a superclass so that the correct subclasses will be
    returned.
    """
    def get_query_set(self):
        return super(AlwaysInheritanceManager, self).get_query_set().select_subclasses()
