echo "Installing dependencies"

sudo apt-get update
sudo apt-get --yes install flite
sudo apt-get --yes install clang
sudo apt-get --yes install git-core
sudo apt-get --yes install swig
sudo apt-get --yes install python-pyaudio
sudo apt-get --yes install portaudio19-dev
sudo apt-get --yes install flac
sudo apt-get --yes install omxplayer
sudo pip3 install SpeechRecognition
sudo pip3 install google-api-python-client
sudo pip3 install pyaudio

