# GitHub Yükleyici


Bu proje, bir Python projesini GitHub'a yüklemek için basit ve kullanıcı dostu bir arayüz sunan bir PyQt5 uygulamasıdır. Uygulama, proje klasörünü seçmenize, gerekli `requirements.txt` ve `python_version.txt` dosyalarını oluşturmanıza, GitHub uzak URL'sini eklemenize ve projeyi GitHub'a yüklemenize olanak tanır.

## Özellikler

- Proje klasörünü seçme
- `requirements.txt` dosyasını oluşturma
- Python sürüm bilgisini içeren `python_version.txt` dosyasını oluşturma
- GitHub uzak URL'sini ekleme
- Projeyi GitHub'a yükleme
- Yükleme sonrası GitHub depo sayfasını tarayıcıda açma

## Gereksinimler

- Python 3.x
- PyQt5
- GitPython
- pipreqs

## Kurulum

1. **Depoyu Klonlayın**:

    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    ```

2. **Gerekli Python Kütüphanelerini Yükleyin**:

    ```bash
    pip install PyQt5 gitpython pipreqs
    ```

## Kullanım

1. **Uygulamayı Başlatın**:

    ```bash
    python main.py
    ```

2. **Proje Klasörünü Seçin**:

    Uygulama arayüzünde "Proje Klasörünü Seç" butonuna tıklayarak proje klasörünüzü seçin.

3. **`requirements.txt` Dosyasını Oluşturun**:

    "requirements.txt Oluştur" butonuna tıklayarak proje bağımlılıklarını `requirements.txt` dosyasına yazdırın.

4. **`python_version.txt` Dosyasını Oluşturun**:

    "python_version.txt Oluştur" butonuna tıklayarak Python sürüm bilgisini içeren dosyayı oluşturun.

5. **GitHub Remote URL'sini Ekleyin**:

    GitHub depo URL'sini giriş alanına yazın ve "Remote URL Ekle" butonuna tıklayın.

6. **Projeyi GitHub'a Yükleyin**:

    "GitHub'a Yükle" butonuna tıklayarak projeyi GitHub'a yükleyin. Yükleme tamamlandığında GitHub depo sayfası tarayıcınızda açılacaktır.

## Hata Ayıklama

- Eğer bir hata ile karşılaşırsanız, uygulamanın alt kısmında bulunan metin alanında hata mesajları görüntülenecektir.
- Python, PyQt5, GitPython veya pipreqs kurulumunda bir sorun varsa, ilgili kütüphanelerin belgelerine başvurun.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir pull request oluşturun veya bir issue açın. Her türlü katkı ve geri bildirime açığız!

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

---

# GitHub Uploader

This project is a PyQt5 application that provides a simple and user-friendly interface for uploading a Python project to GitHub. The application allows you to select the project folder, generate the necessary `requirements.txt` and `python_version.txt` files, add the GitHub remote URL, and upload the project to GitHub.

## Features

- Select project folder
- Generate `requirements.txt` file
- Generate `python_version.txt` file with Python version information
- Add GitHub remote URL
- Upload project to GitHub
- Open GitHub repository page in the browser after upload

## Requirements

- Python 3.x
- PyQt5
- GitPython
- pipreqs

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    ```

2. **Install required Python libraries**:

    ```bash
    pip install PyQt5 gitpython pipreqs
    ```

## Usage

1. **Run the application**:

    ```bash
    python main.py
    ```

2. **Select Project Folder**:

    Click the "Proje Klasörünü Seç" (Select Project Folder) button in the application interface to select your project folder.

3. **Generate `requirements.txt` File**:

    Click the "requirements.txt Oluştur" (Generate requirements.txt) button to create the `requirements.txt` file with project dependencies.

4. **Generate `python_version.txt` File**:

    Click the "python_version.txt Oluştur" (Generate python_version.txt) button to create the `python_version.txt` file with Python version information.

5. **Add GitHub Remote URL**:

    Enter the GitHub repository URL in the input field and click the "Remote URL Ekle" (Add Remote URL) button.

6. **Upload Project to GitHub**:

    Click the "GitHub'a Yükle" (Upload to GitHub) button to upload the project to GitHub. The GitHub repository page will open in your browser upon completion.

## Troubleshooting

- If you encounter an error, the error messages will be displayed in the text area at the bottom of the application.
- Refer to the documentation of Python, PyQt5, GitPython, or pipreqs if there are issues with their installation.

## Contributing

If you would like to contribute, please create a pull request or open an issue. We welcome all contributions and feedback!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
