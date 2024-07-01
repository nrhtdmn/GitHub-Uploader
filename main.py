import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QTextEdit, QLineEdit, QLabel, QMessageBox)
from PyQt5.QtCore import Qt
import git
import subprocess
import webbrowser

class GitHubUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('GitHub Yükleyici')
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        # Repo Path
        self.repo_path = ''
        self.repo_label = QLabel('Seçilen Klasör:')
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        # Select Folder Button
        self.select_btn = QPushButton('Proje Klasörünü Seç', self)
        self.select_btn.clicked.connect(self.select_folder)

        # Generate requirements.txt Button
        self.req_btn = QPushButton('requirements.txt Oluştur', self)
        self.req_btn.clicked.connect(self.generate_requirements)
        self.req_btn.setEnabled(False)

        # Generate python_version.txt Button
        self.python_version_btn = QPushButton('python_version.txt Oluştur', self)
        self.python_version_btn.clicked.connect(self.generate_python_version)
        self.python_version_btn.setEnabled(False)

        # GitHub Remote URL Input
        self.remote_label = QLabel('GitHub Remote URL:')
        self.remote_input = QLineEdit(self)

        # Set Remote Button
        self.set_remote_btn = QPushButton('Remote URL Ekle', self)
        self.set_remote_btn.clicked.connect(self.set_remote)
        self.set_remote_btn.setEnabled(False)

        # Upload Button
        self.upload_btn = QPushButton('GitHub\'a Yükle', self)
        self.upload_btn.clicked.connect(self.upload_to_github)
        self.upload_btn.setEnabled(False)

        # Layout Setup
        main_layout.addWidget(self.repo_label)
        main_layout.addWidget(self.select_btn)
        main_layout.addWidget(self.req_btn)
        main_layout.addWidget(self.python_version_btn)
        main_layout.addWidget(self.remote_label)
        main_layout.addWidget(self.remote_input)
        main_layout.addWidget(self.set_remote_btn)
        main_layout.addWidget(self.upload_btn)
        main_layout.addWidget(self.text_edit)

        self.setLayout(main_layout)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Proje Klasörünü Seç')
        if folder:
            self.repo_path = folder
            self.repo_label.setText(f'Seçilen Klasör: {folder}')
            self.text_edit.append(f'Seçilen klasör: {folder}')
            self.req_btn.setEnabled(True)
            self.python_version_btn.setEnabled(True)
            self.set_remote_btn.setEnabled(True)

    def generate_requirements(self):
        if self.repo_path:
            req_path = os.path.join(self.repo_path, 'requirements.txt')
            result = subprocess.run(['pipreqs', self.repo_path, '--force'], capture_output=True, text=True)
            if result.returncode == 0:
                self.text_edit.append(f'requirements.txt oluşturuldu: {req_path}')
                self.upload_btn.setEnabled(True)
            else:
                self.text_edit.append(f'requirements.txt oluşturulurken hata: {result.stderr}')
        else:
            self.text_edit.append('Klasör seçilmedi!')

    def generate_python_version(self):
        if self.repo_path:
            version_path = os.path.join(self.repo_path, 'python_version.txt')
            with open(version_path, 'w') as f:
                f.write(f'Python {sys.version}\n')
            self.text_edit.append(f'python_version.txt oluşturuldu: {version_path}')
        else:
            self.text_edit.append('Klasör seçilmedi!')

    def set_remote(self):
        remote_url = self.remote_input.text()
        if remote_url and self.repo_path:
            try:
                repo = git.Repo.init(self.repo_path)
                if 'origin' in repo.remotes:
                    repo.delete_remote('origin')
                repo.create_remote('origin', remote_url)
                self.text_edit.append(f'Remote URL eklendi: {remote_url}')
                self.upload_btn.setEnabled(True)
            except Exception as e:
                self.text_edit.append(f'Remote URL eklenirken hata: {str(e)}')
        else:
            self.text_edit.append('Klasör veya URL girilmedi!')

    def upload_to_github(self):
        if self.repo_path:
            try:
                repo = git.Repo(self.repo_path)
                repo.git.add(all=True)
                repo.index.commit('Initial commit')
                origin = repo.remotes.origin
                origin.push(repo.head.ref)
                self.text_edit.append('GitHub\'a başarıyla yüklendi!')
                webbrowser.open(self.remote_input.text())
            except Exception as e:
                self.text_edit.append(f'GitHub\'a yüklenirken hata: {str(e)}')
        else:
            self.text_edit.append('Klasör seçilmedi!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitHubUploader()
    ex.show()
    sys.exit(app.exec_())
