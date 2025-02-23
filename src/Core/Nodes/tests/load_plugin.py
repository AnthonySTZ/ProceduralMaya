def load_plugin():

    import os

    os.system("cls")
    import sys

    from dotenv import load_dotenv

    load_dotenv()

    plugin_path = os.path.join(os.environ["PROCEDURAL_MAYA"], "src")

    sys.path.insert(0, plugin_path)
