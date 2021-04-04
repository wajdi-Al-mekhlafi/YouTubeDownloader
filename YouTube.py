# test cases: https://www.youtube.com/watch?v=7-qGKqveZaM		short video
#             https://www.youtube.com/watch?v=syBxfNIpZFc&t
#Coded by Wajdi 
# Youtube https://www.youtube.com/channel/UC8FJrnR1BAjYdEXfkPkwj6w"
# Facebook https://www.facebook.com/ramjaany.jaany/

from PyQt5 import QtCore, QtGui, QtWidgets
from pafy import new
import os 

class Ui_YouTubeDownloader(object):

    def setupUi(self, YouTubeDownloader):
        YouTubeDownloader.setObjectName("YouTubeDownloader")
        YouTubeDownloader.resize(900, 600)
        YouTubeDownloader.setMaximumSize(QtCore.QSize(900, 600))
        YouTubeDownloader.setMinimumSize(QtCore.QSize(900, 600))
        YouTubeDownloader.setWindowIcon(QtGui.QIcon("youtube.jfif"))
        self.centralwidget = QtWidgets.QWidget(YouTubeDownloader)
        self.centralwidget.setObjectName("centralwidget")

        self.pathLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathLabel.setGeometry(QtCore.QRect(40, 70, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pathLabel.setFont(font)
        self.pathLabel.setObjectName("pathLabel")
        self.pathLabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.pathLabel_1.setGeometry(QtCore.QRect(70, 370, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pathLabel_1.setFont(font)
        self.pathLabel_1.setObjectName("pathLabel_1")
        self.pathEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.pathEntry.setGeometry(QtCore.QRect(170, 70, 620, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pathEntry.setFont(font)
        self.pathEntry.setToolTipDuration(-1)
        self.pathEntry.setObjectName("pathEntry")
        self.pathEntry.editingFinished.connect(self.get_streams)

        self.Resolutions = QtWidgets.QGroupBox(self.centralwidget)
        self.Resolutions.setGeometry(QtCore.QRect(40, 170, 760, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Resolutions.setFont(font)
        self.Resolutions.setObjectName("Resolutions")

        self.res_144 = QtWidgets.QRadioButton(self.Resolutions)
        self.res_144.setEnabled(False)
        self.res_144.setGeometry(QtCore.QRect(30, 60, 140, 30))
        self.res_144.setObjectName("res_144")
        
        self.res_240 = QtWidgets.QRadioButton(self.Resolutions)
        self.res_240.setEnabled(False)
        self.res_240.setGeometry(QtCore.QRect(200, 60, 140, 30))
        self.res_240.setObjectName("res_240")
        
        self.res_360 = QtWidgets.QRadioButton(self.Resolutions)
        self.res_360.setEnabled(False)
        self.res_360.setGeometry(QtCore.QRect(380, 60, 140, 30))
        self.res_360.setObjectName("res_360")
        
        self.res_480 = QtWidgets.QRadioButton(self.Resolutions)
        self.res_480.setEnabled(False)
        self.res_480.setGeometry(QtCore.QRect(30, 150, 140, 30))
        self.res_480.setObjectName("res_480")
        
        self.res_720 = QtWidgets.QRadioButton(self.Resolutions)
        self.res_720.setEnabled(False)
        self.res_720.setGeometry(QtCore.QRect(200, 150, 140, 30))
        self.res_720.setObjectName("res_720")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 450, 650, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()
        
        self.progress_label = QtWidgets.QLabel(self.centralwidget)
        self.progress_label.setGeometry(QtCore.QRect(40, 450, 86, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progress_label.setFont(font)
        self.progress_label.setObjectName("progress_label")
        self.progress_label.hide()

        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(375, 525, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.download.setFont(font)
        self.download.setObjectName("download")
        self.download.clicked.connect(self.start_download)
        self.download_1 = QtWidgets.QPushButton(self.centralwidget)
        self.download_1.setGeometry(QtCore.QRect(70, 410, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download_1.setFont(font)
        self.download_1.setObjectName("Facebook")
        self.download_1.clicked.connect(self.coll)
        self.download_2 = QtWidgets.QPushButton(self.centralwidget)
        self.download_2.setGeometry(QtCore.QRect(200, 410, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download_2.setFont(font)
        self.download_2.setObjectName("YouTube")
        self.download_2.clicked.connect(self.you)
        YouTubeDownloader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(YouTubeDownloader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        YouTubeDownloader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(YouTubeDownloader)
        self.statusbar.setObjectName("statusbar")
        YouTubeDownloader.setStatusBar(self.statusbar)

        self.retranslateUi(YouTubeDownloader)

    def retranslateUi(self, YouTubeDownloader):
        _translate = QtCore.QCoreApplication.translate
        YouTubeDownloader.setWindowTitle(_translate("YouTubeDownloader", "Second YouTube Downloader "+"               "+"               "+"                  "+"Coded by Wajdi Al-Mekhlafi"))
        self.pathLabel.setText(_translate("YouTubeDownloader", "Video Path:"))
        self.pathLabel_1.setText(_translate("YouTubeDownloader", "Contact us:"))
        self.pathEntry.setToolTip(_translate("YouTubeDownloader", "YouTube video URL is placed here"))
        self.pathEntry.setStatusTip(_translate("YouTubeDownloader", "enter video path here..."))
        self.download.setText(_translate("YouTubeDownloader", "Download"))
        self.download_1.setText(_translate("YouTubeDownloader", "Facebook"))
        self.download_2.setText(_translate("YouTubeDownloader", "YouTube"))
        self.Resolutions.setToolTip(_translate("YouTubeDownloader", "Choose a resolution"))
        self.Resolutions.setStatusTip(_translate("YouTubeDownloader", "Available Resolutions"))
        self.Resolutions.setTitle(_translate("YouTubeDownloader", "Resoluation"))
        self.res_144.setText(_translate("YouTubeDownloader", "144p"))
        self.res_240.setText(_translate("YouTubeDownloader", "240p"))
        self.res_360.setText(_translate("YouTubeDownloader", "360p"))
        self.res_480.setText(_translate("YouTubeDownloader", "480p"))
        self.res_720.setText(_translate("YouTubeDownloader", "720p"))
        self.progress_label.setText(_translate("YouTubeDownloader", "Progress"))
        self.progressBar.setToolTip(_translate("YouTubeDownloader", "download progress"))
        self.progressBar.setStatusTip(_translate("YouTubeDownloader", "download progress"))

    def on_progress(self, total, recvd, ratio, rate, eta):
        self.progressBar.setProperty("value", int(ratio)*100)
        print("remaining time: ", int(eta), " Seconds")

    def get_streams(self):
        
        global Streams
        Streams = None
        URL = self.pathEntry.text()

        if not URL:
            return False

        Streams = new(URL).streams

        resolutions = [video.dimensions[1] for video in Streams]
        if 144 in resolutions:
            self.res_144.setEnabled(True)
        if 240 in resolutions:
            self.res_240.setEnabled(True)
        if 360 in resolutions:
            self.res_360.setEnabled(True)
        if 480 in resolutions:
            self.res_480.setEnabled(True)
        if 720 in resolutions:
            self.res_720.setEnabled(True)

    def get_file_name(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget,
            "QFileDialog.getSaveFileName()",
            "",
            "All Files (*);;Video Files (*.mp4)", 
            options=options)
        try:
            path = fileName[: fileName.rfind('/')]
            file_name = fileName[fileName.rindex('/')+1 : fileName.index('.')]
        except ValueError:
            file_name = ''
        except :
            file_name =  fileName[fileName.rindex('/')+1 : ]
        finally:
        	return (path, file_name)

    def start_download(self):
        if not self.pathEntry.text():
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("URL Error")
            msg.setInformativeText("Video URL field is empty")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return
        
        selected_resolution = [resolution.text() for resolution in [self.res_144, self.res_240, self.res_360, self.res_480, self.res_720] if resolution.isChecked()]
        if selected_resolution:
            selected_resolution = int(selected_resolution[0][:-1])
        elif not Streams:
            return
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("No resolution provided")
            msg.setInformativeText("Please select one of the available resolutions")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return

        video = None
        for stream in Streams:
        	if stream.dimensions[1] == selected_resolution:
        		print("in")
        		video = stream
        		break

        path, _ = self.get_file_name()

        self.progressBar.show()
        self.progress_label.show()
        video.download(filepath = path, quiet=True, callback= self.on_progress)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText("Download complete successfully")
        msg.setInformativeText("Video saved at: " + path)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    def coll(self):
        s="Hello"
    def you(self):
        s="Hello"
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YouTubeDownloader = QtWidgets.QMainWindow()
    ui = Ui_YouTubeDownloader()
    ui.setupUi(YouTubeDownloader)
    YouTubeDownloader.show()
    sys.exit(app.exec_())
