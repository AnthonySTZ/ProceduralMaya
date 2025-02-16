class QtInfo:

    @staticmethod
    def reloadQtCore():
        from importlib import reload
        import Core.Qt.QDataAction as QDataAction

        reload(QDataAction)
