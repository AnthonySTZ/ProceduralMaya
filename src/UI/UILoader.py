class UILoader:

    @staticmethod
    def reloadUI():
        from importlib import reload
        import UI.NodeTitleWidget as NodeTitleWidget
        import UI.NodeWidget as NodeWidget
        import UI.NodesView as NodesView
        import UI.MainWindow as MainWindow

        reload(NodeTitleWidget)
        reload(NodeWidget)
        reload(NodesView)
        reload(MainWindow)
