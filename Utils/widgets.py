from Utils.file_handling import get_file_content_of

def MakeCustomWidget(Loader,Target,StyleSheet):
    Loader.setupUi(Target)
    Target.setStyleSheet(get_file_content_of(StyleSheet))
